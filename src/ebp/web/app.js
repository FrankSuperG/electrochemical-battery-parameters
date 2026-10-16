"use strict";
const data = window.EBP_DATA;
const $ = id => document.getElementById(id);
const esc = value => String(value ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const safeUrl = value => /^https?:\/\//.test(value || "") ? esc(value) : "#";
const words = value => value.replaceAll("_", " ");
const directionLabel = {lithiation:"Lithiation", delithiation:"Delithiation", unspecified:"Direction unspecified"};
const colors = ["#287b78","#c39042","#718db0","#ab7489","#5a9c91","#889a51","#bc7560","#8080ae"];
const selected = new Set(["bpx-lfp18650-lfp-ocp", "lfp-afshar2017-formula", "sintef-lfp-d07eb6-c3-delithiation"]);
let detailId = "bpx-lfp18650-lfp-ocp";
const sourceLinks = ids => ids.map(id => `<a href="${safeUrl(data.sources[id].url)}" target="_blank" rel="noopener noreferrer">${esc(id)} ↗</a>`).join(" · ");
const number = value => Math.abs(value) !== 0 && (Math.abs(value) < .001 || Math.abs(value) >= 1e5) ? value.toExponential(5) : String(value);

$("total").textContent = data.records.length;
$("stats").innerHTML = [[data.records.filter(r=>r.representation.kind==="table").length,"Measured OCP branches · 4 specimens"],[data.records.filter(r=>r.representation.kind==="expression").length,"OCP expressions"],[data.parameters.length,"Model parameter records"],[data.full_cell_tests.length,"Full-cell experiment files"]].map(([n,label])=>`<div class="stat"><strong>${n}</strong><span>${esc(label)}</span></div>`).join("");

function filtered() {
  const query = $("query").value.toLowerCase().trim();
  return data.records.filter(r=>(!$("material").value||r.material===$("material").value)&&(!$("representation").value||r.representation.kind===$("representation").value)&&(!$("direction").value||r.direction===$("direction").value)&&(!query||JSON.stringify({...r,display_points:undefined}).toLowerCase().includes(query)));
}
function render() {
  const rows = filtered();
  $("result-count").textContent = `${rows.length} / ${data.records.length}`;
  $("records").innerHTML = rows.map(r=>`<article class="record ${selected.has(r.id)?"selected":""}"><div class="record-head"><button class="record-title" data-detail="${esc(r.id)}">${esc(r.title)}</button><input aria-label="Compare ${esc(r.id)}" type="checkbox" data-compare="${esc(r.id)}" ${selected.has(r.id)?"checked":""}></div><div class="record-tags"><span class="tag ${r.representation.kind==="expression"?"formula":""}">${r.representation.kind==="expression"?"Expression":"C/50 pseudo-OCP"}</span><span class="tag">${directionLabel[r.direction]}</span><span class="tag">${r.x.kind==="stoichiometry"?"Stoichiometry θ":"Branch throughput"}</span></div><small>${esc(r.id)}</small></article>`).join("")||'<p class="empty">No matching records. Adjust the search or filters.</p>';
  renderCharts();
}
$("records").addEventListener("click",event=>{const button=event.target.closest("[data-detail]");if(button){detailId=button.dataset.detail;renderDetail();$("detail").scrollIntoView({behavior:"smooth",block:"nearest"});}});
$("records").addEventListener("change",event=>{const target=event.target;if(target.dataset.compare){target.checked?selected.add(target.dataset.compare):selected.delete(target.dataset.compare);render();}});
for(const id of ["query","representation","direction"]) $(id).addEventListener(id==="query"?"input":"change",render);
$("material").addEventListener("change",()=>{selected.clear();const rows=filtered();for(const r of rows.filter(r=>r.representation.kind==="expression")) selected.add(r.id);const table=rows.find(r=>r.representation.kind==="table");if(table)selected.add(table.id);if(rows.length){detailId=rows[0].id;renderDetail();}render();});
$("reset").addEventListener("click",()=>{for(const id of ["query","material","representation","direction"]) $(id).value="";render();});
$("clear-selection").addEventListener("click",()=>{selected.clear();render();});

// Each plot uses its actual data domain; BPX operating bounds are not 0..1.
function plot(series, xLabel, yLabel) {
  const all=series.flatMap(s=>s.points);
  if(!all.length)return '<p class="empty">No valid observations to plot.</p>';
  const xmin=Math.min(...all.map(p=>p[0])),xmax=Math.max(...all.map(p=>p[0]));
  const lo=Math.min(...all.map(p=>p[1])),hi=Math.max(...all.map(p=>p[1])),pad=Math.max((hi-lo)*.08,.025),ymin=lo-pad,ymax=hi+pad;
  const X=x=>48+(x-xmin)/(xmax-xmin||1)*356,Y=y=>190-(y-ymin)/(ymax-ymin)*156;
  let svg=`<svg viewBox="0 0 430 238" role="img" aria-label="${esc(yLabel+" versus "+xLabel)}"><text x="48" y="20">${esc(yLabel)}</text>`;
  for(let i=0;i<=4;i++){const x=xmin+(xmax-xmin)*i/4,y=ymin+(ymax-ymin)*i/4;svg+=`<line class="grid" x1="48" x2="404" y1="${Y(y)}" y2="${Y(y)}"/><text x="40" y="${Y(y)+3}" text-anchor="end">${y.toFixed(2)}</text><text x="${X(x)}" y="209" text-anchor="middle">${x.toFixed(2)}</text>`;}
  svg+='<line class="axis" x1="48" x2="404" y1="190" y2="190"/>';
  svg+=series.map((s,i)=>`<path class="curve" stroke="${colors[i%colors.length]}" d="${s.points.map((p,j)=>`${j?"L":"M"}${X(p[0]).toFixed(2)},${Y(p[1]).toFixed(2)}`).join(" ")}"><title>${esc(s.label)}</title></path>`).join("");
  svg+=`<text x="225" y="232" text-anchor="middle">${esc(xLabel)}</text></svg>`;
  return svg+'<div class="legend">'+series.map((s,i)=>`<span><i style="background:${colors[i%colors.length]}"></i>${esc(s.label)}</span>`).join("")+"</div>";
}
function renderCharts() {
  const rows=data.records.filter(r=>selected.has(r.id));
  $("selected-count").textContent=`${rows.length} selected`;
  if(!rows.length){$("charts").innerHTML='<p class="empty">Select records to start comparing.</p>';return;}
  const groups=new Map();
  for(const r of rows){const key=r.x.kind+":"+r.direction+":"+r.material;if(!groups.has(key))groups.set(key,[]);groups.get(key).push(r);}
  $("charts").innerHTML=[...groups.values()].map(group=>{const first=group[0],stoich=first.x.kind==="stoichiometry";return `<section class="plot"><h3>${esc(first.material)} / ${esc(directionLabel[first.direction])}</h3>${plot(group.map(r=>({label:r.id,points:r.display_points})),stoich?"Electrode lithium fraction θ":"Normalized branch throughput","Potential / V vs Li/Li⁺")}<div class="axis-note">${stoich?"Each fit is plotted only inside its catalog domain. Domain limits and validity are documented per record.":"0 → 1 follows each branch's test progress. Branch endpoints do not establish equal lithium content."}</div></section>`;}).join("");
}
function renderDetail() {
  const r=data.records.find(r=>r.id===detailId),experiment=data.experiments[r.experiment_id];
  const field=(label,value)=>`<div class="field"><strong>${esc(label)}</strong>${value}</div>`;
  const licenses={"BSD-3-Clause":"PyBaMM-BSD-3-Clause.txt","MIT":"BPX-MIT.txt","CC-BY-4.0":"CC-BY-4.0.txt"};
  $("detail").innerHTML=`<div class="detail-top"><div><div class="eyebrow">RECORD / ${esc(r.id)}</div><h2>${esc(r.title)}</h2></div><div class="actions"><a class="button" href="downloads/${esc(r.id)}.csv" download>${r.representation.kind==="expression"?"Sampled formula CSV":"Retained points CSV"}</a><a class="button" href="downloads/${esc(r.id)}.json" download>Metadata JSON</a></div></div><div class="detail-grid">${field("Coordinate & domain",esc(r.x.definition)+`<br>[${r.x.domain.join(", ")}] · `+esc(r.x.domain_basis))}${field("Cell match",esc(r.cell_link.evidence))}${field("Conditions",esc(experiment?experiment.protocol+" · Cycle 3 · "+r.temperature.description:r.temperature.description))}${field("Data & validation",esc((r.representation.kind==="table"?r.representation.point_count+" retained measured points":"Expression; original measured points not supplied")+" · No independent full-cell validation"))}${field("Sources",sourceLinks(r.source_ids))}${field("License",`<a href="licenses/${licenses[r.license]}">${esc(r.license)}</a>`)}${field("Limits",'<ul>'+r.limitations.map(v=>`<li>${esc(v)}</li>`).join("")+"</ul>")}${field("Provenance",`<code>${esc(r.provenance.location)}</code><br>${esc(r.provenance.derivation)}`)}</div>${r.representation.kind==="expression"?`<div class="formula-text">${esc(r.representation.expression)}<br><small>x = θ; the 2001-point CSV is a numerical sample, not experimental data.</small></div>`:""}`;
}
$("source-cards").innerHTML=Object.entries(data.sources).map(([id,s])=>`<article class="source-card"><span class="tag">${esc(s.kind)} · ${esc(s.year)}</span><h3>${esc(s.title)}</h3><p>${esc(s.authors.join(", "))}</p><p>${esc(s.role)}</p><a href="${safeUrl(s.url)}" target="_blank" rel="noopener noreferrer">${esc(id)} ↗</a></article>`).join("");

const cellOrder=["a123-amp20m1hd-a","a123-high-power-pouch-9ah","bpx-lfp-18650-2ah-undisclosed","lg-m50"];
$("cell-select").innerHTML=cellOrder.map(id=>`<option value="${id}">${esc(data.cells[id].display_name)}</option>`).join("");
function renderCell() {
  const id=$("cell-select").value,cell=data.cells[id],parameters=data.parameters.filter(p=>p.cell_id===id),tests=data.full_cell_tests.filter(t=>t.cell_id===id);
  $("cell-title").textContent=cell.display_name;
  $("cell-context").textContent=cell.model_context||"DFN / SPM / SPMe reference parameterization";
  $("cell-match").innerHTML=`<b>Match: ${esc(words(cell.match_level))}.</b> ${esc(cell.match_evidence)}<br>No independent full-cell model validation has been performed by this project.`;
  $("cell-note").innerHTML=esc(cell.note)+(cell.external_ocp_references?'<br>'+cell.external_ocp_references.map(r=>`<a href="${safeUrl(r.url)}" target="_blank" rel="noopener noreferrer">External pseudo-OCV workbook ↗</a> · ${esc(r.status)}`).join("<br>"):"");
  $("cell-coverage").innerHTML=Object.entries(cell.coverage).map(([k,v])=>`<div><b>${esc(k==="ocp"?"OCP":words(k))}</b><span>${esc(v)}</span></div>`).join("");
  $("cell-downloads").innerHTML=`<a class="button" href="downloads/${id}-parameters.csv" download>Parameters CSV</a><a class="button" href="downloads/${id}-parameters.json" download>Cell package JSON</a>`;
  $("parameter-category").innerHTML='<option value="">All parameters</option>'+[...new Set(parameters.map(p=>p.category))].sort().map(c=>`<option value="${esc(c)}">${esc(words(c))}</option>`).join("");
  $("parameter-detail").innerHTML="";
  $("test-sample").innerHTML=tests.map(t=>`<option value="${esc(t.id)}">${esc(t.id)}</option>`).join("");
  $("test-sample").disabled=!tests.length;
  renderParameters();renderFullCell();
}
function renderParameters() {
  const rows=data.parameters.filter(p=>p.cell_id===$("cell-select").value&&(!$("parameter-category").value||p.category===$("parameter-category").value));
  $("parameter-count").textContent=`${rows.length} records`;
  $("parameter-rows").innerHTML=rows.map(p=>`<tr><td><button data-parameter="${esc(p.id)}">${esc(p.name)}</button>${p.conditions?.cell_SOC_fraction!==undefined?`<small class="condition">Cell SOC ${(p.conditions.cell_SOC_fraction*100).toFixed(0)}%</small>`:""}</td><td>${p.representation.kind==="scalar"?esc(number(p.representation.value)):"Function"}</td><td>${esc(p.unit)}</td></tr>`).join("")||'<tr><td colspan="3">No parameter values imported for this family. See coverage gaps above.</td></tr>';
}
$("parameter-rows").addEventListener("click",event=>{const button=event.target.closest("[data-parameter]");if(!button)return;const p=data.parameters.find(p=>p.id===button.dataset.parameter);$("parameter-detail").innerHTML=`<b>${esc(p.name)}</b><p>${esc(p.definition||p.name)}</p><p>Origin: ${esc(p.provenance.origin_status)}</p><code>${esc(p.representation.kind==="expression"?p.representation.expression:p.provenance.location)}</code><p>Conditions: ${esc(JSON.stringify(p.conditions||{}))}</p><p>${sourceLinks(p.source_ids)}</p><p>${p.limitations.map(esc).join("<br>")}</p>`;});
function renderFullCell() {
  const test=data.full_cell_tests.find(t=>t.id===$("test-sample").value);
  if(!test){$("test-description").textContent="No matching raw full-cell experiments supplied for this parameter example.";$("fullcell-chart").innerHTML='<p class="empty">Full-cell test coverage gap</p>';$("test-downloads").innerHTML="";$("test-note").textContent="No other cell's tests are substituted.";return;}
  $("test-description").textContent=test.protocol+". Measured voltage only; no model prediction overlay.";
  $("fullcell-chart").innerHTML=plot(test.preview_segments,"Time from trace / segment start / h","Full-cell voltage / V");
  const asset=data.assets[test.asset_id];
  $("test-downloads").innerHTML=(test.path?`<a class="button" href="downloads/${esc(test.path.split("/").pop())}" download>Original CSV</a>`:`<a class="button" href="${safeUrl(asset.url)}" target="_blank" rel="noopener noreferrer">Original ${test.original_member?"ZIP":"MAT"} ↗</a>`)+`<a class="button" href="downloads/${esc(test.normalized_path.split("/").pop())}" download>Normalized CSV</a>`;
  $("test-note").innerHTML=`${test.row_count.toLocaleString()} source rows retained. Display is decimated; valid voltage points only. Charge-positive current convention. ${esc(test.temperature_definition||"Cell and ambient temperature retained from the instrument file.")}<br>${esc(test.missing_values?"Missing counts: "+JSON.stringify(test.missing_values):"No missing values introduced.")}<br>${sourceLinks([test.source_id])} · Original SHA-256: <code>${esc(asset.sha256)}</code>`;
}
$("cell-select").addEventListener("change",renderCell);
$("parameter-category").addEventListener("change",renderParameters);
$("test-sample").addEventListener("change",renderFullCell);
render();renderDetail();renderCell();
