# Using the E-BatP local viewer

The viewer is a local interface to the electrochemical model parameter catalog.
It does not publish the repository or fetch external test payloads. Website
files are generated from `src/ebp/web/` and the canonical catalog; the source
HTML template alone does not include the catalog or downloads.

## Follow a parameter package

1. Select a material family and cell/study in **Cell packages**.
2. Use **Electrode OCP** buttons to inspect that cell's stored curves. The curve
   detail links back to its parameter package. Material-only measurements remain
   searchable without assigning them to a commercial cell.
3. Search parameter names, definitions or units, and combine category and model
   variant filters. **Export filtered CSV** retains the selected source values,
   expressions/table references, units, conditions, origin and license. It does
   not combine model variants or fit new parameters. Native parameter tables
   remain separate downloads from the parameter detail.
4. Open **Linked external test sources** to inspect associated file/container
   locations and matching gaps. The source filter uses explicit parameter-cell
   links. A common chemistry or cell name does not imply identical specimens.

For example, HAIDI links seven native pseudo-OCP branches to its same-study
external references. M50LT has grouped diffusion/kinetics but no admitted OCP;
that gap stays visible. NCR18650B links HNEI OCP with separately labeled
cross-study full-cell sources.

## Inspect a plot

Move the pointer or tap a plot to inspect its preview coordinates. Focus the
chart and use left/right arrows, Home or End; Escape clears the readout.
Values are the nearest sampled **preview** points, not newly estimated
measurements. Readouts do not extrapolate beyond a curve's displayed domain.
CSV downloads retain native table points or explicitly sampled analytical
expressions, as labeled. OCP and full-cell coordinates keep their own definitions.

## Keep a view

**Copy current view link** records the selected cell, OCP, comparisons, filters,
parameter variant and retained test selection in the URL. If clipboard access is
unavailable, select and copy the displayed link manually. A local link works
only where its local files are available; it does not grant repository access
or upload any data.

## Repository and maintainer

The header and footer link to the GitHub repository. GitHub sign-in and repository
permission may be required while it remains private. **About Feng** contains the
maintainer introduction, email, Google Scholar, academic homepage and related
research projects. Links open their original providers; no background tracking,
remote fonts or third-party chart libraries are added.

## Rebuild safely

```bash
ebp build-site --output site
```

The builder writes `.ebp-site-files.json` to track generated files. A later build
removes obsolete generated files only if their bytes still match that manifest.
Unmanaged files and edited obsolete files are preserved. Work on source files
under `src/ebp/web/`; generated output can be regenerated.

## Verification boundaries

The focused checks cover pure filter/export/link/readout logic, site generation,
internal asset/download targets, and preservation of source payloads. They do not
certify that every external provider is reachable. Browser visual and click
checks require a permitted HTTP/HTTPS page; source/static checks alone do not
establish that the rendered browser interaction has passed.
