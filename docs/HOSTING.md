# Using and hosting E-BatP

Hosting is optional. The Python library and local viewer work without publishing
the repository or operating a server. Repository visibility and website access
are separate choices; no deployment integration or public site is configured.

## Three ways to use the project

1. Browse locally with `ebp serve`, choose a cell, inspect component evidence and
   download its **Offline bundle ZIP**. The archive contains scoped CSV/JSON data,
   available original sources and license notices. Blank measurements stay blank.
2. Use `ebp cells` to find stable cell IDs, then `ebp tests --cell CELL_ID` or
   `Catalog.linked_tests(CELL_ID)`. Use `ebp parameters --cell CELL_ID --variant original_author_mpm` for author inputs. Inspect `independent_variable` before plotting:
   the Mohtat charging exports use capacity, while other traces use time.
3. Select an explicit parameter variant for Mohtat. The author model and PyBaMM
   differ; a bundle is an evidence-backed partial collection, not an automatically
   validated complete parameterization. The viewer's Variant selector filters the
   parameter table; each exported parameter retains its variant in conditions.

## Static hosting choices

Checked 2026-10-16. Free-plan limits can change; authoritative links are below.

| Platform | Suitable use / current constraints |
|---|---|
| GitHub Pages | A personal site uses the account's root URL; each separate repository can also have one project site. GitHub Free supports Pages from public repositories; private-repository Pages requires an eligible paid plan. |
| Cloudflare Pages | Recommended for this static catalog when keeping the source repository private. Git integration or direct upload; free plan currently allows 500 builds/month and assets up to 25 MiB each. Keep larger raw files at their original repositories or a separate data archive. |
| Vercel Hobby | Free for personal, non-commercial use; suitable for a static viewer. Check fair-use restrictions before wider organizational use. |
| Netlify Free | Static hosting is available; the current plan has 300 usage credits/month shared by deployments, bandwidth and requests. Data download traffic consumes credits. |

Having a private source repository does not itself make a deployed website
private. Website access must be decided separately before deployment. A provider's
repository connection also needs authorization for that specific repository.

## Prepare a deployable directory

Python 3.12 is recommended. Source reconstruction is a curation task, not a
required deployment step: all curated files are already packaged.

```bash
python -m pip install .
ebp validate
ebp build-site --output site
```

Deploy only the generated `site/` directory. It contains static HTML/JS/CSS,
plots, downloads and notices; no live Python backend or database service is
needed. For a future Cloudflare Git integration, the build command is
`python -m pip install . && ebp build-site --output site`, and the output
directory is `site`. This document configures no deployment and grants no access.

## Official references

- [GitHub Pages site types and plan availability](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)
- [Cloudflare Pages free-plan limits](https://developers.cloudflare.com/pages/platform/limits/)
- [Cloudflare GitHub integration](https://developers.cloudflare.com/pages/configuration/git-integration/github-integration/)
- [Vercel Hobby and non-commercial use](https://vercel.com/docs/plans/hobby)
- [Netlify plans and usage credits](https://www.netlify.com/pricing/)
