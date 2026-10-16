"use strict";
const data = window.EBP_DATA;
const $ = id => document.getElementById(id);
const esc = value => String(value).replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const directionLabel = {lithiation:"嵌锂",delithiation:"脱锂",unspecified:"未区分方向"};
const colors = ["#2c7155","#d3a14f","#7c91b6","#a87589","#629b98","#8c9a50","#bc7560","#8080ae","#4e8fac","#8b7a5f"];
const selected = new Set(["lfp-afshar2017-formula","sintef-lfp-d07eb6-c3-delithiation","sintef-lfp-178617-c3-delithiation"]);
let detailId = "lfp-afshar2017-formula";
const safeUrl = value => /^https?:\/\//.test(value || "") ? esc(value) : "#";

$("total").textContent = data.records.length;
$("stats").innerHTML = [[data.records.filter(r=>r.representation.kind==="table").length,"实测 OCP 分支 · 4 个样品"],[data.records.filter(r=>r.representation.kind==="expression").length,"OCP 文献解析公式"],[data.parameters.length,"其他模型参数 · LG M50"],[data.full_cell_tests.length,"同型号全电池测试文件"]].map(([n,label])=>`<div class="stat"><strong>${n}</strong><span>${esc(label)}</span></div>`).join("");

function filtered(){
  const query=$("query").value.toLowerCase().trim();
  return data.records.filter(r=>(!$("material").value||r.material===$("material").value)&&(!$("representation").value||r.representation.kind===$("representation").value)&&(!$("direction").value||r.direction===$("direction").value)&&(!query||JSON.stringify({...r,display_points:undefined}).toLowerCase().includes(query)));
}
function render(){
  const rows=filtered();
  $("result-count").textContent=`${rows.length} / ${data.records.length}`;
  $("records").innerHTML=rows.map(r=>`<article class="record ${selected.has(r.id)?"selected":""}"><div class="record-head"><button class="record-title" data-detail="${esc(r.id)}">${esc(r.title)}</button><input aria-label="对比 ${esc(r.id)}" type="checkbox" data-compare="${esc(r.id)}" ${selected.has(r.id)?"checked":""}></div><div class="record-tags"><span class="tag ${r.representation.kind==="expression"?"formula":""}">${r.representation.kind==="expression"?"解析公式":"C/50 伪 OCP"}</span><span class="tag">${directionLabel[r.direction]}</span><span class="tag">${r.x.kind==="stoichiometry"?"化学计量比 θ":"分支容量坐标"}</span></div><small>${esc(r.id)}</small></article>`).join("")||'<p class="empty">没有匹配的记录。可调整关键词或筛选条件。</p>';
  renderCharts();
}
$("records").addEventListener("click",event=>{const button=event.target.closest("[data-detail]");if(button){detailId=button.dataset.detail;renderDetail();$("detail").scrollIntoView({behavior:"smooth",block:"nearest"});}});
$("records").addEventListener("change",event=>{const target=event.target;if(target.dataset.compare){target.checked?selected.add(target.dataset.compare):selected.delete(target.dataset.compare);render();}});
for(const id of ["query","representation","direction"]) $(id).addEventListener(id==="query"?"input":"change",render);
$("material").addEventListener("change",()=>{
  selected.clear();
  const rows=filtered(),formula=rows.find(r=>r.representation.kind==="expression"),firstTable=rows.find(r=>r.representation.kind==="table");
  if(formula)selected.add(formula.id);
  if(firstTable)for(const r of rows.filter(r=>r.direction===firstTable.direction).slice(0,2))selected.add(r.id);
  if(rows.length){detailId=rows[0].id;renderDetail();}
  render();
});
$("reset").addEventListener("click",()=>{$("query").value="";$("material").value="";$("representation").value="";$("direction").value="";render();});
$("clear-selection").addEventListener("click",()=>{selected.clear();render();});

function renderCharts(){
  const rows=data.records.filter(r=>selected.has(r.id));
  $("selected-count").textContent=`${rows.length} 条已选`;
  if(!rows.length){$("charts").innerHTML='<p class="empty">从左侧勾选曲线，开始对比。</p>';return;}
  const groups=new Map();
  for(const r of rows){const key=r.x.kind+":"+r.direction+":"+r.material;if(!groups.has(key)) groups.set(key,[]);groups.get(key).push(r);}
  $("charts").innerHTML=[...groups.values()].map(group=>{
    const first=group[0],all=group.flatMap(r=>r.display_points),lo=Math.min(...all.map(p=>p[1])),hi=Math.max(...all.map(p=>p[1]));
    const pad=Math.max((hi-lo)*.08,.025),ymin=lo-pad,ymax=hi+pad;
    const X=x=>48+x*356,Y=y=>190-(y-ymin)/(ymax-ymin)*156;
    let svg='<svg viewBox="0 0 430 225" role="img" aria-label="'+esc(first.material+" "+first.x.kind+" "+directionLabel[first.direction])+ '">';
    for(let i=0;i<=4;i++){const x=i/4,y=ymin+(ymax-ymin)*i/4;svg+=`<line class="grid" x1="48" x2="404" y1="${Y(y)}" y2="${Y(y)}"/><text x="40" y="${Y(y)+3}" text-anchor="end">${y.toFixed(2)}</text><text x="${X(x)}" y="210" text-anchor="middle">${x.toFixed(2)}</text>`;}
    svg+='<text x="48" y="20">V vs Li/Li⁺</text><line class="axis" x1="48" x2="404" y1="190" y2="190"/>';
    svg+=group.map(r=>{const color=colors[data.records.indexOf(r)%colors.length],path=r.display_points.map((p,i)=>`${i?"L":"M"}${X(p[0]).toFixed(2)},${Y(p[1]).toFixed(2)}`).join(" ");return `<path class="curve" stroke="${color}" d="${path}"><title>${esc(r.id)}</title></path>`;}).join("");
    svg+='</svg>';
    const label=first.x.kind==="stoichiometry"?"化学计量比 θ · 公式":"分支归一化通过容量 · "+directionLabel[first.direction];
    return `<section class="plot"><h3>${esc(first.material)} / ${label}</h3>${svg}<div class="legend">${group.map(r=>`<span><i style="background:${colors[data.records.indexOf(r)%colors.length]}"></i>${esc(r.id.replace("sintef-","").replace("-c3-"," · "))}</span>`).join("")}</div><div class="axis-note">${first.x.kind==="stoichiometry"?"显示数学定义区间；不代表已验证的拟合范围。":"0 → 1 为该分支的测试进程。不同分支端点不代表相同锂含量。"}</div></section>`;
  }).join("");
}

function renderDetail(){
  const r=data.records.find(r=>r.id===detailId),experiment=data.experiments[r.experiment_id];
  const field=(label,value)=>`<div class="field"><strong>${esc(label)}</strong>${value}</div>`;
  $("detail").innerHTML=`<div class="detail-top"><div><div class="eyebrow">RECORD / ${esc(r.id)}</div><h2>${esc(r.title)}</h2></div><div class="actions"><a class="button" href="downloads/${esc(r.id)}.csv" download>${r.representation.kind==="expression"?"采样公式 CSV":"完整提取点 CSV"}</a><a class="button" href="downloads/${esc(r.id)}.json" download>元数据与来源 JSON</a></div></div><div class="detail-grid">${field("横坐标定义",esc(r.x.definition))}${field("电芯关联",esc(r.cell_link.evidence))}${field("测量条件",esc(experiment?experiment.protocol+" · Cycle 3 · "+r.temperature.description:r.temperature.description))}${field("数据与验证状态",esc((r.representation.kind==="table"?r.representation.point_count+" 个保留实测点":"解析表达式，无原始实测点")+" · 尚未独立验证全电池"))}${field("来源",r.source_ids.map(id=>`<a href="${safeUrl(data.sources[id].url)}" target="_blank" rel="noopener noreferrer">${esc(id)}</a>`).join(" · "))}${field("许可",`<a href="licenses/${r.license==="BSD-3-Clause"?"PyBaMM-BSD-3-Clause.txt":"CC-BY-4.0.txt"}">${esc(r.license)}</a>`)}${field("使用限制",'<ul>'+r.limitations.map(v=>`<li>${esc(v)}</li>`).join("")+"</ul>")}${field("处理与追溯",`<code>${esc(r.provenance.location)}</code><br>${esc(r.provenance.derivation)}${r.representation.sha256?"<br>SHA-256: <code>"+esc(r.representation.sha256)+"</code>":""}`)}</div>${r.representation.kind==="expression"?`<div class="formula-text">${esc(r.representation.expression)}<br><small>x = θ；CSV 下载为 2001 点数值采样，非实验数据。</small></div>`:""}`;
}
$("source-cards").innerHTML=Object.entries(data.sources).map(([id,source])=>`<article class="source-card"><span class="tag">${source.kind==="software"?"代码分发来源":"科学来源"} · ${esc(source.year)}</span><h3>${esc(source.title)}</h3><p>${esc(source.authors.join(", "))}</p><p>${esc(source.role)}</p><a href="${safeUrl(source.url)}" target="_blank" rel="noopener noreferrer">${esc(id)} ↗</a></article>`).join("");
render();renderDetail();

function renderParameters(){
  const category=$("parameter-category").value,rows=data.parameters.filter(p=>!category||p.category===category);
  $("parameter-count").textContent=rows.length+" 条";
  $("parameter-rows").innerHTML=rows.map(p=>`<tr><td><button data-parameter="${esc(p.id)}">${esc(p.name)}</button></td><td>${p.representation.kind==="scalar"?esc(p.representation.value):"多变量函数"}</td><td>${esc(p.unit)}</td></tr>`).join("");
}
$("parameter-category").addEventListener("change",renderParameters);
$("parameter-rows").addEventListener("click",event=>{const button=event.target.closest("[data-parameter]");if(!button)return;const p=data.parameters.find(p=>p.id===button.dataset.parameter);$("parameter-detail").innerHTML=`<b>${esc(p.name)}</b><p>${esc(p.provenance.origin_status)}</p><code>${esc(p.representation.kind==="expression"?p.representation.expression:p.provenance.location)}</code><p>${p.limitations.map(esc).join("<br>")}</p>`;});
$("test-sample").innerHTML=data.full_cell_tests.map(t=>`<option value="${esc(t.id)}">LG M50 · ${esc(t.sample_id)}</option>`).join("");
function renderFullCell(){
  const test=data.full_cell_tests.find(t=>t.id===$("test-sample").value),segments=test.preview_segments;
  const xmax=Math.max(...segments.flatMap(s=>s.points.map(p=>p[0]))),X=x=>48+x/xmax*356,Y=y=>190-(y-2.4)/1.9*156;
  let svg='<svg viewBox="0 0 430 230" role="img" aria-label="LG M50 实测不同倍率放电电压"><text x="48" y="20">全电池电压 / V</text>';
  for(let i=0;i<=4;i++){const y=2.4+1.9*i/4;svg+=`<line class="grid" x1="48" x2="404" y1="${Y(y)}" y2="${Y(y)}"/><text x="40" y="${Y(y)+3}" text-anchor="end">${y.toFixed(1)}</text><text x="${48+356*i/4}" y="209" text-anchor="middle">${(xmax*i/4).toFixed(1)}</text>`;}
  svg+=segments.map((s,i)=>`<path class="curve" stroke="${colors[i]}" d="${s.points.map((p,j)=>`${j?"L":"M"}${X(p[0]).toFixed(2)},${Y(p[1]).toFixed(2)}`).join(" ")}"><title>${s.C_rate}C, step ${s.step}</title></path>`).join("");
  svg+='<text x="225" y="228" text-anchor="middle">该放电段开始后的时间 / h</text></svg>';
  $("fullcell-chart").innerHTML=svg+'<div class="legend">'+segments.map((s,i)=>`<span><i style="background:${colors[i]}"></i>${s.C_rate}C · Step ${s.step}</span>`).join("")+"</div>";
  $("test-downloads").innerHTML=`<a class="button" href="downloads/${esc(test.path.split("/").pop())}" download>原始测试 CSV</a><a class="button" href="downloads/${esc(test.normalized_path.split("/").pop())}" download>标准化测试 CSV</a>`;
}
$("test-sample").addEventListener("change",renderFullCell);
renderParameters();renderFullCell();
