#!/usr/bin/env python3
"""Chrome Web Store үшін 1280x800 таныстыру суреттерін жасайды.

HTML файлдар құрастырылған кеңейтімнің папкасына жазылады, сонда
кіріктірілген Inter қарпі мен CSS қолжетімді болады.
"""
import json, os, sys

DIR = 'dist/build/uBOLite.chromium'
OUT = 'store/screenshots'


def cards():
    logo = open('assets/brand/tazakor-logo.svg', encoding='utf-8').read()
    logo = logo.replace('id="tazakor"', 'id="tk1"').replace('url(#tazakor)', 'url(#tk1)')
    base = """
<style>
@font-face{font-family:Inter;src:url('css/fonts/Inter/Inter-Regular.woff2') format('woff2');font-weight:400}
@font-face{font-family:Inter;src:url('css/fonts/Inter/Inter-SemiBold.woff2') format('woff2');font-weight:600}
*{box-sizing:border-box;margin:0;padding:0}
body{width:1280px;height:800px;background:#12131F;color:#F3F4F9;
     font-family:Inter,'Segoe UI',system-ui,sans-serif;overflow:hidden;
     display:flex;flex-direction:column;justify-content:center;padding:0 96px}
.logo{width:210px}
.logo svg{width:100%;height:auto;display:block}
h1{font-size:58px;font-weight:600;letter-spacing:-.02em;line-height:1.1}
h2{font-size:40px;font-weight:600;letter-spacing:-.015em;margin-bottom:44px}
p.lead{font-size:25px;color:#9AA0B8;line-height:1.5;max-width:840px}
.grad{background:linear-gradient(-44deg,#14A5F1,#BB5BFA);
      -webkit-background-clip:text;background-clip:text;color:transparent}
ul{list-style:none;display:grid;grid-template-columns:1fr 1fr;gap:26px 52px}
li{font-size:24px;line-height:1.4;padding-left:44px;position:relative;color:#E6E8F2}
li:before{content:'';position:absolute;left:0;top:9px;width:22px;height:22px;border-radius:7px;
          background:linear-gradient(-44deg,#14A5F1,#BB5BFA)}
.modes{display:grid;grid-template-columns:repeat(3,1fr);gap:26px}
.card{background:#1C1E2E;border:1px solid #2A2D3C;border-radius:20px;padding:34px 30px}
.card .n{font-size:15px;letter-spacing:.14em;color:#BB5BFA;font-weight:600;margin-bottom:14px}
.card h3{font-size:31px;font-weight:600;margin-bottom:16px}
.card p{font-size:19px;color:#9AA0B8;line-height:1.5}
.card.on{border-color:#BB5BFA;background:#221A33}
.badge{display:inline-block;margin-top:20px;font-size:15px;color:#12131F;
       background:#BB5BFA;border-radius:999px;padding:6px 16px;font-weight:600}
.foot{position:absolute;bottom:52px;left:96px;font-size:19px;color:#6B7192}
</style>
"""
    return {
        '02-hero': base + f"""
<div class="logo">{logo}</div>
<h1 style="margin-top:44px">Жарнамасыз <span class="grad">интернет</span></h1>
<p class="lead" style="margin-top:26px">
Жарнаманы, бақылау трекерлерін және жасырын майнерлерді бұғаттайды.
Интерфейсі толықтай қазақ тілінде.</p>
<div class="foot">Ашық бастапқы код · GPLv3</div>""",

        '03-features': base + """
<h2>Не істейді</h2>
<ul>
  <li>Жарнаманы, трекерлерді және майнерлерді бұғаттайды</li>
  <li>Толықтай қазақ тілді интерфейс</li>
  <li>Әр сайт үшін бөлек сүзгілеу режимі</li>
  <li>Қалқымалы терезелерді бұғаттайды</li>
  <li>Қауіпті сайттарға өтуді тоқтатады</li>
  <li>Қалып қойған элементті қолмен жасыруға болады</li>
  <li>Өз сүзгіңізді жазуға мүмкіндік береді</li>
  <li>Ешқандай дербес дерек жинамайды</li>
</ul>
<div class="foot">github.com/jambyylf/tazakor</div>""",

        '04-modes': base + """
<h2>Үш сүзгілеу режимі</h2>
<div class="modes">
  <div class="card"><div class="n">01</div><h3>Негізгі</h3>
    <p>Тек желілік сұраныстарды бұғаттайды. Сайттардағы деректі оқымайды.</p></div>
  <div class="card"><div class="n">02</div><h3>Оңтайлы</h3>
    <p>Желілік бұғаттауға қоса, беттегі жарнама орындарын жасырады.</p></div>
  <div class="card on"><div class="n">03</div><h3>Толық</h3>
    <p>Барлық сайттарға рұқсат берілген жағдайда осы режим таңдалады.</p>
    <span class="badge">рұқсат берілсе — әдепкі</span></div>
</div>
<div class="foot">Рұқсат берілмесе, кеңейтім негізгі режимде жұмыс істейді</div>""",
    }


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    written = []
    for name, html in cards().items():
        p = os.path.join(DIR, name + '.html')
        open(p, 'w', encoding='utf-8').write(html)
        written.append(name)
    print('HTML жазылды:', ', '.join(written))
    print('Енді әрқайсысын Chrome-мен рендерлеңіз, содан соң HTML файлдарды өшіріңіз.')
