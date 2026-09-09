# ТазаКөр

**ТазаКөр** — Қазақстанға арналған, қазақ тілді интерфейсі бар жарнама
бұғаттаушы Chrome кеңейтімі.

> ### ⚠️ Бұл — форк
>
> Бұл жоба [gorhill/uBlock](https://github.com/gorhill/uBlock) репозиторийіндегі
> **uBlock Origin Lite** (uBOL) кеңейтімінің өзгертілген нұсқасы.
>
> Бұл **uBlock Origin емес**. Түпнұсқаның авторы Raymond Hill бұл фаркқа
> қатысы жоқ, оны қолдамайды және жауап бермейді. Кеңейтімге қатысты
> мәселелерді түпнұсқа жобаға емес, осы репозиторийге жазыңыз.
>
> Репозиторий: <https://github.com/jambyylf/tazakor>
>
> Базалық нұсқа: [`2cf4466`](https://github.com/gorhill/uBlock/commit/2cf4466da8f5b7ffce3b98698568330cdab94ff6)
> (2026-09-07)

---

## Лицензия

**GNU General Public License v3.0 (GPLv3).**

Түпнұсқа жоба GPLv3 бойынша таратылады, сондықтан бұл форк та сол лицензиямен
таратылады. Толық мәтін өзгертілмеген күйінде [LICENSE.txt](LICENSE.txt)
файлында тұр.

Бастапқы код: <https://github.com/gorhill/uBlock>
Авторлық құқық: Copyright (C) 2014-present Raymond Hill

GPLv3 талабы бойынша барлық өзгерістер төменде ашық көрсетілген. Бастапқы
кодтағы авторлық құқық туралы түсініктемелер мен лицензия файлы тиілмеген.

---

## Не өзгертілді

### Брендинг

- Кеңейтімнің атауы, қысқа атауы және авторы `manifest.json` файлдарында
  ауыстырылды (Chrome, Firefox, Safari).
- Таңбашалар мен логотип жаңасына ауыстырылды. Логотип таза SVG түрінде,
  [`assets/brand/`](assets/brand/) папкасында, оны қайта құратын скриптімен бірге.
- Интерфейстегі «uBlock», «uBO», «uBOL» сөздері жаңа атауға ауыстырылды.
  Барлығы 71 локальда 632 жол өзгерді.
- Лицензия файлы мен код ішіндегі авторлық түсініктемелер **тиілмеді**.

### Қазақ тілі

- Қазақ локалі толық аударылды, ағылшынша қалған жол жоқ.
- **Кеңейтімнің өз тіл ауыстырғышы қосылды, әдепкі тіл — қазақша.**
  Chrome-да қазақ тілі мүлдем жоқ: браузердің Locales қалтасында `kk.pak`
  файлы жоқ, сондықтан `chrome.i18n` ешқашан «kk» қайтармайды және
  `_locales/kk` қалтасы үнсіз еленбейді. Сол себепті кеңейтім
  `chrome.i18n.getMessage` әдісін өз бетінде алмастырып, хабарламаларды
  таңдалған тілдің файлынан оқиды. Баптаулардан тілді өзгертуге болады.
  Іске асырылуы: [`platform/mv3/extension/js/i18n.js`](platform/mv3/extension/js/i18n.js),
  ол `src/js/i18n.js` файлының форкі және оны құрастыру кезінде басып жазады.
- Ескерту: манифесттегі атау мен сипаттаманы браузер өзі шешеді, сондықтан
  `chrome://extensions` бетінде кеңейтім браузердің тілінде аталып тұрады.
  Оны кодпен өзгерту мүмкін емес.
- Терминология қайта қаралды. Мысалы «Үнсіз келісім бойынша» дегеннің орнына
  «Әдепкі», «оптималды» орнына «оңтайлы», «блоктау» орнына «бұғаттау».

### Мінез-құлық

- **Әдепкі сүзгілеу режимі «оңтайлы» орнына «толық» етіп қойылды**
  ([`mode-manager.js`](platform/mv3/extension/js/mode-manager.js)).
  Бұл барлық сайттағы деректі оқу рұқсатын талап етеді. Рұқсат берілмесе,
  кеңейтім автоматты түрде «негізгі» режиміне түседі.

### Сүзгі тізімдері

- Қазақстандық сүзгілерге арналған [`filters/kz.txt`](filters/kz.txt) қосылды.
  Қосымша тізім ретінде тіркелген, әдепкіде сөндірулі. Әзірге бос.
  Ереже қосу нұсқаулығы: [`docs/kz-filter-guide.md`](docs/kz-filter-guide.md).
- Үш аймақтық тізім алынып тасталды: үнді, итальян және испан
  (`ind-0`, `ita-0`, `spa-0`). Себебі олар орналасқан сервер Қазақстаннан
  қолжетімсіз, әрі бұл тізімдер жобаның мақсатты аудиториясына қатысы жоқ.

### Құрастыру

- [`tools/make-mv3.sh`](tools/make-mv3.sh) ішіне қадам қосылды: `filters/`
  папкасындағы жергілікті тізімдер құрастыру алдында кэшке көшіріледі.
  Node-тың `fetch` функциясы жергілікті файлды оқи алмайтындықтан керек болды.
- Апталық автоматты синхрондау мен құрастыруға арналған
  [GitHub Actions workflow](.github/workflows/tazakor-sync.yml) қосылды.

---

## Не өзгертілмеді

- `LICENSE.txt` — түпнұсқадағы GPLv3 мәтіні өзгеріссіз.
- Бастапқы кодтағы авторлық құқық туралы түсініктемелер.
- Сүзгілеу қозғалтқышы мен негізгі логика.
- Сүзгі тізімдерінің мазмұны (uAssets, EasyList және басқалары түпнұсқа
  күйінде жүктеледі).

---

## Құрастыру

Талаптар: Node.js 17.5-тен жоғары, `git`, `jq`, `zip`, `bash`.

```bash
git clone https://github.com/jambyylf/tazakor.git
cd tazakor
git checkout brand
git submodule update --init --recursive
mkdir -p dist/build/mv3-data
bash tools/make-mv3.sh chromium
```

Нәтиже: `dist/build/uBOLite.chromium/`

Chrome-ға орнату:

1. `chrome://extensions` бетін ашыңыз.
2. **Developer mode** қосқышын қосыңыз.
3. **Load unpacked** түймесін басып, жоғарыдағы папканы таңдаңыз.
4. **Details** ішінен **Site access** мәні **On all sites** екенін тексеріңіз.

---

## Өз сүзгіңізді қосу

Ережелерді [`filters/kz.txt`](filters/kz.txt) файлына жазып, қайта
құрастырыңыз. Синтаксис нұсқаулығы: [`docs/kz-filter-guide.md`](docs/kz-filter-guide.md).

---

## Алғыс

Бұл жоба Raymond Hill (@gorhill) және uBlock Origin қауымдастығының
көпжылдық еңбегіне негізделген. Сүзгі тізімдерін
[uAssets](https://github.com/uBlockOrigin/uAssets), EasyList және
басқа да ашық жобалардың авторлары жасайды.

---

## English summary

**TazaKor** is a Kazakh-language fork of
[uBlock Origin Lite](https://github.com/gorhill/uBlock) (MV3), targeted at
users in Kazakhstan.

This is **not** uBlock Origin and is **not** affiliated with or endorsed by
Raymond Hill. Please do not report issues with this fork to the upstream
project.

Licensed under **GPLv3**, same as the original. The license text in
[LICENSE.txt](LICENSE.txt) is unmodified, and copyright headers in source
files are preserved.

Changes from upstream: rebranding (name, icons, UI strings across 71 locales),
a fully revised Kazakh translation, default filtering mode changed from
*optimal* to *complete*, an optional Kazakhstan filter list, removal of three
regional lists whose host is unreachable from Kazakhstan, a build step for
local filter lists, and a weekly upstream-sync workflow. Details are listed
in the Kazakh sections above.
