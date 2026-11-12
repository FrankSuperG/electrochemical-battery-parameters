"use strict";

// Pure logic only: these checks do not launch or access a browser.
const {test} = require("node:test");
const assert = require("node:assert/strict");
const {readFileSync} = require("node:fs");
const {runInNewContext} = require("node:vm");
const {join} = require("node:path");
const context = {window: {}, URL};
runInNewContext(readFileSync(join(__dirname, "../src/ebp/web/viewer-utils.js"), "utf8"), context);
const ui = context.window.EBP_UI;
const parameter = (id, overrides = {}) => ({id, cell_id: "cell-a", name: "Positive particle diffusivity",
  category: "diffusion", unit: "m2.s-1", definition: "Defined effective solid diffusivity",
  representation: {kind: "scalar", value: 0}, conditions: {parameterization_variant: "measured"},
  source_ids: ["paper-a"], provenance: {origin_status: "published_fit"}, license: "CC-BY-4.0", ...overrides});

test("parameter search combines cell, category, variant and all query terms", () => {
  const rows = [parameter("a"), parameter("b", {cell_id: "cell-b"}),
    parameter("c", {conditions: {parameterization_variant: "model"}}),
    parameter("d", {category: "kinetics", unit: "A.m-2"})];
  const result = ui.filterParameters(rows, {cell: "cell-a", category: "diffusion", variant: "measured", query: "  POSITIVE  m2.s-1 "});
  assert.equal(result.length, 1);
  assert.strictEqual(result[0], rows[0]);
  assert.equal(ui.filterParameters(rows, {cell: "cell-a", query: "not found"}).length, 0);
  assert.equal(rows.length, 4);
});

test("cell search matches model aliases and requires the selected material family", () => {
  const cells = [
    {id: "lg-m50", name: "LG M50 | 5 Ah", family: "NMC"},
    {id: "lg-m50-oregan2022", name: "LG M50 | O'Regan2022", family: "NMC"},
    {id: "panasonic-ncr18650b-hnei2016", name: "Panasonic NCR18650B", family: "NCA"},
  ];
  assert.equal(ui.filterCells(cells, {family: "NMC", query: "m50-lg"}).length, 2);
  assert.equal(ui.filterCells(cells, {family: "NCA", query: "LG M50"}).length, 0);
  assert.strictEqual(ui.filterCells(cells, {query: "panasonic hnei2016"})[0], cells[2]);
});

test("cell tabs support wrap-around and leave scrolling keys alone", () => {
  const tabs = ["parameters", "ocp", "experiments", "evidence"];
  assert.equal(ui.nextTab(tabs, "parameters", "ArrowLeft"), "evidence");
  assert.equal(ui.nextTab(tabs, "evidence", "ArrowRight"), "parameters");
  assert.equal(ui.nextTab(tabs, "experiments", "Home"), "parameters");
  assert.equal(ui.nextTab(tabs, "ocp", "End"), "evidence");
  assert.equal(ui.nextTab(tabs, "ocp", "ArrowDown"), null);
});

test("CSV preserves zero, quoted definitions, conditions, source and license", () => {
  const csv = ui.parameterCSV([parameter("a", {definition: 'Source says "effective",\nnot intrinsic'})]);
  assert.ok(csv.includes('"0"'));
  assert.ok(csv.includes('"Source says ""effective"",\nnot intrinsic"'));
  assert.ok(csv.includes('"{""parameterization_variant"":""measured""}"'));
  assert.ok(csv.includes('"paper-a","published_fit","CC-BY-4.0"'));
});

test("CSV keeps source expressions and table paths without sampling or fitting", () => {
  const rows = [parameter("law", {representation: {kind: "expression", expression: "max(1, 2)*sto"}}),
    parameter("table", {representation: {kind: "table", path: "parameter_tables/native.csv"}})];
  const csv = ui.parameterCSV(rows);
  assert.ok(csv.includes('"max(1, 2)*sto"'));
  assert.ok(csv.includes('"table:parameter_tables/native.csv"'));
  assert.ok(!csv.includes("undefined"));
});

test("linked sources use explicit cell ownership instead of shared names", () => {
  const sources = [{id: "same-study", parameter_link: {cell_ids: ["cell-a"]}},
    {id: "same-name-other-study", parameter_link: {cell_ids: ["cell-a-other"]}}];
  assert.strictEqual(ui.linkedSources(sources, "cell-a")[0], sources[0]);
  assert.equal(ui.linkedSources(sources, "cell-a").length, 1);
  assert.equal(ui.linkedSources(sources, "unknown").length, 0);
});

test("chart inspection returns retained preview points and never extrapolates", () => {
  const points = [[.2, 3.1], [.5, 3.4], [.8, 3.6]];
  assert.strictEqual(ui.nearestPreviewPoint(points, .44), points[1]);
  assert.strictEqual(ui.nearestPreviewPoint(points, .2), points[0]);
  assert.equal(ui.nearestPreviewPoint(points, .1), null);
  assert.equal(ui.nearestPreviewPoint(points, .9), null);
  assert.equal(ui.nearestPreviewPoint(points, NaN), null);
  assert.equal(ui.nearestPreviewPoint([], .5), null);
});

test("view links preserve all-material/all-variant and empty comparison states", () => {
  const link = new URL(ui.viewURL("https://example.org/viewer/?discard=old#library", {
    cell: "cell-a", cell_tab: "ocp", cell_ocp: "curve-a", material: "", variant: "", compare: "", query: "LFP / graphite", category: "diffusion",
  }, "cell-package"));
  assert.equal(link.searchParams.get("material"), "");
  assert.equal(link.searchParams.get("variant"), "");
  assert.equal(link.searchParams.get("compare"), "");
  assert.equal(link.searchParams.get("query"), "LFP / graphite");
  assert.equal(link.searchParams.get("cell"), "cell-a");
  assert.equal(link.searchParams.get("cell_tab"), "ocp");
  assert.equal(link.searchParams.get("cell_ocp"), "curve-a");
  assert.equal(link.searchParams.has("discard"), false);
  assert.equal(link.hash, "#cell-package");
});
