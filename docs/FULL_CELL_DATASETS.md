# Supporting full-cell references for electrochemical parameters

[Battery parameter index](../data/batteries/README.md) ·
[Supporting tests by material](../data/full-cell/README.md) ·
[Link metadata](../data/full-cell/datasets.json) ·
[Selected source paths](../data/full-cell/files.csv) ·
[Project scope and excluded sources](PROJECT_SCOPE.md)

E-BatP is an electrochemical model parameter library. Full-cell tests help users
interpret and compare admitted parameter sources. Each active external source
explicitly references stored OCP, diffusion or kinetics records, with its own
match level and missing components. Test-only sources are excluded.

OCP and model parameter values are extracted into versioned local records when
reuse permission and definitions are established. New whole-cell observations
remain introductions and provider links. Search, exports, viewer generation and
CI do not fetch these observations. The 51 retained legacy packaged test files
are supporting observations for admitted parameter packages.

There are **11 parameter-associated external sources / 357 selected locators**.
A locator may identify parameter evidence, documentation, an archive, a named
member or a test file. Counts are neither independent tests/specimens nor a
complete temperature/rate matrix.

## Parameter-to-experiment links

| Parameter package / supporting source | Linked experiments | Association and remaining limits |
|---|---|---|
| [LG M50LT / Hallemans2025](../data/full-cell/hallemans-m50lt-eis-2025.md) | Author EIS and unnamed drive-cycle MATs | Same study/model as native grouped diffusion and kinetics. Third-party OCP reuse, intrinsic D/k and serialized-specimen joins unresolved; drive cycle is not named US06. |
| [NCR18650B / HNEI](../data/full-cell/hnei-ncr18650b-2016.md) | Harvested NE/PE and selected full-cell FORM/RPT ZIP members | Four native pseudo-OCP branches; same study/model, exact donor unresolved. No matched D/kinetics. |
| [NCR18650B / Bayreuth](../data/full-cell/bayreuth-ncr18650b-2023.md) | Thirteen beginning-of-life pseudo-OCV, pulse and EIS MAT/CSV links | Cross-study reference to HNEI OCP. Whole-cell pseudo-OCV is not electrode OCP; contents unread and reuse license not stated. |
| [NCR18650B / Virtual Vehicle](../data/full-cell/virtual-vehicle-ncr18650b-aging-2023.md) | 116 external H5 cell files and protocol PDF | Cycle/calendar ageing; HNEI OCP is a same-model cross-study reference, not a shared-specimen or parameter-transfer claim. H5 contents unread. |
| [NCR18650B / Stanford](../data/full-cell/stanford-ncr18650b-rates-2021.md) | Fifteen NCA/k1 workbooks, 0.05/1/2/3/5C at 5/25/35 C | Cross-study HNEI OCP reference. Discharge sweep; no multi-rate charge sweep or same-study D/k. |
| [CALB / NEXTBMS](../data/full-cell/nextbms-calb-nmc532-2026.md) | Characterization, dynamic/ageing histories and four-temperature EIS paths in 7z containers | Four native half-cell branches; same study/model, distinct specimens. Direction/stage-count conflicts retained; GITT observations do not themselves supply D. |
| [Molicel P45B / About:Energy](../data/full-cell/aboutenergy-p45b-2026.md) | CC/GITT/WLTP at 10/25/40/60 C, eVTOL at 25/40/60 C | Native fitted OCP and diffusion/kinetic laws, with source conventions. Experimental/model columns and alternative parameterizations remain separate. |
| [Molicel P45B / TUM](../data/full-cell/tum-p45b-halfcell-aging-2026.md) | Harvested finite-current half cells and one 800-EFC checkup table | Five native branches under scoped first-party MIT. Same study/model; exact donor and half-cell temperature unresolved; reconstructed Si excluded. |
| [LG M50 / TEC2021](../data/full-cell/tec-lgm50-multitemperature-2021.md) | Forty-eight discharge CSV paths, 0/10/25 C at 0.1/0.5/1/2C | Explicit reuse of stored Chen2020 OCP expressions; full-cell tests are a different study. No verified WLTP in this release. |
| [LG MJ1 / SNU2024](../data/full-cell/snu-mj1-dynamic-aging-2024.md) | One 80-cell staged-ageing ZIP | DLR-SINTEF OCP is a same-model, cross-study reference. Inner paths and measured I/V/T remain unverified; no named US06/WLTP trace established. |
| [HAIDI / Rehm2025](../data/full-cell/haidi-lfp-rehm2025.md) | Original dataset access point; six-temperature OCV, multi-rate CC/CP and GEIS described by the paper | Seven native pseudo-OCP branches under CC BY 4.0. Same study/model; one cathode branch quarantined. Original full-cell filenames/headers and donor serials unresolved; coverage is dataset-level `container_only`. |

## Find supporting observations

The [LFP](../data/full-cell/LFP.md), [NMC](../data/full-cell/NMC.md),
[NCA](../data/full-cell/NCA.md), [LCO](../data/full-cell/LCO.md) and
[NCO](../data/full-cell/NCO.md) pages organize references by the parameter
package's material family. Start from the battery/model page to inspect OCP,
diffusion, kinetics, parameter definitions and associated tests together.

```bash
ebp datasets --cell molicel-p45b-aboutenergy2026 --profile WLTP
ebp datasets --files --cell lg-m50 --test-type constant_current
ebp datasets --cell lg-m50lt-hallemans2025 --test-type eis --json
ebp datasets --material NCA --aging-status available --json
```

The legacy CLI command `datasets` searches supporting source metadata. It does
not expand the project's scope into a general test-data repository. `--files`
searches individual inspected locators and does not inherit unverified source
profiles. An archive-member URL opens its parent container; extract the exact
named member yourself. `full_cell_data()` reads retained packaged test IDs only.

## Interpretation and reuse

`parameter_components` gives separate OCP, diffusion and kinetics record IDs,
quantity definitions, matching evidence and gaps. Whole-cell OCV is not electrode
OCP; EIS/GITT does not uniquely identify intrinsic diffusion or kinetics. M50LT
R-squared-over-D times and capacitances remain grouped quantities. A common
chemistry, capacity or model name does not establish identical specimens.

Half-cell temperature is independent of full-cell setpoints. A source protocol
is not a verified condition grid, and a setpoint is not a measured temperature
trace. Source filenames are not proof of channel headers or phase boundaries.

Ageing status is `available`, `not_reported` or `unverified`. Available evidence
retains cycle/calendar kinds and representative linked paths; formation or
repeated initial tests alone do not establish ageing. With `--files`, the ageing
filter applies to the parent source, not every file.

`source_listing` verifies a listed link; `archive_directory` verifies a member
name and size. `content_review=not_read` remains explicit.
`documentation_reviewed` applies to documents, not measured observations.
`existing_source_audit` refers to reviewed catalog evidence. There is no
automatic URL-health certification for every file.

Source-specific licenses apply. A link or an accessible download does not grant
redistribution permission; `not-stated` is not a permissive license. Do not
transfer software licenses onto third-party electrode data. See
[HAIDI rights](HAIDI_REHM2025.md), [TUM first-party scope](TUM_OCP_RIGHTS.md),
[M50LT holds](HALLEMANS2025.md) and [data licenses](../DATA_LICENSES.md).

## Contributions and historical leads

Use the [external-source template](../templates/external-dataset.json) only for
supporting tests linked to actual stored parameters. Supply component record
IDs, source versions, license, match evidence, source paths, coverage and missing
items. Empty placeholders are staging aids, not admissible active records.
`ebp validate` rejects entries with all three parameter components empty.

The [original seven-source review](EXTERNAL_FILE_REVIEW.md) remains historical
research evidence. Six test-only sources and A123 9 Ah were subsequently excluded;
see [scope decisions](PROJECT_SCOPE.md). Source suggestions can remain issues
until an admissible parameter anchor is established. The optional archive
inspector is never invoked automatically by catalog search or reconstruction.
