# Battery model index

[Repository README](../../README.md) · [All data](../README.md)

OCP and parameter links open repository data. Every indexed package has stored OCP, diffusion or kinetics records; full-cell links are supporting references to source descriptions and downloads. **Not extracted** means no reusable native record is curated; it is not a claim that no measurement exists.

Coverage labels below are source-level discovery aids. Read each model page for study, temperature, profile, licence and specimen limits. Half-cell temperature is tracked separately.

[Extraction audit for every battery/study: stored / reuse unresolved / definition unresolved / not located](../../docs/PARAMETER_AUDIT.md)

Record counts include published assumptions, borrowed functions, activation energies and optional submodel inputs, not a count of independent measurements or solid-electrode coefficients. Read parameter names and origin fields before selecting a model input.

## LFP

| Battery / study | OCP | Diffusion | Kinetics | Full-cell tests | Coverage / matching |
|---|---|---|---|---|---|
| [A123 18650M1A &#124; Jahn2024 LFP/graphite](a123-18650m1a-jahn2024.md) | [2 modeled OCPn](../cells/a123-18650m1a-jahn2024.md#ocp-curves) | Not extracted | Not extracted | [14 packaged](a123-18650m1a-jahn2024.md#full-cell-tests) | See test conditions / gaps<br>same model same study · [Match / gaps](a123-18650m1a-jahn2024.md#matching-and-gaps) |
| [A123 AMP20M1HD-A &#124; 20 Ah LFP pouch](a123-amp20m1hd-a.md) | Not extracted | [6 records](../parameters/a123-amp20m1hd-a--diffusion.csv) | [6 records](../parameters/a123-amp20m1hd-a--kinetics.csv) | [1 packaged](a123-amp20m1hd-a.md#full-cell-tests) | See test conditions / gaps<br>same model same study · [Match / gaps](a123-amp20m1hd-a.md#matching-and-gaps) |
| [HAIDI HDCF18650-1800 &#124; Rehm2025 LFP/graphite](haidi-hdcf18650-1800-rehm2025.md) | [7 pseudo-OCP](../cells/haidi-hdcf18650-1800-rehm2025.md#ocp-curves) | Not extracted | Not extracted | [1 external source](haidi-hdcf18650-1800-rehm2025.md#full-cell-tests) | multi-T, EIS<br>same model same study · [Match / gaps](haidi-hdcf18650-1800-rehm2025.md#matching-and-gaps) |
| [ISU-UConn &#124; laboratory LFP/graphite CR2032 family](isu-uconn-lfp-graphite-lab.md) | [4 pseudo-OCP](../cells/isu-uconn-lfp-graphite-lab.md#ocp-curves) | Not extracted | Not extracted | [21 packaged](isu-uconn-lfp-graphite-lab.md#full-cell-tests) | See test conditions / gaps<br>same study cell family · [Match / gaps](isu-uconn-lfp-graphite-lab.md#matching-and-gaps) |
| [LFP 2.3 Ah &#124; Prada2013 implementation &#124; part unresolved](prada2013-lfp-nominal-design.md) | [2 reused expressions](../cells/prada2013-lfp-nominal-design.md#ocp-curves) | [3 records](../parameters/prada2013-lfp-nominal-design--diffusion.csv) | [6 records](../parameters/prada2013-lfp-nominal-design--kinetics.csv) | [Not linked](prada2013-lfp-nominal-design.md#full-cell-tests) | See test conditions / gaps<br>parameter set only · [Match / gaps](prada2013-lfp-nominal-design.md#matching-and-gaps) |
| [Undisclosed LFP/graphite 18650, 2 Ah (BPX)](bpx-lfp-18650-2ah-undisclosed.md) | [2 expressions](../cells/bpx-lfp-18650-2ah-undisclosed.md#ocp-curves) | [6 records](../parameters/bpx-lfp-18650-2ah-undisclosed--diffusion.csv) | [4 records](../parameters/bpx-lfp-18650-2ah-undisclosed--kinetics.csv) | [Not linked](bpx-lfp-18650-2ah-undisclosed.md#full-cell-tests) | See test conditions / gaps<br>unmatched · [Match / gaps](bpx-lfp-18650-2ah-undisclosed.md#matching-and-gaps) |

## NMC

| Battery / study | OCP | Diffusion | Kinetics | Full-cell tests | Coverage / matching |
|---|---|---|---|---|---|
| [CALB generation 3b &#124; NEXTBMS2026](calb-gen3b-nextbms2026.md) | [4 pseudo-OCP](../cells/calb-gen3b-nextbms2026.md#ocp-curves) | Not extracted | Not extracted | [1 external source](calb-gen3b-nextbms2026.md#full-cell-tests) | multi-T, dynamic, ageing, EIS<br>same model same study · [Match / gaps](calb-gen3b-nextbms2026.md#matching-and-gaps) |
| [LG M50 &#124; 5 Ah NMC811/graphite-SiOx](lg-m50.md) | [2 expressions](../cells/lg-m50.md#ocp-curves) | [6 records](../parameters/lg-m50--diffusion.csv) | [7 records](../parameters/lg-m50--kinetics.csv) | [3 packaged + 1 external source](lg-m50.md#full-cell-tests) | multi-T<br>Cross-study / mixed sources · [Match / gaps](lg-m50.md#matching-and-gaps) |
| [LG M50 &#124; O'Regan2022 characterization and model](lg-m50-oregan2022.md) | [2 reused expressions](../cells/lg-m50-oregan2022.md#ocp-curves) | [43 records](../parameters/lg-m50-oregan2022--diffusion.csv) | [14 records](../parameters/lg-m50-oregan2022--kinetics.csv) | [1 external source](lg-m50-oregan2022.md#full-cell-tests) | multi-T<br>Cross-study / mixed sources · [Match / gaps](lg-m50-oregan2022.md#matching-and-gaps) |
| [LG M50LT &#124; Hallemans2025 grouped SPMe](lg-m50lt-hallemans2025.md) | [Reuse unresolved](../cells/lg-m50lt-hallemans2025.md#ocp-curves) | [2 records (groups)](../parameters/lg-m50lt-hallemans2025--diffusion.csv) | [4 records (groups)](../parameters/lg-m50lt-hallemans2025--kinetics.csv) | [1 packaged + 1 external source](lg-m50lt-hallemans2025.md#full-cell-tests) | dynamic, EIS<br>same model same study · [Match / gaps](lg-m50lt-hallemans2025.md#matching-and-gaps) |
| [LG MJ1 &#124; DLR-SINTEF harvested-electrode characterization](lg-mj1-dlr-sintef.md) | [4 pseudo-OCP](../cells/lg-mj1-dlr-sintef.md#ocp-curves) | [18 records](../parameters/lg-mj1-dlr-sintef--diffusion.csv) | [6 records](../parameters/lg-mj1-dlr-sintef--kinetics.csv) | [1 external source](lg-mj1-dlr-sintef.md#full-cell-tests) | dynamic, ageing<br>Cross-study / mixed sources · [Match / gaps](lg-mj1-dlr-sintef.md#matching-and-gaps) |
| [UMBL Mohtat2020 &#124; 5 Ah NMC/graphite research pouch](mohtat2020-nmc532-pouch.md) | [4 expressions](../cells/mohtat2020-nmc532-pouch.md#ocp-curves) | [9 records](../parameters/mohtat2020-nmc532-pouch--diffusion.csv) | [12 records](../parameters/mohtat2020-nmc532-pouch--kinetics.csv) | [5 packaged](mohtat2020-nmc532-pouch.md#full-cell-tests) | See test conditions / gaps<br>same study cell family · [Match / gaps](mohtat2020-nmc532-pouch.md#matching-and-gaps) |

## NCA

| Battery / study | OCP | Diffusion | Kinetics | Full-cell tests | Coverage / matching |
|---|---|---|---|---|---|
| [Panasonic NCR18650B &#124; HNEI2016](panasonic-ncr18650b-hnei2016.md) | [4 pseudo-OCP](../cells/panasonic-ncr18650b-hnei2016.md#ocp-curves) | Not extracted | Not extracted | [4 external sources](panasonic-ncr18650b-hnei2016.md#full-cell-tests) | multi-T, dynamic, ageing, EIS<br>Cross-study / mixed sources · [Match / gaps](panasonic-ncr18650b-hnei2016.md#matching-and-gaps) |
| [Molicel P45B &#124; About:Energy2026 BPX](molicel-p45b-aboutenergy2026.md) | [5 tables / fits](../cells/molicel-p45b-aboutenergy2026.md#ocp-curves) | [7 records](../parameters/molicel-p45b-aboutenergy2026--diffusion.csv) | [8 records](../parameters/molicel-p45b-aboutenergy2026--kinetics.csv) | [2 external sources](molicel-p45b-aboutenergy2026.md#full-cell-tests) | multi-T, dynamic, ageing<br>same model same study · [Match / gaps](molicel-p45b-aboutenergy2026.md#matching-and-gaps) |
| [Molicel P45B &#124; TUM Rehm2026 measured half-cells](molicel-p45b-tum-rehm2026.md) | [5 pseudo-OCP](../cells/molicel-p45b-tum-rehm2026.md#ocp-curves) | Not extracted | Not extracted | [1 external source](molicel-p45b-tum-rehm2026.md#full-cell-tests) | ageing<br>same model same study · [Match / gaps](molicel-p45b-tum-rehm2026.md#matching-and-gaps) |
| [NCA_Kim2011 &#124; NCA/graphite &#124; 0.43 Ah model input](kim2011-nca-nominal-design.md) | [2 expressions](../cells/kim2011-nca-nominal-design.md#ocp-curves) | [6 records](../parameters/kim2011-nca-nominal-design--diffusion.csv) | [7 records](../parameters/kim2011-nca-nominal-design--kinetics.csv) | [Not linked](kim2011-nca-nominal-design.md#full-cell-tests) | See test conditions / gaps<br>unmatched · [Match / gaps](kim2011-nca-nominal-design.md#matching-and-gaps) |

## LCO

| Battery / study | OCP | Diffusion | Kinetics | Full-cell tests | Coverage / matching |
|---|---|---|---|---|---|
| [Enertech &#124; LCO/graphite &#124; 2.28 Ah model input](enertech-lco-pouch-ai2020.md) | [2 tables / fits](../cells/enertech-lco-pouch-ai2020.md#ocp-curves) | [6 records](../parameters/enertech-lco-pouch-ai2020--diffusion.csv) | [7 records](../parameters/enertech-lco-pouch-ai2020--kinetics.csv) | [4 packaged](enertech-lco-pouch-ai2020.md#full-cell-tests) | See test conditions / gaps<br>same study cell family · [Match / gaps](enertech-lco-pouch-ai2020.md#matching-and-gaps) |
| [SLPB78205130H &#124; LCO/graphite &#124; 0.680616 Ah model input](kokam-slpb78205130h-marquis2019.md) | [2 expressions](../cells/kokam-slpb78205130h-marquis2019.md#ocp-curves) | [6 records](../parameters/kokam-slpb78205130h-marquis2019--diffusion.csv) | [7 records](../parameters/kokam-slpb78205130h-marquis2019--kinetics.csv) | [Not linked](kokam-slpb78205130h-marquis2019.md#full-cell-tests) | See test conditions / gaps<br>parameter set only · [Match / gaps](kokam-slpb78205130h-marquis2019.md#matching-and-gaps) |

## NCO

| Battery / study | OCP | Diffusion | Kinetics | Full-cell tests | Coverage / matching |
|---|---|---|---|---|---|
| [Kokam SLPB75106100 &#124; 7.5 Ah NCO/graphite](kokam-slpb75106100-ecker2015.md) | [2 expressions](../cells/kokam-slpb75106100-ecker2015.md#ocp-curves) | [6 records](../parameters/kokam-slpb75106100-ecker2015--diffusion.csv) | [6 records](../parameters/kokam-slpb75106100-ecker2015--kinetics.csv) | [2 packaged](kokam-slpb75106100-ecker2015.md#full-cell-tests) | See test conditions / gaps<br>same model same study · [Match / gaps](kokam-slpb75106100-ecker2015.md#matching-and-gaps) |

Material-only curves without a verified battery model remain in [the OCP material index](../ocp/README.md); no commercial-cell assignment is inferred.
