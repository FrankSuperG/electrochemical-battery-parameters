"use strict";

// Pure helpers shared by the static viewer and offline interaction checks.
window.EBP_UI = Object.freeze({
  filterParameters(parameters, {cell, category = "", variant = "", query = ""}) {
    const terms = query.trim().toLowerCase().split(/\s+/).filter(Boolean);
    return parameters.filter(p => p.cell_id === cell
      && (!category || p.category === category)
      && (!variant || p.conditions?.parameterization_variant === variant)
      && terms.every(term => [p.id, p.name, p.definition, p.unit, p.category]
        .filter(Boolean).join(" ").toLowerCase().includes(term)));
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
