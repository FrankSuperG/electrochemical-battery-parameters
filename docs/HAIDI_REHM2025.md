# HAIDI HDCF18650-1800 / Rehm2025 source review

Reviewed 2026-10-24. **Seven author-processed pseudo-OCP branches, 98,695
original nodes, are native under CC BY 4.0.** One additional cathode branch
is quarantined. Same-study full-cell multi-temperature charge/discharge and
GEIS are linked at dataset level; individual original filenames and observation
headers remain unverified. No new full-cell payload is packaged.

[Battery/model index](../data/batteries/haidi-hdcf18650-1800-rehm2025.md) ·
[Cell package](../data/cells/haidi-hdcf18650-1800-rehm2025.md) ·
[Full-cell source and access gaps](../data/full-cell/haidi-lfp-rehm2025.md) ·
[Pinned originals](../scripts/haidi_assets.json) ·
[Machine-readable rights and quality review](../src/ebp/data/evidence/haidi-rehm2025/review.json)

## Original study and model identity

Rehm, Fischer, Rubio-Gomez, Schuette, Sauer and Jossen, *Comparing the electrical
performance of commercial sodium-ion and lithium-iron-phosphate batteries*,
JPS 633 (2025) 236290, [original DOI](https://doi.org/10.1016/j.jpowsour.2025.236290).
The [original article at the German National Library](https://d-nb.info/1370379285/34)
was downloaded and Methods pages 3–4 were visually reviewed. Its article license
is CC BY 4.0; this is recorded separately from the dataset grant.

Table 1 identifies **LIBHE as HAIDI Energy Group HDCF18650-1800**, 1.8 Ah,
18650, LFP/graphite. The two sodium-ion cell types in the comparative source
are excluded from this package. A shared chemistry does not create an A123
association, and other commercial HAIDI data sheets/batches are not substituted.

## Data reuse evidence and conflicting catalog entries

The original paper identifies [dataset DOI 10.14459/2024mp1762675](https://doi.org/10.14459/2024mp1762675).
The exact-DOI [TUM publisher record in open.bydata](https://open.bydata.de/api/hub/search/datasets/10-14459-2024mp1762675)
belongs to its `mediatum` catalog. Its distribution has the exact mediatum
access URL, a `cc-by` license URI and the six authors' attribution.
The corresponding [GovData record](https://data.gov.de/suche/daten/rate-capability-tests-ocv-measurements-impedance-and-half-cell-measurements-of-two-sodium-ion-b99db5)
resolves its license URL to **CC BY 4.0**, independently consistent with the
[official DCAT-AP.de vocabulary](https://www.dcat-ap.de/def/licenses/20260924).

The retained factual mapping is:

```text
Dataset identifier: 10.14459/2024mp1762675
Distribution accessURL: https://mediatum.ub.tum.de/1762675
Distribution license: http://dcat-ap.de/def/licenses/cc-by
Resolved terms: https://creativecommons.org/licenses/by/4.0/
```

This is dataset-specific publisher-catalog evidence. It replaces the earlier
hold caused by an empty DataCite `rightsList` and unavailable provider page;
the framework's MIT license is not the HAIDI data grant. Attribution is to
**Mathias Rehm; Marco Fischer; Manuel Rubio-Gomez; Moritz Schuette;
Dirk Uwe Sauer; Andreas Jossen**. The author mirror additionally asks users
to cite the 2026 DMA framework paper, which is retained in source IDs.

Conflicting metadata are not hidden:

- DataCite still has an empty rights list. This does not itself forbid reuse.
- A [duplicate GovData record keyed by the mediatum URL](https://data.gov.de/suche/daten/rate-capability-tests-ocv-measurements-impedance-and-half-cell-measurements-of-two-sodium-ion-b)
  has a blank resource URL and `other-closed`/`UnknownIPR`, unlike the specific
  exact-DOI record with a valid distribution and author attribution.
- The exact-DOI RDF also types its generic license document as `UnknownIPR`,
  while its actual license URI, GovData frontend URL and official vocabulary
  resolve to CC BY 4.0. These are separate observations; the explicit license
  URI/terms and exact dataset identity support this scoped admission.

The review retains source URLs, observed license fields and response hashes.
Its own factual curation text is project MIT; that does not relicense data.

## Author mirror and original-data boundary

Eight original HAIDI MATs and the folder attribution notice are retained from
[fixed Zenodo release 19555109](https://zenodo.org/records/19555109), with the
archive MD5 and each member SHA-256 recorded. All eight MATs are byte-identical
to [author GitHub revision 402bab94](https://github.com/tum-ees/DegradationModeAnalysis/tree/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/LFP).
The [author notice](../src/ebp/data/evidence/haidi-rehm2025/TUM-LFP-source-notice.txt)
explicitly traces these curves to Rehm2025 and explains the electrode directions.

The primary provider returned web HTTP 429 and direct TLS/read timeouts,
including public metadata export/OAI attempts. The publisher metadata catalogs
remain accessible. Original mediatum observation filenames, headers and
mirror-to-original byte identity therefore remain unresolved. The native
tables are **author-processed mirrored branches**, not instrument raw files.
The mixed-source release ZIP and the paper PDF are not redistributed.

## Half-cell definitions and uniform format

The original paper identifies 25 C half-cell measurements against lithium
metal in CR2032 cells using harvested single-side-coated 14 mm electrodes and
LP57 electrolyte. The main protocol is 0.02C, with earlier 0.05C cycles;
exact MAT cycle indices are not supplied. Protocol ranges are graphite
0.01–1.5 V and LFP 2–4 V versus Li.

The MAT variable is `batteryData`, with `normalizedCapacity` and `voltage`.
The author notice explains that anode direction/capacity conventions were
swapped to match the full-cell definition. Named electrode lithiation and
delithiation are corroborated by endpoint potentials; they are not inferred
solely from the sign of the source capacity vector.

Each native CSV has:

```text
x,potential_V,source_normalized_capacity,source_mat_row
```

Normalize `q01=(q-min(q))/(max(q)-min(q))`; use `q01` or `1-q01` so potential
decreases along named lithiation and increases along named delithiation,
then stable-sort by this branch-progress coordinate. Original capacity and
one-based MAT row remain recoverable. No chronological order, absolute lithium
fraction or full-cell SOC is inferred. No clipping, smoothing, deleted points,
resampling or inserted endpoints is applied to admitted branches.

The paper reports Savitzky-Golay filtering for displayed half-cell curves;
the exact processing history of each MAT is not independently established.
Millivolt-scale source cutoff excursions are retained and disclosed. Supplied
voltage coverage can be narrower than the complete protocol, and no missing
cutoff region is reconstructed. Absolute half-cell Ah and stoichiometric
balancing endpoints remain missing.

| Branch | Nodes | Native status |
|---|---:|---|
| Graphite delithiation, 0.02C | 17,918 | Admitted |
| Graphite delithiation, 0.05C | 8,988 | Admitted; two nodes up to 2.8033 mV above the 1.5 V protocol cutoff retained |
| Graphite lithiation, 0.02C | 18,069 | Admitted |
| Graphite lithiation, 0.05C | 9,357 | Admitted |
| LFP delithiation, 0.02C | 18,620 | Admitted |
| LFP lithiation, 0.02C | 17,470 | Admitted; supplied low-potential coverage is incomplete |
| LFP lithiation, 0.05C | 8,273 | Admitted |
| LFP delithiation, 0.05C | 9,224 | **Quarantined**, original preserved; no native OCP CSV/record |

The quarantined branch starts at 1.5400677 V; source rows 1–9 fall below
the paper's 2 V cathode cutoff. Normalized capacity/voltage alone cannot
resolve the origin of that discrepancy. The entire branch is held rather
than trimmed or repaired. It is not counted among the seven native curves.

## Same-study full-cell tests: links and protocol evidence

The match level is **same model, same study**. The exact harvested donor,
serialized full-cell specimens and raw-file chain are unresolved. Conditions
below come from the paper/catalog, not inspected observation headers.

| Test class | Original study protocol | Access/verification |
|---|---|---|
| Full-cell quasi/relaxed OCV | 10/20/25/30/35/45 C; 0.05C quasi-OCV; relaxed OCV uses 0.1C steps/rests | [Dataset access point](https://mediatum.ub.tum.de/1762675); individual filenames/headers unverified |
| CC charge/discharge | Six temperatures; equal rates 0.1/0.2/0.33/0.5/0.67/1C; additional 1.5/2/2.5C discharge with charge held at 1C | Same dataset; `container_only`, no invented temperature-by-file matrix |
| Constant power | E-rate experiments and partial SOC windows | Described in paper; E-rates are not C-rates or named road profiles |
| GEIS / pulse resistance | Six temperatures, eleven SOCs; GEIS 10 mHz–100 kHz, 15 points/decade, 100 mA for LIBHE | Dataset description and paper methods confirmed; frequency/Z columns and files not read |
| Dynamic road cycles / ageing | No verified road profile or longitudinal ageing series | Not established; conditioning/rate cycles are not ageing evidence |

The EIS SOCs are 5/10/15/30/45/60/75/80/85/90/95%. The paper uses different
cells across test groups and new LIB cells across temperatures to limit ageing
effects. This does not create a same-specimen link to the harvested electrodes.
No full-cell time/current/voltage/temperature channels are advertised as read.
No same-study intrinsic diffusivity or kinetic law is inferred from relaxed
OCV/GITT or GEIS alone. No electrochemical-model validation is performed.
