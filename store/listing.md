# Chrome Web Store — тізімдеме мәтіндері

Бұл файлдағы мәтіндерді Chrome Web Store әзірлеуші панеліне көшіріп қою керек.
Таңбалар саны Google қоятын шектеуге сай тексерілген.

> **Маңызды.** Дүкен қысқа сипаттама ретінде манифесттегі `extShortDesc`
> мәнін көрсетеді, төмендегі «Қысқа сипаттама» блоктары емес. Екеуі бірдей
> болуы үшін мәтіндер `_locales/{kk,ru,en}/messages.json` файлдарымен
> синхрондалған. Біреуін өзгертсеңіз, екіншісін де өзгертіңіз.

---

## Атауы (75 таңбаға дейін)

Атау локаль файлдарындағы `extName` мәнінен келеді, сондықтан үш тілде де
бөлек.

### Қазақша
```
ТазаКөр — жарнамасыз интернет
```

### Орысша
```
ТазаКөр — интернет без рекламы
```

### Ағылшынша
```
TazaKor — ad-free internet
```

---

## Қысқа сипаттама (132 таңбаға дейін)

Форк екені осы жерде айтылады, себебі іздеу нәтижесінде және орнату
терезесінде тек осы жол көрінеді.

### Қазақша
```
Жарнаманы, трекерлерді және майнерлерді бұғаттайды. uBlock Origin Lite ашық кодына негізделген тәуелсіз форк.
```

### Орысша
```
Блокирует рекламу, трекеры и майнеры. Независимый форк открытого кода uBlock Origin Lite.
```

### Ағылшынша
```
Blocks ads, trackers and miners. An independent fork of the open-source uBlock Origin Lite.
```

---

## Толық сипаттама

### Қазақша

```
ТазаКөр — Raymond Hill жазған uBlock Origin Lite жобасының ашық кодына
негізделген тәуелсіз форк. Бұл uBlock Origin ЕМЕС. Түпнұсқа жобаның авторы
бұл кеңейтімге қатысы жоқ және оны қолдамайды.

ТазаКөр веб-беттердегі жарнаманы, бақылау трекерлерін және жасырын
майнерлерді бұғаттайды. Қазақстандағы қолданушыларға арналған, интерфейсі
толықтай қазақ тілінде.

НЕГІЗГІ МҮМКІНДІКТЕР

• Жарнама, трекер және майнер бұғаттау
• Толықтай қазақ тілді интерфейс, орыс және ағылшын тілдері де бар
• Үш сүзгілеу режимі: негізгі, оңтайлы және толық
• Әр сайт үшін бөлек режим таңдау мүмкіндігі
• Қалқымалы терезелерді бұғаттау
• Қатаң бұғаттау: сүзгі тізімдерінде белгіленген сайттар ашылмас бұрын
  ескерту беріледі
• Бетте қалып қойған элементті қолмен жасыру құралы
• Өз сүзгіңізді жазу мүмкіндігі

СҮЗГІЛЕУ РЕЖИМДЕРІ

Негізгі: тек желілік сұраныстарды бұғаттайды, беттегі деректі оқымайды.

Оңтайлы: желілік бұғаттауға қоса, беттегі жарнама орындарын жасырады.

Толық: барлық сайттарға рұқсат берілген жағдайда әдепкіде осы режим
таңдалады. Рұқсат берілмесе, кеңейтім негізгі режимде жұмыс істейді.

Кеңейтім орнатылғанда браузер барлық сайттарға рұқсат сұрайды, себебі
әдепкі режим толық. Рұқсатты chrome://extensions бетінен кез келген уақытта
тарылтуға болады.

ҚҰПИЯЛЫҚ

Кеңейтімнің сервері жоқ. Ол сізге қатысты дерек жинамайды және әзірлеушіге
ештеңе жібермейді. Талдау жүйелері мен жарнама желілері қолданылмайды.

Толық саясат: https://github.com/jambyylf/tazakor/blob/brand/store/privacy-policy.md

АШЫҚ БАСТАПҚЫ КОД

Бүкіл код ашық: https://github.com/jambyylf/tazakor
Лицензиясы: GNU General Public License v3.0

Түпнұсқа жоба: https://github.com/gorhill/uBlock
Кеңейтімге қатысты мәселелерді түпнұсқа жобаға емес, жоғарыдағы
репозиторийге жазыңыз.
```

### Орысша

```
ТазаКөр — независимый форк открытого кода uBlock Origin Lite, автором
которого является Raymond Hill. Это НЕ uBlock Origin. Автор оригинального
проекта не имеет отношения к этому расширению и не поддерживает его.

ТазаКөр блокирует рекламу, трекеры слежки и скрытые майнеры на веб-страницах.
Создано для пользователей в Казахстане, интерфейс доступен на казахском и
русском языках.

ОСНОВНЫЕ ВОЗМОЖНОСТИ

• Блокировка рекламы, трекеров и майнеров
• Интерфейс на казахском, русском и английском языках
• Три режима фильтрации: базовый, оптимальный и полный
• Отдельный режим для каждого сайта
• Блокировка всплывающих окон
• Строгая блокировка: предупреждение перед открытием сайтов, отмеченных в
  списках фильтров
• Инструмент для скрытия оставшихся элементов вручную
• Возможность писать собственные фильтры

РЕЖИМЫ ФИЛЬТРАЦИИ

Базовый: блокирует только сетевые запросы, не читает содержимое страниц.

Оптимальный: дополнительно скрывает рекламные блоки на странице.

Полный: выбирается по умолчанию, если предоставлен доступ ко всем сайтам.
Без такого доступа расширение работает в базовом режиме.

При установке браузер запрашивает доступ ко всем сайтам, поскольку режим по
умолчанию полный. Доступ можно ограничить на странице chrome://extensions.

КОНФИДЕНЦИАЛЬНОСТЬ

У расширения нет сервера. Оно не собирает данные о вас и ничего не отправляет
разработчику. Аналитика и рекламные сети не используются.

Полная политика: https://github.com/jambyylf/tazakor/blob/brand/store/privacy-policy.md

ОТКРЫТЫЙ ИСХОДНЫЙ КОД

Весь код открыт: https://github.com/jambyylf/tazakor
Лицензия: GNU General Public License v3.0

Оригинальный проект: https://github.com/gorhill/uBlock
Сообщения о проблемах направляйте не в оригинальный проект, а в репозиторий
выше.
```

### Ағылшынша

```
TazaKor is an independent fork of the open-source uBlock Origin Lite by
Raymond Hill. This is NOT uBlock Origin. The author of the original project
is not affiliated with this extension and does not endorse it.

TazaKor blocks ads, tracking scripts and hidden miners on web pages. It is
built for users in Kazakhstan and ships with a complete Kazakh interface.

FEATURES

• Blocks ads, trackers and miners
• Interface in Kazakh, Russian and English
• Three filtering modes: basic, optimal and complete
• Per-site filtering mode
• Pop-up blocking
• Strict blocking: warns before opening sites flagged by the enabled filter
  lists
• Element picker for hiding leftovers by hand
• Support for your own custom filters

FILTERING MODES

Basic blocks network requests only and does not read page content.

Optimal additionally hides ad placeholders on the page.

Complete is selected by default when access to all sites has been granted.
Without that access the extension runs in basic mode.

At installation the browser asks for access to all sites, because the default
mode is complete. Access can be narrowed from chrome://extensions at any time.

PRIVACY

The extension has no server. It collects nothing about you and sends nothing
to the developer. No analytics, no ad networks.

Full policy: https://github.com/jambyylf/tazakor/blob/brand/store/privacy-policy.md

OPEN SOURCE

Full source code: https://github.com/jambyylf/tazakor
License: GNU General Public License v3.0

Upstream project: https://github.com/gorhill/uBlock
Please report issues to the repository above, not to the upstream project.
```

---

## Санат және тіл

- Санат: **Защита и безопасность** (Privacy & Security). Жарнама мен
  трекерлерді бұғаттайтын құрал үшін Productivity-ден дәлірек, әрі
  «жалғыз мақсат» мәлімдемесімен үйлеседі.
- Негізгі тіл: манифесттегі `default_locale` бойынша **english – en**.
  Панельде қазақша мен орысшаны қосымша локаль ретінде қосамыз.

## Скриншоттар туралы

Панельде екі бөлек өріс бар, екеуі де міндетті:

- **Локализованные скриншоты** — әр тіл үшін бөлек
- **Глобальные скриншоты** — тілі сәйкес келмегенде көрсетілетін жиын

Екеуіне де `screenshots/` ішіндегі бірдей төрт файлды жүктеу жеткілікті.
