# Рұқсаттардың негіздемесі

Chrome Web Store әр рұқсат үшін негіздеме сұрайды. Төмендегі мәтіндер
«Privacy practices» бөліміне ағылшынша көшіріледі, себебі модераторлар
сол тілде оқиды. Қазақша түсіндірмесі жақшада берілген.

---

## Single purpose (панельдегі бірінші өріс)

```
Blocking advertising, tracking and cryptomining requests on web pages.

Every capability the extension requests exists to serve that one purpose:
declarative rules block the requests, cosmetic filtering hides the elements
that remain, and storage keeps the user's own filtering preferences.
```

*Кеңейтімнің жалғыз мақсаты: беттердегі жарнаманы, трекерлерді және
майнерлерді бұғаттау.*

---

## declarativeNetRequest

```
Core functionality. The extension blocks advertising and tracking requests
using declarative rulesets that are bundled with the package. No requests
are observed or intercepted by extension code; blocking is performed by the
browser itself.
```

*Негізгі функция. Жарнама мен трекерлерді бұғаттау осы арқылы істейді.*

## storage

```
Stores the user's settings: the default filtering mode, per-site filtering
modes, which filter lists are enabled, and custom filters written by the
user. All data stays in local browser storage and is never transmitted.
```

*Қолданушының баптауларын сақтау үшін.*

## unlimitedStorage

```
Compiled filter data and per-site settings can exceed the default 5 MB
quota when many filter lists are enabled. Without this permission the
extension would fail to save its state for users with large lists.
```

*Сүзгі деректері әдепкі 5 МБ шектеуден асуы мүмкін.*

## scripting

```
Injects cosmetic filtering code into pages to hide advertising placeholders
that remain after network blocking. Used only in the optimal and complete
filtering modes, and only on sites the user has granted access to.
```

*Беттегі жарнама орындарын жасыру үшін.*

## activeTab

```
Used when the user opens the popup and activates the element picker or the
element zapper. Grants temporary access to the current tab only, at the
moment the user clicks the button.
```

*Қолданушы элементті қолмен жасыру құралын ашқанда ғана керек.*

## userScripts

```
Executes scriptlet filters, which neutralise anti-adblock scripts and
similar page behaviour. This capability is off by default and requires an
explicit opt-in by the user: on Chrome 138 and later via the per-extension
"Allow user scripts" toggle, and on earlier versions by enabling Developer
mode. If the user does not opt in, scriptlet filters simply do not run; the
rest of the extension is unaffected.
```

*Скриптлет сүзгілерін орындау үшін. Әдепкіде сөндірулі.*

## offscreen

```
Compiles filter lists into cosmetic filtering data in an offscreen
document. Filter compilation requires DOM APIs that are not available in a
service worker.
```

*Сүзгілерді өңдеу үшін. Service worker-де қажетті API жоқ.*

## alarms

```
Schedules deferred maintenance work, such as re-registering content scripts
after the browser restarts the extension's service worker.
```

*Кейінге қалдырылған қызметтік тапсырмаларды жоспарлау үшін.*

---

## host_permissions: `<all_urls>`

```
The complete filtering mode, which is the default, needs to read and modify
page content on every site the user visits in order to hide advertising
elements that network-level blocking cannot remove.

The extension does not collect, store or transmit any browsing data. Page
access is used solely to apply cosmetic filtering rules locally, inside the
user's browser.

Because complete filtering is the default, this access is granted at
installation and Chrome shows "Read and change all your data on all
websites". Users who prefer less access can narrow site access at any time
from chrome://extensions. When broad access is not available the extension
automatically falls back to basic filtering, which uses declarative rules
only and reads no page content.
```

*Толық режим барлық сайттағы мазмұнды өзгертуді талап етеді. Рұқсат
берілмесе, кеңейтім автоматты түрде негізгі режимге түседі.*

---

## Remote code декларациясы

Панельдегі сұрақ: «Are you using remote code?»

Ұсынылатын жауап: **Иә**, содан соң төмендегі түсіндірме. «Жоқ» деп жауап
беру де қисынды, себебі жүктелетін файл орындалатын код емес, дерек. Бірақ
модератор оны басқаша бағалауы мүмкін, ал жалған «жоқ» саясат бұзушылығы
болып саналады. Ашық түсіндіріп, «иә» деген қауіпсіздеу.

```
Yes, with an important qualification.

All executable code ships inside the package. Every scriptlet body, every
content script and the entire filtering engine are bundled; nothing
executable is fetched at runtime.

The qualification: a user may optionally add an external filter list by
URL. The extension then downloads that file, and while the list stays
enabled it refreshes it periodically (roughly every seven days by default).

That downloaded file is filter-list text, not script. It is parsed into
declarative net-request rules, CSS selectors, and string arguments passed
to scriptlets that are already present in the package. Downloaded content
is never evaluated as code.

No external list is configured out of the box, so a default installation
fetches nothing at all.
```

*Пакетте орындалатын кодтың бәрі дайын тұр. Қолданушы өзі қосқан сүзгі
тізімі ғана жүктеледі, ал ол код емес, дерек. Әдепкі күйде ешқандай сыртқы
тізім жоқ.*

---

## Деректерді пайдалану туралы декларация

Chrome Web Store «Data usage» бөлімінде **ешбір** санатты белгілемеу керек.
Кеңейтім дербес деректі, орналасқан жерді, шолу тарихын, әрекеттерді және
басқа да ешнәрсені жинамайды.

Үш мәлімдемеге де келісу керек:

- Деректер үшінші тарапқа сатылмайды
- Деректер кеңейтімнің негізгі функциясына қатысы жоқ мақсатта
  пайдаланылмайды
- Деректер несиеқабілеттілікті анықтау немесе несие беру үшін
  пайдаланылмайды
