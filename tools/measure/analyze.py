#!/usr/bin/env python3
import json, glob, os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from matcher import load, domain_hit

BUILD = sys.argv[1]
HOSTS = sys.argv[2]
dom, allow, subs = load(BUILD)

SITE_OWN = {
 'zakon':'zakon.kz','nur':'nur.kz','tengri':'tengrinews.kz','informburo':'informburo.kz',
 'kolesa':'kolesa.kz','krisha':'krisha.kz','24kz':'24.kz','inbusiness':'inbusiness.kz',
 'sportskz':'sports.kz','lada':'lada.kz','ktk':'ktk.kz','diapazon':'diapazon.kz',
}
# Браузердің өз қызметтері — жарнамаға қатысы жоқ
INFRA = re.compile(r'(^|\.)(gstatic\.com|googleapis\.com|google\.com|google\.kz|'
                   r'gvt1\.com|gvt2\.com|chrome\.com|mozilla\.(org|net)|'
                   r'cloudflare\.com|jsdelivr\.net|unpkg\.com|bootstrapcdn\.com|'
                   r'jquery\.com|fontawesome\.com|w3\.org|schema\.org)$')

per_host_sites = {}
for f in glob.glob(os.path.join(HOSTS, '*.json')):
    name = os.path.splitext(os.path.basename(f))[0]
    own = SITE_OWN.get(name, '')
    for h in json.load(open(f, encoding='utf-8')):
        hl = h.lower()
        if own and (hl == own or hl.endswith('.' + own)):
            continue                                  # сайттың өз домені
        if INFRA.search(hl):
            continue
        per_host_sites.setdefault(hl, set()).add(name)

blocked, passing = [], []
for h, sites in per_host_sites.items():
    (blocked if domain_hit(h, dom) else passing).append((h, sites))

print(f'Барлығы {len(per_host_sites)} бөгде хост')
print(f'  бұғатталады : {len(blocked)}')
print(f'  өтіп кетеді : {len(passing)}')
print()
print('ӨТІП КЕТЕТІНДЕРІ, неше сайтта кездескеніне қарай:')
for h, sites in sorted(passing, key=lambda x: (-len(x[1]), x[0])):
    mark = '  <-- бірнеше сайтта' if len(sites) >= 2 else ''
    print(f'  {len(sites)}x  {h:<38} {",".join(sorted(sites))[:40]}{mark}')
