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
4. `git checkout brand`
5. `git submodule init`
6. `git submodule update`
7. `mkdir -p dist/build/mv3-data`
8. `bash tools/make-mv3.sh chromium`

The build downloads filter lists from their respective remote servers, then
converts them into declarative rulesets.

Upon completion, the resulting extension package will be present in
`dist/build/uBOLite.chromium`.

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
