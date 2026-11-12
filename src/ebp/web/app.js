"use strict";
(() => {
const $ = id => document.getElementById(id);
const data = window.EBP_DATA;
if (!data || !window.EBP_UI) {
  $("load-status").hidden = false;
  if (window.location.protocol === "file:" && window.location.pathname.endsWith("/src/ebp/web/index.html")) {
    $("generated-viewer").href = "../../../site/index.html";
    $("generated-viewer").hidden = false;
  }
  return;
}
const ui = window.EBP_UI;
const saved = new URLSearchParams(window.location.search);
const plotStates = new Map();
let nextPlot = 0;
const esc = value => String(value ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const safeUrl = value => /^https?:\/\//.test(value || "") ? esc(value) : "#";
const words = value => value.replaceAll("_", " ");
const measurementLabel = r => r.representation.kind==="expression" ? "Expression" : ({literature_table:"Published OCP table",pseudo_ocp:"Finite-current pseudo-OCP",model_ocp:"Modeled PD-ECM OCPn"}[r.measurement] || words(r.measurement));
const coordinateLabel = {stoichiometry:"Stoichiometry θ",normalized_branch_capacity:"Branch throughput",model_soc:"Author model SOC/DOL",source_reported_stoichiometry:"Source-reported electrode coordinate"};
const directionLabel = {lithiation:"Lithiation", delithiation:"Delithiation", unspecified:"Direction unspecified"};
const colors = ["#287b78","#c39042","#718db0","#ab7489","#5a9c91","#889a51","#bc7560","#8080ae"];
const recordById = new Map(data.records.map(record => [record.id, record]));
const selected = new Set((saved.get("compare") || "").split(",").filter(id => recordById.has(id)));
let detailId = recordById.has(saved.get("ocp")) ? saved.get("ocp") : "";
const sourceLinks = ids => ids.map(id => `<a href="${safeUrl(data.sources[id].url)}" target="_blank" rel="noopener noreferrer">${esc(id)} ↗</a>`).join(" · ");
const channelLabels={time_s:"Original time coordinate",voltage_V:"Voltage",current_charge_positive_A:"Measured current",cell_temperature_K:"Absolute cell temperature",ambient_temperature_K:"Ambient temperature"};
const number = value => Math.abs(value) !== 0 && (Math.abs(value) < .001 || Math.abs(value) >= 1e5) ? value.toExponential(5) : String(value);

$("total").textContent = data.records.length;
$("stats").innerHTML = [[data.records.filter(r=>r.representation.kind==="table").length,"Tabulated electrode curves / model potentials"],[data.records.filter(r=>r.representation.kind==="expression").length,"OCP expressions"],[data.parameters.length,"Model parameter records"],[data.full_cell_tests.length,"Full-cell experiment files"]].map(([n,label])=>`<div class="stat"><strong>${n}</strong><span>${esc(label)}</span></div>`).join("");

const ocpFilterIds = ["query", "material", "ocp-cell", "representation", "direction"];
const ocpSearchText = new Map(data.records.map(r => [r.id, [
  r.id, r.title, r.material, r.direction, r.reference,
  data.cells[r.cell_link.cell_id]?.display_name,
  ...r.source_ids.map(id => `${id} ${data.sources[id]?.title || ""}`),
].filter(Boolean).join(" ")]));
function filtered() {
  const material = $("material").value, cell = $("ocp-cell").value;
  const kind = $("representation").value, direction = $("direction").value, query = $("query").value;
  return data.records.filter(r => (!material || r.material === material)
    && (!cell || (cell === "material-only" ? !r.cell_link.cell_id : r.cell_link.cell_id === cell))
    && (!kind || r.representation.kind === kind) && (!direction || r.direction === direction)
    && ui.matchesSearch(ocpSearchText.get(r.id), query));
}
function markOcpDetail() {
  for (const button of $("records").querySelectorAll("[data-detail]")) {
    const active = button.dataset.detail === detailId;
    button.setAttribute("aria-pressed", String(active));
    button.closest(".record").classList.toggle("active-record", active);
  }
}
function renderOcpResults() {
  const rows = filtered();
  const next = rows.some(r => r.id === detailId) ? detailId : rows[0]?.id || "";
  $("result-count").textContent = `${rows.length} / ${data.records.length}`;
  $("records").innerHTML = rows.map(r => `<article class="record ${selected.has(r.id) ? "selected" : ""}"><div class="record-head"><button class="record-title" data-detail="${esc(r.id)}" aria-controls="detail">${esc(r.title)}</button><label class="compare-choice"><input aria-label="Compare ${esc(r.title)}" type="checkbox" data-compare="${esc(r.id)}" ${selected.has(r.id) ? "checked" : ""}> Compare</label></div><div class="record-tags"><span class="tag ${r.representation.kind === "expression" ? "formula" : ""}">${esc(measurementLabel(r))}</span><span class="tag">${esc(directionLabel[r.direction])}</span><span class="tag">${esc(coordinateLabel[r.x.kind] || words(r.x.kind))}</span></div><small>${esc(r.id)}</small></article>`).join("") || '<p class="empty">No curves match these filters. Try clearing a filter or broadening your search.</p>';
  if (next !== detailId || !$("detail").hasChildNodes()) {
    detailId = next;
    renderDetail();
  }
  markOcpDetail();
}
function focusOnNarrowScreen(element) {
  if (window.matchMedia("(max-width: 800px)").matches) element.scrollIntoView({block: "nearest"});
}
$("records").addEventListener("click", event => {
  const button = event.target.closest("[data-detail]");
  if (!button) return;
  detailId = button.dataset.detail;
  renderDetail();
  markOcpDetail();
  focusOnNarrowScreen($("detail"));
});
$("records").addEventListener("change", event => {
  const input = event.target;
  if (!input.dataset.compare) return;
  if (input.checked) selected.add(input.dataset.compare);
  else selected.delete(input.dataset.compare);
  refreshComparison();
});
for (const id of ocpFilterIds) $(id).addEventListener(id === "query" ? "input" : "change", renderOcpResults);
$("reset").addEventListener("click", () => {
  for (const id of ocpFilterIds) $(id).value = "";
  renderOcpResults();
});
$("clear-selection").addEventListener("click", () => {
  selected.clear();
  refreshComparison();
  $("query").focus({preventScroll: true});
});
$("selected-curves").addEventListener("click", event => {
  const button = event.target.closest("[data-remove-curve]");
  if (!button) return;
  selected.delete(button.dataset.removeCurve);
  refreshComparison();
  ($("selected-curves").querySelector("button") || $("query")).focus({preventScroll: true});
});

// Each plot uses its actual data domain; BPX operating bounds are not 0..1.
function forgetPlots(container) {
  for (const svg of container.querySelectorAll("[data-plot]")) plotStates.delete(svg.dataset.plot);
}
function plot(series, xLabel, yLabel) {
  const all=series.flatMap(s=>s.points);
  if(!all.length)return '<p class="empty">No valid observations to plot.</p>';
  const xmin=Math.min(...all.map(p=>p[0])),xmax=Math.max(...all.map(p=>p[0]));
  const lo=Math.min(...all.map(p=>p[1])),hi=Math.max(...all.map(p=>p[1])),pad=Math.max((hi-lo)*.08,.025),ymin=lo-pad,ymax=hi+pad;
  const X=x=>48+(x-xmin)/(xmax-xmin||1)*356,Y=y=>190-(y-ymin)/(ymax-ymin)*156;
  const id=String(++nextPlot);
  plotStates.set(id,{series,xmin,xmax,X,Y,xLabel,yLabel,focusX:null});
  let svg=`<svg class="interactive-plot" data-plot="${id}" viewBox="0 0 430 238" tabindex="0" role="img" aria-label="${esc(yLabel+" versus "+xLabel)}. Use left and right arrows to inspect preview points." aria-describedby="plot-hint-${id}"><text x="48" y="20">${esc(yLabel)}</text>`;
  for(let i=0;i<=4;i++){const x=xmin+(xmax-xmin)*i/4,y=ymin+(ymax-ymin)*i/4;svg+=`<line class="grid" x1="48" x2="404" y1="${Y(y)}" y2="${Y(y)}"/><text x="40" y="${Y(y)+3}" text-anchor="end">${y.toFixed(2)}</text><text x="${X(x)}" y="209" text-anchor="middle">${x.toFixed(2)}</text>`;}
  svg+='<line class="axis" x1="48" x2="404" y1="190" y2="190"/>';
  svg+=series.map((s,i)=>`<path class="curve" stroke="${colors[i%colors.length]}" d="${s.points.map((p,j)=>`${j?"L":"M"}${X(p[0]).toFixed(2)},${Y(p[1]).toFixed(2)}`).join(" ")}"><title>${esc(s.label)}</title></path>`).join("");
  svg+='<g class="plot-cursor" hidden><line class="plot-crosshair" y1="34" y2="190"/><g class="plot-markers"></g></g>';
  svg+=`<text x="225" y="232" text-anchor="middle">${esc(xLabel)}</text></svg>`;
  return '<div class="plot-inspector">'+svg+'<div class="legend">'+series.map((s,i)=>`<span><i style="background:${colors[i%colors.length]}"></i>${esc(s.label)}</span>`).join("")+`</div><p id="plot-hint-${id}" class="axis-note">Move the pointer or tap the chart. Keyboard: left/right arrows, Home, End; Escape clears. Readings are sampled preview points; downloads retain native data.</p><div class="plot-readout" aria-live="off">Inspect a preview point to see its coordinates.</div></div>`;
}
function inspectPlot(svg,x,announce=false) {
  const state=plotStates.get(svg.dataset.plot);
  if(!state)return;
  x=Math.max(state.xmin,Math.min(state.xmax,x));state.focusX=x;
  const cursor=svg.querySelector(".plot-cursor");cursor.removeAttribute("hidden");
  const line=cursor.querySelector("line");line.setAttribute("x1",state.X(x));line.setAttribute("x2",state.X(x));
  const points=state.series.map(s=>ui.nearestPreviewPoint(s.points,x));
  cursor.querySelector(".plot-markers").innerHTML=points.map((p,i)=>p?`<circle cx="${state.X(p[0])}" cy="${state.Y(p[1])}" r="4" fill="${colors[i%colors.length]}"/>`:"").join("");
  const readout=svg.parentElement.querySelector(".plot-readout");readout.setAttribute("aria-live",announce?"polite":"off");
  readout.innerHTML=state.series.map((s,i)=>`<span><b>${esc(s.label)}</b>: ${points[i]?`${esc(state.xLabel)} = ${points[i][0].toPrecision(6)}; ${esc(state.yLabel)} = ${points[i][1].toPrecision(6)}`:"outside this curve's domain"}</span>`).join("");
}
document.addEventListener("pointermove",event=>{
  const svg=event.target.closest("[data-plot]");if(!svg)return;
  const state=plotStates.get(svg.dataset.plot),box=svg.getBoundingClientRect();
  if(state&&box.width)inspectPlot(svg,state.xmin+((event.clientX-box.left)*430/box.width-48)/356*(state.xmax-state.xmin));
});
document.addEventListener("pointerdown",event=>{
  const svg=event.target.closest("[data-plot]");if(!svg)return;
  const state=plotStates.get(svg.dataset.plot),box=svg.getBoundingClientRect();
  if(state&&box.width)inspectPlot(svg,state.xmin+((event.clientX-box.left)*430/box.width-48)/356*(state.xmax-state.xmin));
});
document.addEventListener("keydown",event=>{
  const svg=event.target.closest("[data-plot]");if(!svg||!["ArrowLeft","ArrowRight","Home","End","Escape"].includes(event.key))return;
  const state=plotStates.get(svg.dataset.plot);if(!state)return;event.preventDefault();
  if(event.key==="Escape"){svg.querySelector(".plot-cursor").setAttribute("hidden","");svg.parentElement.querySelector(".plot-readout").textContent="Inspect a preview point to see its coordinates.";state.focusX=null;return;}
  const x=event.key==="Home"?state.xmin:event.key==="End"?state.xmax:(state.focusX??state.xmin)+(event.key==="ArrowRight"?1:-1)*(state.xmax-state.xmin)/200;
  inspectPlot(svg,x,true);
});
function refreshComparison() {
  for (const input of $("records").querySelectorAll("[data-compare]")) {
    input.checked = selected.has(input.dataset.compare);
    input.closest(".record").classList.toggle("selected", input.checked);
  }
  forgetPlots($("charts"));
  const rows = [...selected].map(id => recordById.get(id)).filter(Boolean);
  $("selected-count").textContent = `${rows.length} selected`;
  $("clear-selection").disabled = !rows.length;
  $("selected-curves").innerHTML = rows.map(r => `<button class="compare-chip" data-remove-curve="${esc(r.id)}" aria-label="Remove ${esc(r.title)} from comparison" title="${esc(r.title)}">${esc(r.id)} <span aria-hidden="true">×</span></button>`).join("");
  if (!rows.length) {
    $("charts").innerHTML = '<p class="empty">Tick Compare beside a curve to plot it here.</p>';
    return;
  }
  const groups=new Map();
  for(const r of rows){const key=r.x.kind+":"+r.direction+":"+r.material+":"+r.reference+":"+(r.measurement==="model_ocp"?r.id:"observations");if(!groups.has(key))groups.set(key,[]);groups.get(key).push(r);}
  $("charts").innerHTML=[...groups.values()].map(group=>{const first=group[0],stoich=first.x.kind==="stoichiometry";return `<section class="plot"><h3>${esc(first.material)} / ${esc(directionLabel[first.direction])}</h3>${plot(group.map(r=>({label:r.id,points:r.display_points})),coordinateLabel[first.x.kind],first.reference==="Li/Li+"?"Potential / V vs Li/Li⁺":"Half-cell voltage / V (reference unresolved)")}<div class="axis-note">${first.x.kind==="source_reported_stoichiometry"?"Source-reported coordinate; absolute lithium-fraction calibration requires explicit evidence. Native charging/discharging labels do not establish lithiation direction.":first.x.kind==="model_soc"?"Parameterized PD-ECM OCPn on its source model coordinate; not raw measured OCP or verified lithium fraction.":stoich?"Each fit is plotted only inside its catalog domain. Domain limits and validity are documented per record.":"0 → 1 follows the record's defined branch coordinate. Branch endpoints do not establish equal lithium content or chronological acquisition order."}</div></section>`;}).join("");
}
const ocpYLabel = r => r.reference === "Li/Li+" ? "Potential / V vs Li/Li⁺" : "Half-cell voltage / V (reference unresolved)";
function recordDetails(r, showCellLink = false) {
  const experiment = data.experiments[r.experiment_id];
  const field = (label, value) => `<div class="field"><strong>${esc(label)}</strong>${value}</div>`;
  const isTable = r.representation.kind === "table";
  const jump = showCellLink && r.cell_link.cell_id
    ? `<button class="text-button" data-open-cell="${esc(r.cell_link.cell_id)}">Open cell package →</button>` : "";
  return `<h3>${esc(r.title)}</h3><p class="muted compact">${esc(measurementLabel(r))} · ${esc(directionLabel[r.direction])}</p>
    <div class="actions"><a class="button" href="downloads/${esc(r.id)}.csv" download>${isTable ? "Retained points CSV" : "Sampled formula CSV"}</a><a class="button" href="downloads/${esc(r.id)}.json" download>Metadata JSON</a>${jump}</div>
    <details class="record-evidence"><summary>Coordinate, source and limitations</summary><div class="detail-grid">
    ${field("Coordinate & domain", esc(r.x.definition) + `<br>[${esc(r.x.domain.join(", "))}] · ${esc(r.x.domain_basis)}`)}
    ${field("Cell match", esc(r.cell_link.evidence))}
    ${field("Conditions", esc(experiment ? experiment.protocol + (experiment.cycle_selected != null ? " · Cycle " + experiment.cycle_selected : "") + " · " + r.temperature.description : r.temperature.description))}
    ${field("Data representation", esc(isTable ? `${r.representation.point_count} retained table points (${words(r.measurement)})` : "Expression; original measured points not supplied"))}
    ${field("Sources", sourceLinks(r.source_ids))}
    ${field("License", `<a href="${esc(r.license_url)}">${esc(r.license)}</a>`)}
    ${field("Limits", '<ul>' + r.limitations.map(v => `<li>${esc(v)}</li>`).join("") + "</ul>")}
    ${field("Provenance", `<code>${esc(r.provenance.location)}</code><br>${esc(r.provenance.derivation)}`)}</div>
    ${isTable ? "" : `<div class="formula-text">${esc(r.representation.expression)}<br><small>x follows the coordinate definition above. The 2001-point CSV is a numerical sample.</small></div>`}</details>`;
}
function renderDetail() {
  const record = recordById.get(detailId);
  $("detail").hidden = !record;
  $("detail").innerHTML = record ? recordDetails(record, true) : "";
}
$("source-cards").innerHTML=Object.entries(data.sources).map(([id,s])=>`<article class="source-card"><span class="tag">${esc(s.kind)} · ${esc(s.year)}</span><h3>${esc(s.title)}</h3><p>${esc(s.authors.join(", "))}</p><p>${esc(s.role)}</p><a href="${safeUrl(s.url)}" target="_blank" rel="noopener noreferrer">${esc(id)} ↗</a></article>`).join("");

const cellTabs = ["parameters", "ocp", "experiments", "evidence"];
const cells = Object.entries(data.cells).map(([id, value]) => ({
  id, name: value.display_name, family: data.cell_material_families[id],
})).sort((a, b) => a.name.localeCompare(b.name));
const cellPackages = new Map(cells.map(({id}) => [id, {
  cell: data.cells[id],
  parameters: data.parameters.filter(p => p.cell_id === id),
  curves: data.records.filter(r => r.cell_link.cell_id === id),
  traces: data.full_cell_tests.filter(t => t.cell_id === id),
  sources: ui.linkedSources(data.external_datasets, id),
}]));
const parameterById = new Map(data.parameters.map(p => [p.id, p]));
const savedCell = saved.get("cell");
let activeCell = cellPackages.has(savedCell) ? savedCell : cellPackages.has("lg-m50") ? "lg-m50" : cells[0]?.id;
let activeTab = cellTabs.includes(saved.get("cell_tab")) ? saved.get("cell_tab") : "parameters";
let activeParameter = "";
const cellViews = new Map();
if (activeCell && activeCell === savedCell) cellViews.set(activeCell, {
  category: saved.get("category"), variant: saved.get("variant"), query: saved.get("pq") || "",
  parameter: saved.get("parameter") || "", curve: saved.get("cell_ocp"), sample: saved.get("sample"),
});
const optionsMarkup = (values, label) => values.map(value => `<option value="${esc(value)}">${esc(label(value))}</option>`).join("");
function restoreSelect(id, value) {
  if (value != null && [...$(id).options].some(option => option.value === value)) $(id).value = value;
}
const materialNames = [...new Set(data.records.map(r => r.material))].sort((a, b) => a.localeCompare(b));
$("material").innerHTML += optionsMarkup(materialNames, x => x);
$("ocp-cell").innerHTML += '<option value="material-only">Material-only studies</option>'
  + optionsMarkup(cells.filter(x => cellPackages.get(x.id).curves.length).map(x => x.id), id => data.cells[id].display_name);
$("cell-material").innerHTML += optionsMarkup([...new Set(cells.map(x => x.family))].sort(), x => x);
function renderCellChoices() {
  const matches = ui.filterCells(cells, {family: $("cell-material").value, query: $("cell-query").value});
  const available = matches.some(x => x.id === activeCell);
  $("cell-select").innerHTML = `<option value="" disabled>${matches.length ? "Choose a matching cell or study" : "No matching cells"}</option>`
    + matches.map(x => `<option value="${esc(x.id)}">${esc(x.name)}</option>`).join("");
  $("cell-select").value = available ? activeCell : "";
  $("cell-select").disabled = !matches.length;
  $("cell-content").hidden = !available;
  $("cell-choice-status").textContent = !matches.length ? "No matching cells or studies. Clear a filter or broaden your search."
    : matches.length === 1 && !available ? "1 match · press Enter or choose the cell to open it"
    : `${matches.length} ${matches.length === 1 ? "match" : "matches"}${available ? "" : " · choose a cell to open its package"}`;
}
function showCellTab(tab, focus = false) {
  if (!cellTabs.includes(tab)) return;
  activeTab = tab;
  for (const name of cellTabs) {
    const button = $("cell-tab-" + name), on = name === tab;
    button.setAttribute("aria-selected", String(on));
    button.tabIndex = on ? 0 : -1;
    $("cell-panel-" + name).hidden = !on;
  }
  if (focus) $("cell-tab-" + tab).focus({preventScroll: true});
}
$("cell-tabs").addEventListener("click", event => {
  const tab = event.target.closest("[data-cell-tab]");
  if (tab) showCellTab(tab.dataset.cellTab);
});
$("cell-tabs").addEventListener("keydown", event => {
  const tab = event.target.closest("[data-cell-tab]");
  const next = tab && ui.nextTab(cellTabs, tab.dataset.cellTab, event.key);
  if (!next) return;
  event.preventDefault();
  showCellTab(next, true);
});
function currentCellView() {
  return {
    category: $("parameter-category").value, variant: $("parameter-variant").value,
    query: $("parameter-query").value, parameter: activeParameter,
    curve: $("cell-ocp-select").value, sample: $("test-sample").value,
  };
}
function openCell(id) {
  if (!cellPackages.has(id) || id === activeCell) return;
  if (activeCell) cellViews.set(activeCell, currentCellView());
  activeCell = id;
  renderCell();
  renderCellChoices();
}
$("cell-query").addEventListener("input", renderCellChoices);
$("cell-query").addEventListener("keydown", event => {
  if (event.key !== "Enter" || event.isComposing) return;
  const choices = [...$("cell-select").options].filter(option => !option.disabled);
  if (!choices.length) return;
  event.preventDefault();
  if (choices.length === 1) {
    openCell(choices[0].value);
    showCellTab(activeTab, true);
  } else {
    $("cell-select").focus();
  }
});
$("cell-material").addEventListener("change", renderCellChoices);
$("cell-select").addEventListener("change", event => openCell(event.target.value));
function defaultVariant(parameters) {
  return parameters.some(p => p.conditions?.parameterization_variant === "original_author_mpm") ? "original_author_mpm" : "";
}
function renderCell() {
  const {cell, parameters, curves, traces, sources} = cellPackages.get(activeCell);
  const view = cellViews.get(activeCell) || {};
  $("cell-title").textContent = cell.display_name;
  $("cell-context").textContent = cell.model_context || "DFN / SPM / SPMe reference parameterization";
  $("tab-count-parameters").textContent = parameters.length;
  $("tab-count-ocp").textContent = curves.length;
  $("tab-count-experiments").textContent = traces.length + sources.length;
  $("cell-tab-experiments").setAttribute("aria-label", `Experiments: ${traces.length} stored trace files, ${sources.length} external sources`);
  $("cell-match").innerHTML = `<b>Match: ${esc(words(cell.match_level))}.</b> ${esc(cell.match_evidence)}`;
  $("cell-note").innerHTML = esc(cell.note) + (cell.external_ocp_references ? '<br>' + cell.external_ocp_references.map(r => `<a href="${safeUrl(r.url)}" target="_blank" rel="noopener noreferrer">External pseudo-OCV workbook ↗</a> · ${esc(r.status)}`).join("<br>") : "");
  $("cell-coverage").innerHTML = Object.entries(cell.coverage).map(([k, v]) => `<div><b>${esc(k === "ocp" ? "OCP" : words(k))}</b><span>${esc(v)}</span></div>`).join("");
  $("cell-evidence").innerHTML = `<h4>Evidence and missing items</h4><div class="evidence-scroll"><table class="parameter-table"><thead><tr><th scope="col">Component</th><th scope="col">Match / origin</th><th scope="col">Sources and gaps</th></tr></thead><tbody>${Object.entries(cell.evidence_matrix || {}).map(([key, row]) => `<tr><td>${esc(words(key))}<small class="condition">${row.record_ids.length} records</small></td><td><b>${esc(words(row.match_level))}</b><br>${esc(row.evidence)}</td><td>${sourceLinks(row.source_ids)}<br>${row.missing_items.map(esc).join("<br>")}</td></tr>`).join("")}</tbody></table></div><p class="compact">Cell gaps: ${(cell.missing_items || []).map(esc).join(" · ")}</p>`;
  $("cell-downloads").innerHTML = (parameters.length ? `<a class="button" href="downloads/${esc(activeCell)}-parameters.csv" download>All parameters CSV</a>` : "") + `<a class="button" href="downloads/${esc(activeCell)}-parameters.json" download>Cell package JSON</a><a class="button" href="downloads/${esc(activeCell)}-bundle.zip" download>Offline bundle ZIP</a>`;
  $("cell-downloads").parentElement.open = false;
  const categories = [...new Set(parameters.map(p => p.category))].sort();
  const variants = [...new Set(parameters.map(p => p.conditions?.parameterization_variant).filter(Boolean))];
  $("parameter-category").innerHTML = '<option value="">All categories</option>' + optionsMarkup(categories, words);
  $("parameter-variant").innerHTML = '<option value="">All variants</option>' + optionsMarkup(variants, words);
  $("parameter-category").disabled = !categories.length;
  $("parameter-variant").disabled = !variants.length;
  $("parameter-query").disabled = !parameters.length;
  $("parameter-variant").value = defaultVariant(parameters);
  restoreSelect("parameter-category", view.category);
  restoreSelect("parameter-variant", view.variant);
  $("parameter-query").value = view.query || "";
  activeParameter = view.parameter || "";
  $("cell-ocp-select").innerHTML = optionsMarkup(curves.map(r => r.id), id => {
    const r = recordById.get(id);
    return `${r.material} · ${directionLabel[r.direction]} · ${r.title}`;
  });
  restoreSelect("cell-ocp-select", view.curve);
  $("test-sample").innerHTML = traces.map(t => `<option value="${esc(t.id)}">${esc(t.sample_id || t.id)} · ${esc(t.protocol.split(";")[0])}</option>`).join("");
  restoreSelect("test-sample", view.sample);
  $("cell-test-references").innerHTML = `<h4>External test references · ${sources.length}</h4>` + (sources.length
    ? sources.map(source => `<details class="linked-experiment"><summary>${esc(source.title)} <span class="tag">${esc(words(source.parameter_link.match_level))}</span></summary><p>${esc(source.parameter_link.evidence)}</p><p><b>Tests:</b> ${esc(source.test_types.map(words).join(", "))} · <b>Temperature labels:</b> ${esc(source.temperatures_C.length ? source.temperatures_C.join(", ") + " °C" : "Not verified")}</p><div class="actions"><a class="button" href="${safeUrl(source.source.url)}" target="_blank" rel="noopener noreferrer">Open original dataset ↗</a><a class="button" href="${safeUrl(source.license.evidence_url)}" target="_blank" rel="noopener noreferrer">${esc(source.license.identifier)} ↗</a></div>${renderDatasetFileLocations(source)}</details>`).join("")
    : '<p class="muted compact">No reviewed external test source is linked to this package.</p>');
  renderParameters();
  renderCellOcp();
  renderFullCell();
  showCellTab(activeTab);
}
function renderCellOcp() {
  forgetPlots($("cell-ocp-chart"));
  const record = recordById.get($("cell-ocp-select").value);
  $("cell-ocp-control").hidden = !record;
  $("cell-ocp-chart").innerHTML = record
    ? plot([{label: record.id, points: record.display_points}], coordinateLabel[record.x.kind] || words(record.x.kind), ocpYLabel(record))
    : '<p class="empty">No electrode OCP is stored for this package. See Evidence for source and reuse gaps.</p>';
  $("cell-ocp-detail").innerHTML = record ? recordDetails(record) : "";
}
$("cell-ocp-select").addEventListener("change", renderCellOcp);
$("compare-cell-ocp").addEventListener("click", () => {
  const r = recordById.get($("cell-ocp-select").value);
  if (!r) return;
  selected.add(r.id);
  for (const id of ocpFilterIds) $(id).value = "";
  $("ocp-cell").value = r.cell_link.cell_id;
  detailId = r.id;
  renderOcpResults();
  renderDetail();
  refreshComparison();
  goTo("library");
});
function visibleParameters() {
  return ui.filterParameters(cellPackages.get(activeCell).parameters, {
    cell: activeCell, variant: $("parameter-variant").value,
    category: $("parameter-category").value, query: $("parameter-query").value,
  });
}
function renderParameterDetail(p) {
  const target = $("parameter-detail");
  if (target.dataset.parameter === (p?.id || "")) return;
  target.dataset.parameter = p?.id || "";
  if (!p) {
    target.innerHTML = '<h4>Parameter details</h4><p>Choose a parameter to see its definition, conditions, sources and limitations.</p>';
    return;
  }
  const rep = p.representation;
  const conditions = Object.entries(p.conditions || {}).map(([key, value]) => `<dt>${esc(words(key))}</dt><dd>${esc(value && typeof value === "object" ? JSON.stringify(value) : value)}</dd>`).join("");
  target.innerHTML = `<h4>${esc(p.name)}</h4><p>${esc(p.definition || p.name)}</p><p><b>Origin:</b> ${esc(words(p.provenance.origin_status))} · <b>License:</b> ${esc(p.license)}</p><code>${esc(rep.kind === "expression" ? rep.expression : p.provenance.location)}</code>
    ${rep.kind === "expression" ? `<p><b>Inputs:</b> ${esc(JSON.stringify(rep.variables))}<br><b>Domain:</b> ${esc(rep.domain)}</p>` : ""}
    ${rep.kind === "table" ? `<p>${esc(rep.x.definition)}<br>Input: ${esc(rep.x.variable)} / ${esc(rep.x.unit)} · Domain: ${esc(rep.x.domain.join(" to "))}<br>Linear interpolation; extrapolation disabled.</p><a class="button" href="downloads/${esc(rep.path.split("/").pop())}" download>Native parameter table CSV</a>` : ""}
    ${conditions ? `<dl>${conditions}</dl>` : ""}<p>${sourceLinks(p.source_ids)}</p><p>${p.limitations.map(esc).join("<br>")}</p>`;
}
function markParameter() {
  for (const button of $("parameter-rows").querySelectorAll("[data-parameter]")) {
    const active = button.dataset.parameter === activeParameter;
    button.setAttribute("aria-pressed", String(active));
    button.closest("tr").classList.toggle("active-parameter", active);
  }
}
function renderParameters() {
  const rows = visibleParameters(), {parameters} = cellPackages.get(activeCell);
  if (!rows.some(p => p.id === activeParameter)) activeParameter = "";
  $("export-parameters").disabled = !rows.length;
  $("export-parameters").textContent = rows.length ? `Export ${rows.length} matching ${rows.length === 1 ? "row" : "rows"} (CSV)` : "Export matching CSV";
  $("reset-parameters").disabled = !parameters.length || (!$("parameter-query").value && !$("parameter-category").value && $("parameter-variant").value === defaultVariant(parameters));
  $("parameter-count").textContent = `${rows.length} of ${parameters.length} parameter rows`;
  $("parameter-rows").innerHTML = rows.map(p => `<tr><td><button data-parameter="${esc(p.id)}" aria-controls="parameter-detail">${esc(p.name)}</button>${p.conditions?.cell_SOC_fraction !== undefined ? `<small class="condition">Cell SOC ${(p.conditions.cell_SOC_fraction * 100).toFixed(0)}%</small>` : ""}</td><td>${p.representation.kind === "scalar" ? esc(number(p.representation.value)) : p.representation.kind === "table" ? `Table · ${p.representation.point_count} nodes` : "Function"}</td><td>${esc(p.unit)}</td></tr>`).join("")
    || `<tr><td colspan="3">${parameters.length ? "No rows match these filters. Try Reset filters." : "No model parameters are stored. See the OCP or Evidence tab."}</td></tr>`;
  markParameter();
  renderParameterDetail(parameterById.get(activeParameter));
}
$("parameter-rows").addEventListener("click", event => {
  const button = event.target.closest("[data-parameter]");
  if (!button) return;
  activeParameter = button.dataset.parameter;
  markParameter();
  renderParameterDetail(parameterById.get(activeParameter));
  focusOnNarrowScreen($("parameter-detail"));
});
for (const id of ["parameter-category", "parameter-variant", "parameter-query"]) {
  $(id).addEventListener(id === "parameter-query" ? "input" : "change", renderParameters);
}
$("reset-parameters").addEventListener("click", () => {
  $("parameter-query").value = "";
  $("parameter-category").value = "";
  $("parameter-variant").value = defaultVariant(cellPackages.get(activeCell).parameters);
  renderParameters();
  $("parameter-query").focus({preventScroll: true});
});
$("export-parameters").addEventListener("click", () => {
  const rows = visibleParameters();
  if (!rows.length) return;
  const url = URL.createObjectURL(new Blob([ui.parameterCSV(rows)], {type: "text/csv;charset=utf-8"}));
  const a = document.createElement("a");
  a.href = url;
  a.download = activeCell + "-filtered-parameters.csv";
  document.body.append(a);
  a.click();
  a.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
});

function renderFullCell() {
  forgetPlots($("fullcell-chart"));
  const test=data.full_cell_tests.find(t=>t.id===$("test-sample").value);
  $("test-toolbar").hidden = !test;
  $("test-note-panel").hidden = !test;
  $("test-note-panel").open = false;
  if (!test) {
    $("test-description").textContent = "No full-cell trace is stored for this package. Any reviewed external sources are listed separately.";
    $("fullcell-chart").replaceChildren();
    $("test-downloads").replaceChildren();
    $("test-note").textContent = "";
    return;
  }
  $("test-description").textContent=test.protocol+". "+words(test.observation_kind)+". Voltage observations; no model prediction overlay.";
  $("fullcell-chart").innerHTML=plot(test.preview_segments,test.independent_variable?.label||"Time from trace / segment start / h","Full-cell voltage / V");
  const asset=data.assets[test.asset_id];
  $("test-downloads").innerHTML=(test.original_download_path?`<a class="button" href="downloads/${esc(test.original_download_path.split("/").pop())}" download>Original ${esc(test.original_format)}</a>`:test.path?`<a class="button" href="downloads/${esc(test.path.split("/").pop())}" download>Original CSV</a>`:`<a class="button" href="${safeUrl(asset.url)}" target="_blank" rel="noopener noreferrer">Original ${test.original_member?"ZIP":"MAT"} ↗</a>`)+`<a class="button" href="downloads/${esc(test.normalized_path.split("/").pop())}" download>Normalized CSV</a>`+(test.sidecars||[]).map(side=>`<a class="button" href="downloads/${esc(side.path.split("/").pop())}" download>Temperature rise CSV</a><a class="button" href="downloads/${esc(side.original_download_path.split("/").pop())}" download>Original rise TXT</a>`).join("");
  $("test-note").innerHTML=`${test.row_count.toLocaleString()} source rows retained. Display is decimated; valid voltage points only. Current: ${esc(words(test.basic_test.current_measurement))}. ${esc(test.temperature_definition||"Cell and ambient temperature retained from the instrument file.")}<br>${esc(test.missing_values?"Missing rows: "+Object.entries(test.missing_values).map(([key,value])=>(channelLabels[key]||words(key))+": "+value.toLocaleString()).join(" · "):"No missing values introduced.")}<br>${(test.source_issues||[]).map(esc).join("<br>")}<br>Missing items: ${(test.missing_items||[]).map(esc).join(" · ")||"See cell evidence matrix"}<br>Channels: ${Object.entries(test.channel_availability).map(([key,value])=>esc((channelLabels[key]||words(key))+": "+value.present_rows.toLocaleString()+"/"+value.total_rows.toLocaleString()+" rows")).join(" · ")}<br>${sourceLinks([test.source_id,...(test.scientific_source_ids||[])])}${test.source_id==="pybamm-data-1-0-2"?' · <a href="licenses/PyBaMM-data-BSD-3-Clause.txt">Data license notice</a>':""} · Original SHA-256: <code>${esc(asset.sha256)}</code>`;
}
$("test-sample").addEventListener("change", renderFullCell);

// External dataset filters inspect metadata only. No remote payload is fetched.
const datasets = data.external_datasets;
const datasetById = new Map(datasets.map(r => [r.id, r]));
const datasetSearchText = new Map(datasets.map(r => [r.id, JSON.stringify(r)]));
const datasetFilterIds = ["dataset-cell", "dataset-material", "dataset-type", "dataset-profile", "dataset-aging", "dataset-query"];
$("dataset-cell").innerHTML += optionsMarkup(cells.filter(x => cellPackages.get(x.id).sources.length).map(x => x.id), id => data.cells[id].display_name);
for (const [id, values] of [
  ["dataset-material", datasets.flatMap(r => r.material_families)],
  ["dataset-type", datasets.flatMap(r => r.test_types)],
  ["dataset-profile", datasets.flatMap(r => r.profiles)],
  ["dataset-aging", datasets.map(r => r.aging_data.status)],
]) {
  $(id).innerHTML += optionsMarkup([...new Set(values)].sort(), words);
}
function renderDatasetFileLocations(record) {
  const components = Object.entries(record.parameter_components).map(([name, item]) => `<p><b>${esc(words(name))}:</b> ${esc(words(item.match_level))} · ${esc(words(item.quantity_kind))}<br>${esc(item.evidence)}<br>Records: ${esc(item.record_ids.join(", ") || "None")}</p>`).join("");
  const coverage = Object.entries(record.test_coverage).map(([name, item]) => `<p><b>${esc(words(name))}:</b> ${esc(words(item.status))}<br>${esc(item.evidence)}</p>`).join("");
  return `<details><summary>OCP / diffusion / kinetics association</summary>${components}</details><details><summary>Multi-rate / US06 / EIS coverage</summary>${coverage}</details><details data-source-files="${esc(record.id)}"><summary>File locations (${record.file_links.length})</summary><p>${esc(record.inventory_scope)}</p><div class="dataset-file-list"></div></details>`;
}
document.addEventListener("toggle", event => {
  const details = event.target;
  if (!details.matches("[data-source-files]") || !details.open || details.dataset.loaded) return;
  const record = datasetById.get(details.dataset.sourceFiles);
  if (!record) return;
  const files = record.file_links.map(item => `<li><code>${esc(item.source_path)}</code><br>${esc(item.cell_model || "Model unresolved")} · ${esc(item.source_sample_id || "Sample unresolved")}<br>${esc(item.test_types.join(", "))} ${esc(item.profiles.join(", "))} · ${esc(item.verification)} · content: ${esc(item.content_review)}<br>${esc(item.note)}<br><a href="${safeUrl(item.url)}" target="_blank" rel="noopener noreferrer">${item.kind === "archive_member" ? "Open parent archive" : item.kind === "documentation" ? "Open dataset / documentation" : "Open source file"} ↗</a></li>`).join("");
  details.querySelector(".dataset-file-list").innerHTML = files ? `<ul>${files}</ul>` : "No individual file locations were verified.";
  details.dataset.loaded = "true";
}, true);
function renderDatasets() {
  const cell = $("dataset-cell").value, material = $("dataset-material").value, type = $("dataset-type").value;
  const profile = $("dataset-profile").value, aging = $("dataset-aging").value, query = $("dataset-query").value;
  const rows = datasets.filter(r => (!cell || r.parameter_link.cell_ids.includes(cell))
    && (!material || r.material_families.includes(material)) && (!type || r.test_types.includes(type))
    && (!profile || r.profiles.includes(profile)) && (!aging || r.aging_data.status === aging)
    && ui.matchesSearch(datasetSearchText.get(r.id), query));
  $("dataset-count").textContent = `${rows.length} of ${datasets.length} parameter-linked external sources`;
  $("dataset-cards").innerHTML = rows.map(r => `<article class="source-card" id="source-${esc(r.id)}"><span class="tag">${esc(r.material_families.join(" / "))} · external link</span><h3>${esc(r.title)}</h3><p>${esc(r.cell_identity)}</p><p><b>Tests:</b> ${esc(r.test_types.map(words).join(", "))}<br><b>Parameter match:</b> ${esc(words(r.parameter_link.match_level))}</p><div class="actions"><a class="button" href="${safeUrl(r.source.url)}" target="_blank" rel="noopener noreferrer">Open original dataset ↗</a><a class="button" href="${safeUrl(r.license.evidence_url)}" target="_blank" rel="noopener noreferrer">${esc(r.license.identifier)} ↗</a></div><details><summary>Conditions, source review and missing items</summary><p><b>Electrode OCP anchor:</b> ${esc(words(r.ocp_anchor.kind))}<br>${esc(r.ocp_anchor.evidence)}<br>Half-cell temperature labels / °C: ${esc(r.ocp_anchor.half_cell_temperatures_C.length ? r.ocp_anchor.half_cell_temperatures_C.join(", ") : "Not independently verified")}</p><p><b>Profiles:</b> ${esc(r.profiles.join(", ") || "No named drive profile verified")}</p><p>${esc(r.rate_summary)}<br>Source temperature labels / °C: ${esc(r.temperatures_C.length ? r.temperatures_C.join(", ") : "Not verified")}</p><p><b>Ageing data:</b> ${esc(words(r.aging_data.status))}${r.aging_data.kinds.length ? " (" + esc(r.aging_data.kinds.join(", ")) + ")" : ""}<br>${esc(r.aging_data.evidence)} <a href="${safeUrl(r.aging_data.source_url)}" target="_blank" rel="noopener noreferrer">Coverage evidence ↗</a></p><p>${esc(r.parameter_link.evidence)}</p><p>${esc(r.license.note)}</p><p>Version: ${esc(r.source.version)} · Checked: ${esc(r.review.checked_on)} · ${esc(words(r.review.level))}</p><p>${esc(r.review.note)}</p><p>${esc(r.channels.note)}</p><p>Components without a native catalog join: ${esc(r.parameter_link.missing_components.join(", "))}</p><ul>${r.missing_items.map(item => `<li>${esc(item)}</li>`).join("")}</ul></details>${renderDatasetFileLocations(r)}</article>`).join("") || '<p class="empty">No parameter-linked source matches these filters. Try resetting the filters.</p>';
}
for (const id of datasetFilterIds) $(id).addEventListener(id === "dataset-query" ? "input" : "change", renderDatasets);
$("reset-datasets").addEventListener("click", () => {
  for (const id of datasetFilterIds) $(id).value = "";
  renderDatasets();
});
function goTo(section) {
  if (window.location.hash !== "#" + section) window.location.hash = section;
  else $(section).scrollIntoView({block: "start"});
}
$("detail").addEventListener("click", event => {
  const button = event.target.closest("[data-open-cell]");
  if (!button) return;
  $("cell-query").value = "";
  $("cell-material").value = "";
  openCell(button.dataset.openCell);
  renderCellChoices();
  restoreSelect("cell-ocp-select", detailId);
  renderCellOcp();
  showCellTab("ocp");
  goTo("cell-package");
});
$("copy-view").addEventListener("click", async () => {
  const cellView = currentCellView();
  const state = {
    cell: activeCell, cell_family: $("cell-material").value, cq: $("cell-query").value, cell_tab: activeTab,
    cell_ocp: cellView.curve, parameter: cellView.parameter, category: cellView.category, variant: cellView.variant,
    pq: cellView.query, sample: cellView.sample, ocp: detailId, compare: [...selected].join(","),
    material: $("material").value, ocp_cell: $("ocp-cell").value, query: $("query").value,
    repr: $("representation").value, direction: $("direction").value,
    source_cell: $("dataset-cell").value, source_material: $("dataset-material").value,
    test_type: $("dataset-type").value, profile: $("dataset-profile").value, ageing: $("dataset-aging").value,
    source_query: $("dataset-query").value,
  };
  const section = window.location.hash.slice(1) || "cell-package";
  const url = ui.viewURL(window.location.href, state, section);
  $("view-link").value = url;
  $("view-link-label").hidden = false;
  try {
    if (!navigator.clipboard?.writeText) throw new Error("Clipboard unavailable");
    await navigator.clipboard.writeText(url);
    $("view-status").textContent = "View link copied. Local links work on this computer; repository access is unchanged.";
  } catch {
    $("view-link").focus();
    $("view-link").select();
    $("view-status").textContent = "Select and copy the view link. Local links work on this computer.";
  }
});
function updateNavigation() {
  const section = window.location.hash || "#cell-package";
  for (const link of document.querySelectorAll("nav a")) {
    const active = link.getAttribute("href") === section;
    link.classList.toggle("active", active);
    if (active) link.setAttribute("aria-current", "location");
    else link.removeAttribute("aria-current");
  }
}

restoreSelect("material", saved.get("material"));
restoreSelect("ocp-cell", saved.get("ocp_cell"));
restoreSelect("representation", saved.get("repr"));
restoreSelect("direction", saved.get("direction"));
$("query").value = saved.get("query") || "";
restoreSelect("cell-material", saved.get("cell_family"));
$("cell-query").value = saved.get("cq") || "";
restoreSelect("dataset-cell", saved.get("source_cell"));
restoreSelect("dataset-material", saved.get("source_material"));
restoreSelect("dataset-type", saved.get("test_type"));
restoreSelect("dataset-profile", saved.get("profile"));
restoreSelect("dataset-aging", saved.get("ageing"));
$("dataset-query").value = saved.get("source_query") || "";
if (activeCell) renderCell();
renderCellChoices();
renderOcpResults();
refreshComparison();
renderDatasets();
window.addEventListener("hashchange", updateNavigation);
updateNavigation();
})();
