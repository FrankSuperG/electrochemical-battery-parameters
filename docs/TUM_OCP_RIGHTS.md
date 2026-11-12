# TUM and M50LT OCP rights and definitions — 2026-10-23

**Follow-up, 2026-10-24:** [HAIDI reuse is now cleared through exact-DOI publisher metadata](HAIDI_REHM2025.md), with seven native branches and one quality quarantine. The original dated review/metadata below remain history; the framework MIT grant is not extended to HAIDI.

**v0.14 admits seven first-party TUM pseudo-OCP branches (40,378 points).**
Five belong to harvested Molicel P45B electrodes; two are laboratory graphite
comparators without a commercial-cell assignment. M50LT third-party OCP and
the other unresolved TUM inputs remain excluded. No full-cell observations
are added in this review.

[P45B model index](../data/batteries/molicel-p45b-tum-rehm2026.md) ·
[Native curve index](../data/ocp/README.md) ·
[Asset pins](../scripts/tum_ocp_assets.json) ·
[Machine-readable decisions](../src/ebp/data/evidence/tum-rehm2026/rights-review.json)

## Original sources and scoped admission

1. Rehm et al., *How to determine the degradation modes of lithium-ion
   batteries with silicon–graphite blend electrodes*, JPS 670 (2026) 239418,
   [original DOI](https://doi.org/10.1016/j.jpowsour.2026.239418).
   Section 2.4 identifies harvested P45B electrodes and laboratory graphite
   half-cells against lithium metal. Data availability points to the authors'
   GitHub. Methods were read in the [author-uploaded original paper](https://www.researchgate.net/publication/403407038_How_to_determine_the_degradation_modes_of_lithium-ion_batteries_with_silicon-graphite_blend_electrodes);
   the publisher PDF could not be retrieved. The article's CC BY license is
   recorded separately and is not used to relicense external tables.
2. The fixed author release [Zenodo 19555109, v2.0.0](https://zenodo.org/records/19555109)
   states **MIT**. The archive MD5 is
   `0f2c702fab98561dcc5eee8a09f90166`; its root is
   `tum-ees-DegradationModeAnalysis-d2e80c7/`.
3. Its bundled [Mathias Rehm MIT notice](../src/ebp/licenses/TUM-Rehm2026-MIT.txt),
   [SiGr attribution notice](../src/ebp/data/evidence/tum-rehm2026/input_data--silicon-graphite--README_additional_citations_necessary.txt),
   [graphite notice](../src/ebp/data/evidence/tum-rehm2026/input_data--graphite--README_additional_citations_necessary.txt)
   and [NCA notice](../src/ebp/data/evidence/tum-rehm2026/input_data--NCA--README_additional_citations_necessary.txt)
   identify the selected data as the authors' measurements published with the
   tool. This combined first-party release evidence supports the seven-file
   MIT admission. It does not clear third-party literature digitizations.
4. The seven MATs are also byte-identical to the corresponding files in
   [author revision 402bab94](https://github.com/tum-ees/DegradationModeAnalysis/tree/402bab94d20258162ff059b8d5d51abe40ec1c30).
   The manifest retains release members and SHA-256; the review records Git
   blob hashes. The complete mixed-source ZIP is not redistributed.

This replaces the earlier conservative P45B hold with a narrowly scoped
decision based on the fixed release, first-party notices and original paper.
The root README's instruction to check original sources still applies to the
remaining literature inputs. No author has been contacted.

## Extracted branches

| Source basename | Nodes | Association | Direction / source rate |
|---|---:|---|---|
| P45B_Cathode_Delithiation_0C03 | 5,481 | P45B harvested NCA | delithiation / filename 0.03C |
| P45B_Anode_Delithiation_0C02 | 9,386 | P45B harvested SiGr | delithiation / 0.02C |
| P45B_Anode_Delithiation_0C03 | 5,579 | P45B harvested SiGr | delithiation / filename 0.03C |
| P45B_Anode_Lithiation_0C02 | 9,400 | P45B harvested SiGr | lithiation / 0.02C |
| P45B_Anode_Lithiation_0C03 | 5,601 | P45B harvested SiGr | lithiation / filename 0.03C |
| Gr_Delithiation_Rehm2026 | 2,481 | SGL Carbon laboratory graphite only | delithiation / paper 0.0145C |
| Gr_Lithiation_Rehm2026 | 2,450 | SGL Carbon laboratory graphite only | lithiation / paper 0.0145C |

The graphite MAT variables retain the older `Gr_*_Kuecher` names; the importer
records these aliases. It does not assign laboratory graphite to P45B's
graphite phase. The NCA label is the author's material classification, not
an inferred composition ratio.

## Coordinates, rates and gaps

The source fields are `normalizedCapacity` and `voltage`. They are processed
finite-current branches, not instrument current/time records or certified
equilibrium OCP. Original MATs and every source voltage/capacity node are kept.
CSV columns are `x,potential_V,source_normalized_capacity,source_mat_row`.

The uniform `x` coordinate is normalized branch progress. First calculate
`q01=(q-min(q))/(max(q)-min(q))`; use `q01` or `1-q01` so the endpoint potential
decreases on named lithiation and increases on named delithiation. Stable-sort
by `x`. Each record states whether the axis was reversed. This does not infer
chronological acquisition order. Small source excursions beyond [0,1] and the
graphite lithiation vector's local backtrack remain recoverable through original
capacity and one-based row columns. No clipping, smoothing, resampling, row
deletion or inserted endpoints occurs. A stoichiometric mapping is required
before model use; `x` is not full-cell SOC or absolute lithium fraction.

The SiGr notice defines `0C03` as 0.03C, whereas paper Section 2.4 reports
0.033C in its protocol. Both labels are retained. Exact cycle selection,
absolute capacity and numeric half-cell temperature remain unresolved. Protocol
cutoffs do not guarantee that each supplied branch reaches every cutoff.

## Full-cell association

The [serial23 ageing checkup file](../data/full-cell/tum-p45b-halfcell-aging-2026.md#file-locations)
is linked at **same model, same study**. The paper describes four P45B cells,
25 C ageing, CCCV charge and CC discharge with periodic pOCV checks. This is
a source condition, not evidence of a measured temperature channel in that MAT.
The checkup file has not been numerically inspected here; continuous cycling
I/V/T, dynamic, EIS and multi-temperature matrices are not established.

The harvested beginning-of-test donor is not mapped to serial23. No same-study
intrinsic diffusion or kinetic coefficients were located. The separate
About:Energy P45B BPX is discoverable by model, but its parameters are not
transferred or called a same-study measured set.

## Sources still held

| Source | Decision / missing evidence |
|---|---|
| M50LT / Hallemans2025 | OCP is attributed to About:Energy personal communication. No explicit M50LT grant located in the original notes or current author/company repositories. Existing grouped parameters and tests remain unchanged. [Detailed review](HALLEMANS2025.md). |
| Stapf et al. M50/M50T/M50LT | Original [2025 paper](https://doi.org/10.1149/1945-7111/add112) is CC BY 4.0, but its raw-data statement is request-based. No open raw table resolved; no plot-digitized or substitute Hallemans curve admitted. |
| HAIDI LFP / graphite | Original [paper](https://doi.org/10.1016/j.jpowsour.2025.236290) identifies [dataset DOI](https://doi.org/10.14459/2024mp1762675). [Saved DOI metadata](../src/ebp/data/evidence/tum-rehm2026/haidi-datacite.json) resolves the provider but has an empty `rightsList`; the provider returned HTTP 429/timeouts. This was the v0.14 hold; the [v0.15 follow-up](HAIDI_REHM2025.md) resolves reuse/direction via publisher metadata and the original paper. One branch remains quarantined for quality. |
| M35A / LG M36 | First-party attribution alone does not establish original protocol, Li reference or study/full-cell mapping. These definitions still need primary confirmation. |
| Wetjen / Schmitt / Hossain and other literature curves | Original-source permission/definition checks remain incomplete; root MIT is not imposed on third-party inputs. |
| Reconstructed silicon | Derived from blend decomposition, not measured pure-silicon OCP. Version-specific reconstruction and later boundary/zero-fill corrections need separate review. |

The [offline importer](../scripts/seed_tum_ocp.py) accepts only seven pinned
members. Tests compare all original nodes and source rows, branch orientation,
licensing boundaries and study links. No new electrochemical model validation
is claimed.

## Executed verification

The local suite passes 142 tests, including all 40,378 admitted source nodes.
All 336 canonical files reproduce byte-for-byte through the offline seed
pipeline; the 244 generated navigation files and README index are current.
All prior 76 curve records, 1,041 non-OCP records and 61 full-cell records
are unchanged. Their full-cell file bytes are unchanged as well.
