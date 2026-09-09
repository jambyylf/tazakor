#!/usr/bin/env python3
"""Chrome Web Store-ға жүктеуге дайын ZIP архивін жасайды.

Windows-та `zip` командасы жоқ, ал PowerShell-дің Compress-Archive
командасы жол бөлгішін кері қиғаш сызық етіп жазады, ол ZIP стандартына
қайшы. Сондықтан архивті осы скрипт жасайды.

Қолданылуы:
    python tools/make-store-zip.py [папка] [шығыс.zip]

Әдепкі мәндері:
    папка     dist/build/uBOLite.chromium
    шығыс     dist/tazakor-<нұсқа>-chromium.zip
"""
import json, os, sys, zipfile

# Пакетке кірмейтін файлдар
EXCLUDE_NAMES = {'log.txt', '.DS_Store', 'Thumbs.db'}
EXCLUDE_EXTS = ('.map',)


def build(src, out=None):
    manifest_path = os.path.join(src, 'manifest.json')
    if not os.path.isfile(manifest_path):
        sys.exit(f'manifest.json табылмады: {manifest_path}')
    with open(manifest_path, encoding='utf-8') as fh:
        manifest = json.load(fh)
    version = manifest.get('version', '0.0.0')

    if out is None:
        out = os.path.join('dist', f'tazakor-{version}-chromium.zip')
    os.makedirs(os.path.dirname(out) or '.', exist_ok=True)
    if os.path.exists(out):
        os.remove(out)

    added, skipped = 0, []
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for root, dirs, files in os.walk(src):
            dirs.sort()
            for name in sorted(files):
                if name in EXCLUDE_NAMES or name.endswith(EXCLUDE_EXTS):
                    skipped.append(name)
                    continue
                full = os.path.join(root, name)
                # ZIP стандарты тек алға қиғаш сызықты қабылдайды
                rel = os.path.relpath(full, src).replace(os.sep, '/')
                z.write(full, rel)
                added += 1

    # Тексеру
    with zipfile.ZipFile(out) as z:
        names = z.namelist()
    problems = []
    if 'manifest.json' not in names:
        problems.append('manifest.json архивтің түбірінде жоқ')
    bad = [n for n in names if chr(92) in n]
    if bad:
        problems.append(f'{len(bad)} жолда кері қиғаш сызық бар')
    dev = [p for p in manifest.get('permissions', []) if 'Feedback' in p]
    if dev:
        problems.append(f'әзірлеу рұқсаты қалған: {dev}')

    size_mb = os.path.getsize(out) / 1048576
    print(f'нұсқа     : {version}')
    print(f'архив     : {out}')
    print(f'файл саны : {added}' + (f' (өткізілді: {len(skipped)})' if skipped else ''))
    print(f'өлшемі    : {size_mb:.1f} MB')
    if problems:
        print('\nМӘСЕЛЕ:')
        for p in problems:
            print(f'  - {p}')
        sys.exit(1)
    print('тексеру   : бәрі дұрыс')
    return out


if __name__ == '__main__':
    src = sys.argv[1] if len(sys.argv) > 1 else 'dist/build/uBOLite.chromium'
    out = sys.argv[2] if len(sys.argv) > 2 else None
    build(src, out)
