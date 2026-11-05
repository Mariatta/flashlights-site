# flashlights.app

The project site for [Flashlights](https://github.com/mariatta/flashlights):
what it is, the features, how to try, deploy and adapt it, the changelog and
the blog. A [Popular](https://popular.mariatta.ca) site in its Hugo flavour,
published on GitHub Pages at <https://flashlights.app/>.

The core's own documentation, one version per release, is a separate site at
<https://docs.flashlights.app/>, built from the core repository.

## Working on it

```sh
git clone --recurse-submodules https://github.com/mariatta/flashlights-site.git
cd flashlights-site
hugo server
```

The changelog page mirrors the released sections of the core's `CHANGELOG.md`.
`python scripts/changelog.py` copies them from the newest GitHub release;
the Changelog workflow runs it daily and on demand, and commits the page when
it changed.

The theme is the `themes/popular` submodule, pinned to a release tag. Update
it by checking out a newer tag there and committing the change.

The fonts in `static/fonts/` are copied from the core with their licences:
Bricolage Grotesque for display and Atkinson Hyperlegible Next for text, both
under the SIL Open Font License.
