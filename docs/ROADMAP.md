# Roadmap

## Completed in v0.1

- Eight measured LFP/graphite pseudo-OCP branches and two attributed expressions.
- Explicit coordinate semantics, conservative cell matching and provenance.
- Thirty-eight LG M50 parameters and three same-model full-cell files.
- Python/CLI, interpolation, PyBaMM OCP components, local viewer, packaging and CI.

## Completed in v0.2

- LFP-first expansion: AMP20 fitted diffusion/kinetics/transport/thermal parameters linked to the full-discharge experiment.
- Ten 9 Ah A123 study-family CC tests with explicit identity and parameter gaps.
- Official BPX LFP example OCP fits and scalar parameters, with unresolved commercial identity.
- Cell-scoped exports, match/coverage inspection, English documentation/viewer and Atlas companion logo.
- Preserved missing measurements, pinned originals, source-value audit and per-source notices.

## Completed in v0.3

- Ten material families, including NMC111/532/811, LNMO, silicon, silicon–graphite, LCO and NCA.
- Thirty-two measured branches from sixteen specimens; eleven attributed model expressions.
- NMC811 OCP linked to existing LG M50 tests; conservative association for three additional model packages.
- Two-input Arrhenius diffusivities, source-aware math transcription and dynamic viewer filters.

## Next priorities

1. Verify reusable LMO/LTO sources and locate electrode-resolved OCP and characterization data for an exactly identified commercial LFP model with matching full-cell experiments.
2. Extend the AMP20 experiment collection to fitting and held-out pulse tests; establish specimen mapping using supplementary evidence.
3. Audit BPX per-field origins and support electrolyte/entropy functions without changing their independent variables or units.
4. Curate GITT/EIS processing with geometry, concentration, electrode-area and identifiability assumptions.
5. Reproduce one complete DFN/SPMe/SPM case with versioned model options, initialization, sign conventions, fit/validation separation and voltage/temperature errors.
6. Add uncertainty only when supported by repeated observations or published estimates.

Public hosting, PyPI publication and automated parameter identification remain separate future decisions. Current cell packages are partial data collections, not validated plug-and-play models.

## v0.4 follow-up gaps

- Retrieve and inspect the explicitly same-paper Mohtat voltage/expansion deposit
  when public file access works; verify each file's units, protocol and specimen.
- Seek electrode-specific OCP and current-resolved baseline tests for the existing
  LFP entries without converting fitted/assumed quantities into measurements.
- Resolve Enertech commercial identity and seek original current/charge records;
  keep borrowed Dualfoil inputs separate from same-cell characterized quantities.
- Locate same-study full-cell observations for SINTEF material specimens, the
  nominal NCA design and Marquis context; do not join solely by chemistry.
