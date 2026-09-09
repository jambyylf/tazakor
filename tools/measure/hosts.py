#!/usr/bin/env python3
"""Chrome желі журналынан хост атауларын шығарады."""
import re, sys, json
from urllib.parse import urlparse
from collections import Counter

BS = chr(92)

def hosts_from(path):
    data = open(path, encoding='utf-8', errors='replace').read()
    out = Counter()
    for u in re.findall(r'"url":\s*"(https?://[^"]+)"', data):
        u = u.replace(BS + '/', '/')
        try:
            h = urlparse(u).hostname
        except Exception:
            continue
        if h:
            out[h] += 1
    return out

if __name__ == '__main__':
    c = hosts_from(sys.argv[1])
    if len(sys.argv) > 2 and sys.argv[2] == '--json':
        print(json.dumps(dict(c), ensure_ascii=False))
    else:
        print(f'сұраныс: {sum(c.values())}, хост: {len(c)}')
        for h, n in c.most_common(40):
            print(f'  {n:>4}  {h}')
