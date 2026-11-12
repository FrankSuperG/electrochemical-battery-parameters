"use strict";

// Pure helpers shared by the static viewer and offline interaction checks.
const ebpSearchText = value => String(value ?? "").normalize("NFKC").toLowerCase().replace(/[-_]+/g, " ");
const ebpMatchesSearch = (text, query) => {
  const candidate = ebpSearchText(text);
  return ebpSearchText(query).trim().split(/\s+/).filter(Boolean).every(term => candidate.includes(term));
};

window.EBP_UI = Object.freeze({
  matchesSearch: ebpMatchesSearch,
  filterCells(cells, {family = "", query = ""}) {
    return cells.filter(cell => (!family || cell.family === family)
      && ebpMatchesSearch([cell.id, cell.name, cell.family].join(" "), query));
  },
  nextTab(tabs, current, key) {
    const index = tabs.indexOf(current);
    if (index < 0) return null;
    if (key === "Home") return tabs[0];
    if (key === "End") return tabs[tabs.length - 1];
    if (key === "ArrowRight") return tabs[(index + 1) % tabs.length];
    if (key === "ArrowLeft") return tabs[(index + tabs.length - 1) % tabs.length];
    return null;
  },
  filterParameters(parameters, {cell, category = "", variant = "", query = ""}) {
    return parameters.filter(p => p.cell_id === cell
      && (!category || p.category === category)
      && (!variant || p.conditions?.parameterization_variant === variant)
      && ebpMatchesSearch([p.id, p.name, p.definition, p.unit, p.category].filter(Boolean).join(" "), query));
  },
  parameterCSV(parameters) {
    const headers = ["id", "cell_id", "name", "category", "value_or_expression",
      "unit", "conditions_json", "definition", "source_ids", "origin_status", "license"];
    const rows = parameters.map(p => [p.id, p.cell_id, p.name, p.category,
      p.representation.kind === "table" ? "table:" + p.representation.path
        : (p.representation.value ?? p.representation.expression),
      p.unit, JSON.stringify(p.conditions || {}), p.definition || p.name,
      p.source_ids.join(";"), p.provenance.origin_status, p.license]);
    return [headers, ...rows].map(row => row.map(value =>
      '"' + String(value ?? "").replaceAll('"', '""') + '"').join(",")).join("\r\n") + "\r\n";
  },
  linkedSources(sources, cell) {
    return sources.filter(source => source.parameter_link.cell_ids.includes(cell));
  },
  nearestPreviewPoint(points, x) {
    if (!points.length || !Number.isFinite(x)) return null;
    const xs = points.map(point => point[0]);
    if (x < Math.min(...xs) || x > Math.max(...xs)) return null;
    return points.reduce((nearest, point) =>
      Math.abs(point[0] - x) < Math.abs(nearest[0] - x) ? point : nearest);
  },
  viewURL(href, state, section) {
    const url = new URL(href);
    url.search = "";
    for (const [key, value] of Object.entries(state)) {
      if (value !== undefined && value !== null && (value !== "" || ["compare", "material", "variant"].includes(key)))
        url.searchParams.set(key, value);
    }
    url.hash = section;
    return url.href;
  },
});
