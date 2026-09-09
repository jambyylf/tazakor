# How to build TazaKor (MV3)

Instructions for store reviewers.

## About this package

TazaKor is a fork of **uBlock Origin Lite** (MV3) by Raymond Hill, adapted for
users in Kazakhstan. It is licensed under **GPLv3**, the same license as the
original. The unmodified license text ships as `LICENSE.txt` inside this
package.

Upstream project: https://github.com/gorhill/uBlock

This fork differs from upstream in the following ways, all of which affect the
build output:

- Extension name, short name, author, icons and logo are rebranded.
- UI strings referring to the original product name are replaced across all
  71 locales; the Kazakh locale has been fully revised.
- The default filtering mode is **complete** instead of *optimal*
  (`platform/mv3/extension/js/mode-manager.js`).
- An optional, currently empty Kazakhstan filter list (`filters/kz.txt`) is
  registered as ruleset `kz`.
- Three regional rulesets are removed (`ind-0`, `ita-0`, `spa-0`) because their
  host is unreachable from Kazakhstan.
- `tools/make-mv3.sh` copies local filter lists from `filters/` into the build
  cache before generating rulesets.

The filtering engine and all core logic are unchanged from upstream.

## Build steps

The following assumes a Linux environment with `node` (17.5.0 or above),
`git`, `jq`, `zip` and `bash` available.

1. Open a Bash console
2. `git clone https://github.com/jambyylf/tazakor.git`
3. `cd tazakor`
4. `git checkout v1.0.0`   (the exact commit this package was built from)
5. `git submodule init`
6. `git submodule update`
7. `mkdir -p dist/build/mv3-data`
8. `bash tools/make-mv3.sh chromium 1.0.0`
9. `python tools/make-store-zip.py`

Step 8 must be given the version number. Without it the script produces a
local development build: it appends the `declarativeNetRequestFeedback`
permission and keeps `rulesets/debug`, neither of which is present in the
submitted package.

The build downloads filter lists from their respective remote servers, then
converts them into declarative rulesets.

Step 9 produces `dist/tazakor-<version>-chromium.zip`, which is the submitted
artifact. It excludes `log.txt` and verifies that `manifest.json` sits at the
archive root and that no development-only permission survived. The equivalent
without the script is:

    cd dist/build/uBOLite.chromium && zip -r -X ../../tazakor-1.0.0-chromium.zip . -x log.txt

Upon completion, the unpacked extension is in `dist/build/uBOLite.chromium`.

## Reproducibility note

`rulesets/*.json` are generated from filter lists fetched over the network at
build time. Those lists change upstream, so a rebuild on a later date produces
different rule contents and a different rule count. Everything else in the
package is byte-reproducible from the tagged commit.

## Remote code

The extension executes no remote code. All executable code, including every
scriptlet body, ships inside the package. The declarative rulesets are static
JSON produced at build time.

Users may optionally add an external filter list by URL. That downloaded file
is data, not code: it is parsed into declarative rules and into string
arguments for scriptlets that are already bundled. Downloaded content is never
evaluated as script.

## Third-party bundle

`lib/codemirror/cm6.bundle.ubol.min.js` is a minified CodeMirror 6 bundle used
by the in-extension filter editor. It is not obfuscated. It is produced from
the `platform/mv3/extension/lib/codemirror/codemirror-ubol` submodule, which is
pinned in this repository, by running `make ubol.bundle` inside that directory.
The unminified `cm6.bundle.ubol.js` is generated alongside it by the same
command.

## Notes

`dist/build/mv3-data` caches data fetched from remote servers, so repeated
builds do not re-download the same lists. Delete that folder to force a fresh
fetch. Note that `tools/make-mv3.sh` also copies every `filters/*.txt` file
into this cache, named after its ruleset id; those lists are therefore never
fetched from the network.

`dist/build/uBOLite.chromium/log.txt` contains detailed information about what
happened during the build, including any filters that were rejected or could
not be converted to MV3 declarative rules.

`tools/make-mv3.sh [platform]` is the entry point. It copies files from the
uBlock Origin source tree and the MV3-specific tree into a single folder which
becomes the final extension package. It then calls a Node.js script that
converts the filter lists into rulesets.

All final rulesets are present in `dist/build/uBOLite.chromium/rulesets`.
