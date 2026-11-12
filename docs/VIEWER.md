# Using the E-BatP local viewer

The viewer is a local interface to the electrochemical model parameter catalog.
It does not publish the repository or fetch external test payloads. Website
files are generated from `src/ebp/web/` and the canonical catalog; the source
HTML template alone does not include the catalog or downloads.

## Follow a parameter package

1. Start in **Cell explorer**. Search for a model or study, optionally narrow by
   material family, and choose a matching package. Searching narrows the options
   without silently changing the selected package. Press Enter to open a single
   match or focus the results selector when several match.
2. Switch between **Parameters**, **OCP**, **Experiments**, and **Evidence** in
   the package. Use the left/right arrow keys, Home or End to move between tabs.
   Parameter filters, the selected curve, and the stored trace are remembered
   for each cell while you explore other packages.
3. In **Parameters**, search names, definitions or units, and combine category
   and model variant filters. The export button states how many matching rows
   will be saved. The CSV retains source values, expressions/table references,
   units, conditions, origin and license. Use **Package downloads** for the
   whole package or the row detail for a native parameter table.
4. In **OCP**, choose a curve to plot it and download its data without leaving
   the package. **Add to OCP comparison** adds the curve to the cross-study
   comparison, where selections stay in place as you change the filters.
   Material-only studies remain searchable in the comparison library.
5. In **Experiments**, inspect stored full-cell traces and expand linked test
   sources for file/container locations. The **Evidence** tab explains the
   matching limits. A common chemistry or cell name does not establish an
   identical specimen.

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

**Copy current view link** records the selected cell and tab, OCP, comparisons,
filters, parameter variant and retained test selection in the URL. If clipboard access is
unavailable, select and copy the displayed link manually. A local link works
only where its local files are available; it does not grant repository access
or upload any data.

## Repository and maintainer

The header and footer link to the GitHub repository. Sign in to GitHub to
submit issues or pull requests. **About Feng** contains the
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
