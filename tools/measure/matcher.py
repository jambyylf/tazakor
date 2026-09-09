#!/usr/bin/env python3
"""ТазаКөр ережелері белгілі бір хостты бұғаттай ма, соны тексереді.

Толық DNR қозғалтқышы емес. Тек домен деңгейіндегі бұғаттауды қарайды,
себебі жарнама домендеріне жазылатын ережелердің басым бөлігі сондай.
Нәтиже жуық: «бұғатталады» деген сенімді, «бұғатталмайды» деген тексеруді
қажет етеді.
"""
import json, glob, os, re, sys

def load(build_dir, enabled_only=True):
    m = json.load(open(os.path.join(build_dir, 'manifest.json'), encoding='utf-8'))
    ids = {r['id'] for r in m['declarative_net_request']['rule_resources']
           if (r['enabled'] or not enabled_only)}
    domains = set()          # ||host^ немесе requestDomains
    substrings = []          # қалған urlFilter үлгілері
    allow_domains = set()
    for f in glob.glob(os.path.join(build_dir, 'rulesets', 'main', '*.json')):
        rid = os.path.splitext(os.path.basename(f))[0]
        if rid not in ids:
            continue
        try:
            rules = json.load(open(f, encoding='utf-8'))
        except Exception:
            continue
        for r in rules:
            if not isinstance(r, dict):
                continue
            act = (r.get('action') or {}).get('type')
            cond = r.get('condition') or {}
            target = allow_domains if act == 'allow' else domains
            for d in cond.get('requestDomains') or []:
                target.add(d.lower())
            uf = cond.get('urlFilter')
            if isinstance(uf, str) and uf:
                mm = re.fullmatch(r'\|\|([a-z0-9.-]+)\^?', uf.lower())
                if mm:
                    target.add(mm.group(1))
                elif act != 'allow':
                    substrings.append(uf.lower())
    return domains, allow_domains, substrings

def domain_hit(host, dset):
    host = host.lower().rstrip('.')
    parts = host.split('.')
    for i in range(len(parts) - 1):
        if '.'.join(parts[i:]) in dset:
            return '.'.join(parts[i:])
    return None

if __name__ == '__main__':
    build = sys.argv[1]
    dom, allow, subs = load(build)
    print(f'ережелерден жиналды: {len(dom)} бұғаттау домені, '
          f'{len(allow)} ерекшелік, {len(subs)} үлгі')
    for h in sys.argv[2:]:
        hit = domain_hit(h, dom)
        print(f'  {h:<30} {"БҰҒАТТАЛАДЫ (" + hit + ")" if hit else "өтіп кетеді"}')
