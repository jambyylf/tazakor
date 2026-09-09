# Инструкции для тестирования

Панельдегі «Инструкции для тестирования» өрісіне қойылатын мәтін. Міндетті
емес, бірақ форк болғандықтан толтырған дұрыс: модератор кеңейтімнің неге
uBlock Origin Lite-қа ұқсайтынын және оның заңды екенін бірден түсінеді.

Ағылшынша, өйткені модераторлар сол тілде оқиды.

> **Өрістің шегі — 500 таңба.** Сондықтан екі нұсқа бар: панельге
> қойылатын қысқасы және толық нұсқасы. Толығы бұл жерде анықтама
> ретінде сақталады, әрі оны GitHub-тағы issue-де немесе модератор
> сұраса, жауап ретінде пайдалануға болады.

---

## Панельге қойылатын қысқа нұсқа (500 таңбаға дейін)

```
Fork of uBlock Origin Lite (GPLv3), rebranded for Kazakhstan. LICENSE.txt and copyright headers preserved. Upstream: github.com/gorhill/uBlock

IMPORTANT: the UI opens in Kazakh. Chrome has no Kazakh locale, so the extension manages its own language. To review in English: options page > Settings > "Интерфейс тілі" > English.

Default mode is "complete", hence the all-sites permission; "basic" stops all page access.

Build steps: README.md in the package. Source: github.com/jambyylf/tazakor
```

---

## Толық нұсқа (анықтама үшін)

```
WHAT THIS EXTENSION IS

TazaKor is a rebranded fork of uBlock Origin Lite (MV3) by Raymond Hill,
adapted for users in Kazakhstan. The upstream project is licensed under
GPLv3, which permits redistribution of modified versions under the same
license.

The unmodified GPLv3 text ships as LICENSE.txt inside the package, all
copyright headers in the source files are preserved, and the store listing
states prominently that this is a fork and not uBlock Origin.

Upstream: https://github.com/gorhill/uBlock
This fork: https://github.com/jambyylf/tazakor

THE INTERFACE OPENS IN KAZAKH

This will look unusual, so please read this note first.

Chrome does not support Kazakh as a browser interface language: there is no
kk locale in Chrome's own Locales directory, so chrome.i18n never returns
"kk" and a _locales/kk folder is ignored. Because the whole point of this
extension is to serve Kazakh speakers, it manages its own interface
language instead of following the browser.

To review the UI in English: open the extension's options page, find
"Интерфейс тілі" (Interface language) in the Settings pane, and choose
English. The page reloads in English.

The implementation is in js/i18n.js. It replaces chrome.i18n.getMessage
with a function that reads messages from the selected locale file inside
the package. Nothing is fetched from the network for this.

HOW TO REPRODUCE THE BUILD

The package includes README.md with exact steps. In short:

    git clone https://github.com/jambyylf/tazakor.git
    cd tazakor
    git checkout v1.0.0
    git submodule init && git submodule update
    mkdir -p dist/build/mv3-data
    bash tools/make-mv3.sh chromium 1.0.0
    python tools/make-store-zip.py

Note: rulesets/*.json are generated from filter lists fetched at build
time, so a rebuild on a later date produces different rule contents. The
rest of the package is byte-reproducible from the tagged commit.

WHAT TO TEST

1. Install and visit any site with ads. Ads are blocked by declarative
   rules; the extension observes no requests itself.
2. Open the options page. The default filtering mode is "complete", which
   is why the extension requests access to all sites. Switch to "basic" and
   the extension stops reading page content entirely.
3. Scriptlet filters require the user to enable "Allow user scripts" in
   chrome://extensions. Without that opt-in they simply do not run.

ABOUT THE REMOTE CODE DECLARATION

Declared as Yes, deliberately. By default nothing is fetched. If a user
adds an external filter list by URL in the settings, cosmetic filters from
that list are compiled into a script registered via chrome.userScripts as
a code string. That script runs in the isolated USER_SCRIPT world, only on
hostnames the filters specify, and only if the user enabled user scripts.
Network filters from such a list never become code; they become declarative
rules handled by the browser.

CHANGES FROM UPSTREAM

Rebranding (name, icons, UI strings), a fully revised Kazakh translation
with an in-extension language switcher, default filtering mode changed from
optimal to complete, an optional and currently empty Kazakhstan filter list,
removal of three regional lists whose host is unreachable from Kazakhstan,
and a weekly upstream-sync workflow. The filtering engine itself is
unchanged.
```
