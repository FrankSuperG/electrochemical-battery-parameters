# Half-cell OCP data (graphite anode / NMC532 cathode)

[Back to the dataset overview](../../DataOverview.md).

Electrode samples were harvested from the pristine full cell `Cell_96` (see the
[teardown-image documentation](../../1_Teardown/Teardown_images/README_teardown_images.md)),
punched as 15 mm coins and assembled into 2032 coin cells
against a lithium chip (half-cell configuration) with a polypropylene
separator and 500 uL LP30 electrolyte (1 M LiPF6 in EC:DMC, 1:1 v/v). Note
the separator and electrolyte do not exactly match those of the full cell.
The half-cells were cycled outside the glovebox to obtain the electrode
Open-Circuit Potentials (OCPs).

## Files

| Folder | File | Content |
|---|---|---|
| `Anode_Graphite/` | `NEXTMBS-full-charge-discharge-GITT-full0charge-discharge-NMC-anode.csv` | Full slow cycle + charge/discharge GITT raw time series |
| `Anode_Graphite/` | `anode_NExtBMS_fCharge.csv`, `anode_NExtBMS_fDischarge.csv` | Slow full charge / discharge sweeps. Columns: `Capacity(mAh/g)` (specific capacity), `Voltage(V)` |
| `Anode_Graphite/` | `Sample_image_GITT_graphite-anode-Akzhan.B.jpg` | Sample photo |
| `Cathode_NMC532/` | `NEXTMBS-full-charge-discharge-GITT-full0charge-discharge-NMC-cathode.csv` | Full slow cycle + charge/discharge GITT raw time series |
| `Cathode_NMC532/` | `cathode_NExtBMS_fCharge.csv`, `cathode_NExtBMS_fDischarge.csv` | Slow full charge / discharge sweeps. Columns: `Capacity(mAh/g)`, `Voltage(V)` |
| `Cathode_NMC532/` | `Sample image GITT NMC-Akzhan B.jpg` | Sample photo |

To convert the slow-sweep specific capacity [mAh/g] to absolute capacity
[mAh], multiply by the active-material mass of the coin sample:
**cathode 0.03553 g, anode 0.01668 g**.

## GITT protocol - NMC532 cathode (2.8-4.4 V vs Li/Li+)

| Step | C-rate | Pulse time | Cycles | Rest |
|---|---|---|---|---|
| Full charge (conditioning) | C/20 | 19.74 h | - | 1 min |
| Full discharge (conditioning) | C/20 | 18.43 h | - | 1 min |
| Charge titration | C/50 | 2.5 h | 5 | 20 h |
| Charge titration | C/20 | 1 h | 14 | 5 h |
| Discharge titration | C/20 | 1 h | 14 | 5 h |
| Discharge titration | C/50 | 2.5 h | 6 | 20 h |

## GITT protocol - graphite anode (0.01-1.5 V vs Li/Li+)

One preceding full cycle was performed between 0.01 and 2 V vs Li/Li+.
The titration is segmented by specific capacity because the graphite
voltage plateaus require finer resolution at the ends of the window:

| Step | C-rate | Pulse time | Cycles | Rest |
|---|---|---|---|---|
| Full charge (conditioning) | C/20 | 19.6 h | - | 1 min |
| Full discharge (conditioning) | C/20 | 19.73 h | - | 1 min |
| Charge 0-112.4 mAh/g | C/20 | 50 min | 9 | 10 h |
| Charge 112.4-162.4 mAh/g | C/20 | 20 min | 10 | 20 h |
| Charge 162.4-212.4 mAh/g | C/20 | 20 min | 10 | 10 h |
| Charge 212.4-294.8 mAh/g | C/50 | 1.25 h | 11 | 20 h |
| Discharge 0-75 mAh/g | C/50 | 1.25 h | 10 | 20 h |
| Discharge 75-125 mAh/g | C/20 | 20 min | 10 | 10 h |
| Discharge 125-175 mAh/g | C/20 | 20 min | 10 | 20 h |
| Discharge 175-300 mAh/g | C/20 | 50 min | 10 | 10 h |

"Charge" here means delithiation for the cathode and lithiation windows as
per the file naming; in the analysis code and paper figures, red = charge
by delithiation and black = discharge by lithiation.

## Processing

The GITT CSVs are processed by `extractOCPLines.m` in the
[analysis-code repository](https://github.com/robinson-medina/Analsys_Of_NMC_Dataset)
into the anode/cathode OCP publication figures; the relaxation end points of
each pulse provide the OCP-vs-capacity curves.
