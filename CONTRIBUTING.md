# Contributing

Discuss changes through issues or pull requests in the private repository. Each data addition should include:

1. Accessible original sources, stable versions, reuse licenses and citations.
2. Material, electrode and cell identities, distinguishing commercial model, lot, specimen and study family.
3. Protocol, reference electrode, direction, temperature and state; leave undisclosed information unknown.
4. Coordinates, units, validity domains, parameter definitions and all processing steps.
5. Original checksums, retained observations and a reproducible extraction script.
6. Measured/fitted/derived/borrowed/assumed origin, limitations and validation status.

Treat original instrument points, digitized plots and formula samples as distinct representations. Do not count multiple representations or branches from one source as independent evidence. Never join cells by chemistry or nominal capacity alone. Keep source NaNs or other gaps visible instead of silently imputing or deleting them. Preserve per-source attribution and notices.

Run `ebp validate`, `python -m pytest -q` and `ebp build-site`. When extraction changes, also run `python scripts/seed_v01.py --download` and verify deterministic generated data. Update record versions, hashes and changelog when values or interpretation change. Explain what was added, its cell-match evidence and its practical limits. Automated extraction does not replace source review.
