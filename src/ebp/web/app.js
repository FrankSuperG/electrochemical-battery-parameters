"use strict";
const data = window.EBP_DATA;
const $ = id => document.getElementById(id);
const esc = value => String(value ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const safeUrl = value => /^https?:\/\//.test(value || "") ? esc(value) : "#";
const words = value => value.replaceAll("_", " ");
const measurementLabel = r => r.representation.kind==="expression" ? "Expression" : ({literature_table:"Published OCP table",pseudo_ocp:"Finite-current pseudo-OCP",model_ocp:"Modeled PD-ECM OCPn"}[r.measurement] || words(r.measurement));
const coordinateLabel = {stoichiometry:"Stoichiometry θ",normalized_branch_capacity:"Branch throughput",model_soc:"Author model SOC/DOL",source_reported_stoichiometry:"Source-reported electrode coordinate"};
const directionLabel = {lithiation:"Lithiation", delithiation:"Delithiation", unspecified:"Direction unspecified"};
const colors = ["#287b78","#c39042","#718db0","#ab7489","#5a9c91","#889a51","#bc7560","#8080ae"];
const selected = new Set(["bpx-lfp18650-lfp-ocp", "lfp-afshar2017-formula", "sintef-lfp-d07eb6-c3-delithiation"]);
let detailId = "bpx-lfp18650-lfp-ocp";
const sourceLinks = ids => ids.map(id => `<a href="${safeUrl(data.sources[id].url)}" target="_blank" rel="noopener noreferrer">${esc(id)} ↗</a>`).join(" · ");
const channelLabels={time_s:"Original time coordinate",voltage_V:"Voltage",current_charge_positive_A:"Measured current",cell_temperature_K:"Absolute cell temperature",ambient_temperature_K:"Ambient temperature"};
const number = value => Math.abs(value) !== 0 && (Math.abs(value) < .001 || Math.abs(value) >= 1e5) ? value.toExponential(5) : String(value);

$("total").textContent = data.records.length;
$("stats").innerHTML = [[data.records.filter(r=>r.representation.kind==="table").length,"Tabulated electrode curves / model potentials"],[data.records.filter(r=>r.representation.kind==="expression").length,"OCP expressions"],[data.parameters.length,"Model parameter records"],[data.full_cell_tests.length,"Full-cell experiment files"]].map(([n,label])=>`<div class="stat"><strong>${n}</strong><span>${esc(label)}</span></div>`).join("");

function filtered() {
  const query = $("query").value.toLowerCase().trim();
  return data.records.filter(r=>(!$("material").value||r.material===$("material").value)&&(!$("representation").value||r.representation.kind===$("representation").value)&&(!$("direction").value||r.direction===$("direction").value)&&(!query||JSON.stringify({...r,display_points:undefined}).toLowerCase().includes(query)));
}
function render() {
  const rows = filtered();
  $("result-count").textContent = `${rows.length} / ${data.records.length}`;
  $("records").innerHTML = rows.map(r=>`<article class="record ${selected.has(r.id)?"selected":""}"><div class="record-head"><button class="record-title" data-detail="${esc(r.id)}">${esc(r.title)}</button><input aria-label="Compare ${esc(r.id)}" type="checkbox" data-compare="${esc(r.id)}" ${selected.has(r.id)?"checked":""}></div><div class="record-tags"><span class="tag ${r.representation.kind==="expression"?"formula":""}">${esc(measurementLabel(r))}</span><span class="tag">${directionLabel[r.direction]}</span><span class="tag">${esc(coordinateLabel[r.x.kind]||words(r.x.kind))}</span></div><small>${esc(r.id)}</small></article>`).join("")||'<p class="empty">No matching records. Adjust the search or filters.</p>';
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
  for(const r of rows){const key=r.x.kind+":"+r.direction+":"+r.material+":"+r.reference+":"+(r.measurement==="model_ocp"?r.id:"observations");if(!groups.has(key))groups.set(key,[]);groups.get(key).push(r);}
  $("charts").innerHTML=[...groups.values()].map(group=>{const first=group[0],stoich=first.x.kind==="stoichiometry";return `<section class="plot"><h3>${esc(first.material)} / ${esc(directionLabel[first.direction])}</h3>${plot(group.map(r=>({label:r.id,points:r.display_points})),coordinateLabel[first.x.kind],first.reference==="Li/Li+"?"Potential / V vs Li/Li⁺":"Half-cell voltage / V (reference unresolved)")}<div class="axis-note">${first.x.kind==="source_reported_stoichiometry"?"Source-reported coordinate; absolute lithium-fraction calibration requires explicit evidence. Native charging/discharging labels do not establish lithiation direction.":first.x.kind==="model_soc"?"Parameterized PD-ECM OCPn on its source model coordinate; not raw measured OCP or verified lithium fraction.":stoich?"Each fit is plotted only inside its catalog domain. Domain limits and validity are documented per record.":"0 → 1 follows the record's defined branch coordinate. Branch endpoints do not establish equal lithium content or chronological acquisition order."}</div></section>`;}).join("");
}
function renderDetail() {
  const r=data.records.find(r=>r.id===detailId),experiment=data.experiments[r.experiment_id];
  const field=(label,value)=>`<div class="field"><strong>${esc(label)}</strong>${value}</div>`;
  $("detail").innerHTML=`<div class="detail-top"><div><div class="eyebrow">RECORD / ${esc(r.id)}</div><h2>${esc(r.title)}</h2></div><div class="actions"><a class="button" href="downloads/${esc(r.id)}.csv" download>${r.representation.kind==="expression"?"Sampled formula CSV":"Retained points CSV"}</a><a class="button" href="downloads/${esc(r.id)}.json" download>Metadata JSON</a></div></div><div class="detail-grid">${field("Coordinate & domain",esc(r.x.definition)+`<br>[${r.x.domain.join(", ")}] · `+esc(r.x.domain_basis))}${field("Cell match",esc(r.cell_link.evidence))}${field("Conditions",esc(experiment?experiment.protocol+(experiment.cycle_selected!==null&&experiment.cycle_selected!==undefined?" · Cycle "+experiment.cycle_selected:"")+" · "+r.temperature.description:r.temperature.description))}${field("Data representation",esc((r.representation.kind==="table"?r.representation.point_count+" retained table points ("+words(r.measurement)+")":"Expression; original measured points not supplied")))}${field("Sources",sourceLinks(r.source_ids))}${field("License",`<a href="${esc(r.license_url)}">${esc(r.license)}</a>`)}${field("Limits",'<ul>'+r.limitations.map(v=>`<li>${esc(v)}</li>`).join("")+"</ul>")}${field("Provenance",`<code>${esc(r.provenance.location)}</code><br>${esc(r.provenance.derivation)}`)}</div>${r.representation.kind==="expression"?`<div class="formula-text">${esc(r.representation.expression)}<br><small>x = θ; the 2001-point CSV is a numerical sample, not experimental data.</small></div>`:""}`;
}
$("source-cards").innerHTML=Object.entries(data.sources).map(([id,s])=>`<article class="source-card"><span class="tag">${esc(s.kind)} · ${esc(s.year)}</span><h3>${esc(s.title)}</h3><p>${esc(s.authors.join(", "))}</p><p>${esc(s.role)}</p><a href="${safeUrl(s.url)}" target="_blank" rel="noopener noreferrer">${esc(id)} ↗</a></article>`).join("");

const preferredCells=["a123-amp20m1hd-a","a123-high-power-pouch-9ah","bpx-lfp-18650-2ah-undisclosed","lg-m50"];
const cellOrder=[...preferredCells.filter(id=>data.cells[id]),...Object.keys(data.cells).filter(id=>!preferredCells.includes(id)).sort()];
const materialNames=[...new Set(data.records.map(r=>r.material))].sort((a,b)=>a.localeCompare(b));
$("material").innerHTML='<option value="">All materials</option>'+materialNames.map(m=>`<option value="${esc(m)}">${esc(m)}</option>`).join("");
$("material").value="LFP";
const cellFamilies=[...new Set(Object.values(data.cell_material_families))].sort();
$("cell-material").innerHTML='<option value="">All materials</option>'+cellFamilies.map(m=>`<option value="${esc(m)}">${esc(m)}</option>`).join("");
function renderCellChoices() {
  const prior=$("cell-select").value,family=$("cell-material").value;
  const ids=cellOrder.filter(id=>!family||data.cell_material_families[id]===family);
  $("cell-select").innerHTML=ids.map(id=>`<option value="${esc(id)}">${esc(data.cells[id].display_name)}</option>`).join("");
  if(ids.includes(prior))$("cell-select").value=prior;
}
$("cell-material").addEventListener("change",()=>{renderCellChoices();renderCell();});
renderCellChoices();
function renderCell() {
  const id=$("cell-select").value,cell=data.cells[id],parameters=data.parameters.filter(p=>p.cell_id===id),tests=data.full_cell_tests.filter(t=>t.cell_id===id);
  $("cell-title").textContent=cell.display_name;
  $("cell-context").textContent=cell.model_context||"DFN / SPM / SPMe reference parameterization";
  $("cell-match").innerHTML=`<b>Match: ${esc(words(cell.match_level))}.</b> ${esc(cell.match_evidence)}`;
  $("cell-note").innerHTML=esc(cell.note)+(cell.external_ocp_references?'<br>'+cell.external_ocp_references.map(r=>`<a href="${safeUrl(r.url)}" target="_blank" rel="noopener noreferrer">External pseudo-OCV workbook ↗</a> · ${esc(r.status)}`).join("<br>"):"");
  $("cell-coverage").innerHTML=Object.entries(cell.coverage).map(([k,v])=>`<div><b>${esc(k==="ocp"?"OCP":words(k))}</b><span>${esc(v)}</span></div>`).join("");
  $("cell-evidence").innerHTML=`<details open><summary>Evidence and missing items</summary><div class="evidence-scroll"><table class="parameter-table"><thead><tr><th>Component</th><th>Match / origin</th><th>Sources and gaps</th></tr></thead><tbody>${Object.entries(cell.evidence_matrix||{}).map(([key,row])=>`<tr><td>${esc(words(key))}<small class="condition">${row.record_ids.length} records</small></td><td><b>${esc(words(row.match_level))}</b><br>${esc(row.evidence)}</td><td>${sourceLinks(row.source_ids)}<br>${row.missing_items.map(esc).join("<br>")}</td></tr>`).join("")}</tbody></table></div><p class="compact">Cell gaps: ${(cell.missing_items||[]).map(esc).join(" · ")}</p></details>`;
  $("cell-downloads").innerHTML=`<a class="button" href="downloads/${id}-parameters.csv" download>Parameters CSV · all variants</a><a class="button" href="downloads/${id}-parameters.json" download>Cell package JSON</a><a class="button" href="downloads/${id}-bundle.zip" download>Offline bundle ZIP</a>`;
  $("parameter-category").innerHTML='<option value="">All parameters</option>'+[...new Set(parameters.map(p=>p.category))].sort().map(c=>`<option value="${esc(c)}">${esc(words(c))}</option>`).join("");
  $("parameter-variant").innerHTML='<option value="">All variants</option>'+[...new Set(parameters.map(p=>p.conditions?.parameterization_variant).filter(Boolean))].map(v=>`<option value="${esc(v)}">${esc(words(v))}</option>`).join("");
  if(parameters.some(p=>p.conditions?.parameterization_variant==="original_author_mpm")) $("parameter-variant").value="original_author_mpm";
  $("parameter-detail").innerHTML="";
  $("test-sample").innerHTML=tests.map(t=>`<option value="${esc(t.id)}">${esc(t.id)}</option>`).join("");
  $("test-sample").disabled=!tests.length;
  renderParameters();renderFullCell();
}
function renderParameters() {
  const rows=data.parameters.filter(p=>p.cell_id===$("cell-select").value&&(!$("parameter-variant").value||p.conditions?.parameterization_variant===$("parameter-variant").value)&&(!$("parameter-category").value||p.category===$("parameter-category").value));
  $("parameter-count").textContent=`${rows.length} records`;
  $("parameter-rows").innerHTML=rows.map(p=>`<tr><td><button data-parameter="${esc(p.id)}">${esc(p.name)}</button>${p.conditions?.cell_SOC_fraction!==undefined?`<small class="condition">Cell SOC ${(p.conditions.cell_SOC_fraction*100).toFixed(0)}%</small>`:""}</td><td>${p.representation.kind==="scalar"?esc(number(p.representation.value)):p.representation.kind==="table"?`Table · ${p.representation.point_count} nodes`:"Function"}</td><td>${esc(p.unit)}</td></tr>`).join("")||'<tr><td colspan="3">No parameter values imported for this family. See coverage gaps above.</td></tr>';
}
$("parameter-rows").addEventListener("click",event=>{const button=event.target.closest("[data-parameter]");if(!button)return;const p=data.parameters.find(p=>p.id===button.dataset.parameter);$("parameter-detail").innerHTML=`<b>${esc(p.name)}</b><p>${esc(p.definition||p.name)}</p><p>Origin: ${esc(p.provenance.origin_status)}</p><code>${esc(p.representation.kind==="expression"?p.representation.expression:p.provenance.location)}</code>${p.representation.kind==="expression"?`<p>Inputs: ${esc(JSON.stringify(p.representation.variables))}</p><p>Domain: ${esc(p.representation.domain)}</p>`:""}${p.representation.kind==="table"?`<p>${esc(p.representation.x.definition)}<br>Input: ${esc(p.representation.x.variable)} / ${esc(p.representation.x.unit)} · Domain: ${esc(p.representation.x.domain.join(" to "))}<br>Linear interpolation; extrapolation disabled.</p><a class="button" href="downloads/${esc(p.representation.path.split("/").pop())}" download>Native parameter table CSV</a>`:""}<p>Conditions: ${esc(JSON.stringify(p.conditions||{}))}</p><p>${sourceLinks(p.source_ids)}</p><p>${p.limitations.map(esc).join("<br>")}</p>`;});
function renderFullCell() {
  const test=data.full_cell_tests.find(t=>t.id===$("test-sample").value);
  if(!test){$("test-description").textContent="No matching raw full-cell experiments imported for this cell or parameter set.";$("fullcell-chart").innerHTML='<p class="empty">Full-cell test coverage gap</p>';$("test-downloads").innerHTML="";$("test-note").textContent="This package retains an explicit test coverage gap.";return;}
  $("test-description").textContent=test.protocol+". "+words(test.observation_kind)+". Voltage observations; no model prediction overlay.";
  $("fullcell-chart").innerHTML=plot(test.preview_segments,test.independent_variable?.label||"Time from trace / segment start / h","Full-cell voltage / V");
  const asset=data.assets[test.asset_id];
  $("test-downloads").innerHTML=(test.original_download_path?`<a class="button" href="downloads/${esc(test.original_download_path.split("/").pop())}" download>Original ${esc(test.original_format)}</a>`:test.path?`<a class="button" href="downloads/${esc(test.path.split("/").pop())}" download>Original CSV</a>`:`<a class="button" href="${safeUrl(asset.url)}" target="_blank" rel="noopener noreferrer">Original ${test.original_member?"ZIP":"MAT"} ↗</a>`)+`<a class="button" href="downloads/${esc(test.normalized_path.split("/").pop())}" download>Normalized CSV</a>`+(test.sidecars||[]).map(side=>`<a class="button" href="downloads/${esc(side.path.split("/").pop())}" download>Temperature rise CSV</a><a class="button" href="downloads/${esc(side.original_download_path.split("/").pop())}" download>Original rise TXT</a>`).join("");
  $("test-note").innerHTML=`${test.row_count.toLocaleString()} source rows retained. Display is decimated; valid voltage points only. Current: ${esc(words(test.basic_test.current_measurement))}. ${esc(test.temperature_definition||"Cell and ambient temperature retained from the instrument file.")}<br>${esc(test.missing_values?"Missing rows: "+Object.entries(test.missing_values).map(([key,value])=>(channelLabels[key]||words(key))+": "+value.toLocaleString()).join(" · "):"No missing values introduced.")}<br>${(test.source_issues||[]).map(esc).join("<br>")}<br>Missing items: ${(test.missing_items||[]).map(esc).join(" · ")||"See cell evidence matrix"}<br>Channels: ${Object.entries(test.channel_availability).map(([key,value])=>esc((channelLabels[key]||words(key))+": "+value.present_rows.toLocaleString()+"/"+value.total_rows.toLocaleString()+" rows")).join(" · ")}<br>${sourceLinks([test.source_id,...(test.scientific_source_ids||[])])}${test.source_id==="pybamm-data-1-0-2"?' · <a href="licenses/PyBaMM-data-BSD-3-Clause.txt">Data license notice</a>':""} · Original SHA-256: <code>${esc(asset.sha256)}</code>`;
}
$("cell-select").addEventListener("change",renderCell);
$("parameter-category").addEventListener("change",renderParameters);
$("parameter-variant").addEventListener("change",renderParameters);
$("test-sample").addEventListener("change",renderFullCell);
render();renderDetail();renderCell();

// External dataset filters inspect metadata only. No remote payload is fetched.
const datasets=data.external_datasets;
for(const [id,values] of [
  ["dataset-material",[...new Set(datasets.flatMap(r=>r.material_families))]],
  ["dataset-type",[...new Set(datasets.flatMap(r=>r.test_types))]],
  ["dataset-profile",[...new Set(datasets.flatMap(r=>r.profiles))]],
  ["dataset-aging",[...new Set(datasets.map(r=>r.aging_data.status))]],
]) {
  $(id).innerHTML+=[...values].sort().map(v=>`<option value="${esc(v)}">${esc(words(v))}</option>`).join("");
  $(id).addEventListener("change",renderDatasets);
}
function renderDatasetFileLocations(record) {
  const components=Object.entries(record.parameter_components).map(([name,item])=>`<p><b>${esc(words(name))}:</b> ${esc(words(item.match_level))} · ${esc(words(item.quantity_kind))}<br>${esc(item.evidence)}<br>Records: ${esc(item.record_ids.join(", ")||"None")}</p>`).join("");
  const coverage=Object.entries(record.test_coverage).map(([name,item])=>`<p><b>${esc(words(name))}:</b> ${esc(words(item.status))}<br>${esc(item.evidence)}</p>`).join("");
  const files=record.file_links.map(item=>`<li><code>${esc(item.source_path)}</code><br>${esc(item.cell_model||"Model unresolved")} · ${esc(item.source_sample_id||"Sample unresolved")}<br>${esc(item.test_types.join(", "))} ${esc(item.profiles.join(", "))} · ${esc(item.verification)} · content: ${esc(item.content_review)}<br>${esc(item.note)}<br><a href="${safeUrl(item.url)}" target="_blank" rel="noopener noreferrer">${item.kind==="archive_member"?"Open parent archive":"Open source file"} ↗</a></li>`).join("");
  return `<details><summary>OCP / diffusion / kinetics association</summary>${components}</details><details><summary>Multi-rate / US06 / EIS coverage</summary>${coverage}</details><details><summary>File locations (${record.file_links.length})</summary><p>${esc(record.inventory_scope)}</p><div class="dataset-file-list"><ul>${files}</ul></div></details>`;
}
function renderDatasets() {
  const material=$("dataset-material").value,type=$("dataset-type").value,profile=$("dataset-profile").value,aging=$("dataset-aging").value,query=$("dataset-query").value.trim().toLowerCase();
  const rows=datasets.filter(r=>(!material||r.material_families.includes(material))&&(!type||r.test_types.includes(type))&&(!profile||r.profiles.includes(profile))&&(!aging||r.aging_data.status===aging)&&(!query||JSON.stringify(r).toLowerCase().includes(query)));
  $("dataset-count").textContent=`${rows.length} / ${datasets.length} parameter-linked external sources. Counts describe source references.`;
  $("dataset-cards").innerHTML=rows.map(r=>`<article class="source-card"><span class="tag">${esc(r.material_families.join(" / "))} · external link</span><h3>${esc(r.title)}</h3><p>${esc(r.cell_identity)}</p><p><b>Electrode OCP anchor:</b> ${esc(words(r.ocp_anchor.kind))}<br>${esc(r.ocp_anchor.evidence)}<br>Half-cell temperature labels / °C: ${esc(r.ocp_anchor.half_cell_temperatures_C.length?r.ocp_anchor.half_cell_temperatures_C.join(", "):"Not independently verified")}</p><p><b>Tests:</b> ${esc(r.test_types.map(words).join(", "))}<br><b>Profiles:</b> ${esc(r.profiles.join(", ")||"No named drive profile verified")}</p><p>${esc(r.rate_summary)}<br>Source temperature labels / °C: ${esc(r.temperatures_C.length?r.temperatures_C.join(", "):"Not verified")}</p><p><b>Ageing data:</b> ${esc(words(r.aging_data.status))}${r.aging_data.kinds.length?" ("+esc(r.aging_data.kinds.join(", "))+")":""}<br>${esc(r.aging_data.evidence)} <a href="${safeUrl(r.aging_data.source_url)}" target="_blank" rel="noopener noreferrer">Coverage evidence ↗</a></p><p><b>Parameter match:</b> ${esc(words(r.parameter_link.match_level))}<br>${esc(r.parameter_link.evidence)}</p><p><b>License:</b> <a href="${safeUrl(r.license.evidence_url)}" target="_blank" rel="noopener noreferrer">${esc(r.license.identifier)}</a><br>${esc(r.license.note)}</p><details><summary>Source review and missing items</summary><p>Version: ${esc(r.source.version)} · Checked: ${esc(r.review.checked_on)} · ${esc(words(r.review.level))}</p><p>${esc(r.review.note)}</p><p>${esc(r.channels.note)}</p><p>Components without a native catalog join: ${esc(r.parameter_link.missing_components.join(", "))}</p><ul>${r.missing_items.map(item=>`<li>${esc(item)}</li>`).join("")}</ul></details><p><a class="button" href="${safeUrl(r.source.url)}" target="_blank" rel="noopener noreferrer">Open original dataset ↗</a></p>${renderDatasetFileLocations(r)}</article>`).join("")||'<p class="empty">No parameter-linked source matches these filters.</p>';
}
$("dataset-query").addEventListener("input",renderDatasets);
renderDatasets();
