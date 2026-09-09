#!/usr/bin/env python3
"""TazaKor icon builder.

SVG -> transparent PNG at every size the extension and the Chrome Web Store need.
Uses headless Chrome, so nothing extra has to be installed.

  python make-icons.py tazakor-logo.svg
  python make-icons.py tazakor-logo.svg --out ./png
"""
import argparse, os, shutil, subprocess, sys, tempfile

SIZES = [16, 32, 48, 64, 128, 512]      # 16/32/64/128 = manifest, 48+512 = store
OFF_SIZES = [16, 32, 64, 128]           # greyed-out "paused" toolbar icons

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
]

def find_chrome():
    for p in CHROME_CANDIDATES:
        if p and os.path.isfile(p):
            return p
    p = shutil.which("chrome") or shutil.which("chromium") or shutil.which("google-chrome")
    if p:
        return p
    sys.exit("Chrome/Edge not found. Install Google Chrome, or edit CHROME_CANDIDATES.")

def render(chrome, svg_markup, size, dest, off=False):
    grey = "filter:grayscale(1) opacity(.45);" if off else ""
    html = (f"<style>html,body{{margin:0;padding:0;background:transparent}}"
            f"#i{{width:{size}px;height:{size}px;{grey}}}"
            f"#i svg{{width:100%!important;height:100%!important;display:block}}</style>"
            f"<div id='i'>{svg_markup}</div>")
    with tempfile.TemporaryDirectory() as td:
        page = os.path.join(td, "i.html")
        with open(page, "w", encoding="utf-8") as fh:
            fh.write(html)
        subprocess.run([chrome, "--headless", "--disable-gpu", "--hide-scrollbars",
                        "--default-background-color=00000000",
                        f"--screenshot={dest}", f"--window-size={size},{size}",
                        "file:///" + page.replace("\\", "/")],
                       check=True, capture_output=True)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("svg")
    ap.add_argument("--out", default=".")
    ap.add_argument("--prefix", default="tazakor-icon")
    args = ap.parse_args()

    svg = open(args.svg, encoding="utf-8").read()
    if "<image" in svg or "data:image" in svg:
        print("WARNING: the SVG embeds a raster image; the result will not be clean vector.")
    os.makedirs(args.out, exist_ok=True)
    chrome = find_chrome()
    print("Chrome:", chrome)

    for s in SIZES:
        dest = os.path.abspath(os.path.join(args.out, f"{args.prefix}-{s}.png"))
        render(chrome, svg, s, dest)
        print(f"  {os.path.basename(dest):<28} {os.path.getsize(dest):>7} bytes")
    for s in OFF_SIZES:
        dest = os.path.abspath(os.path.join(args.out, f"{args.prefix}-{s}-off.png"))
        render(chrome, svg, s, dest, off=True)
        print(f"  {os.path.basename(dest):<28} {os.path.getsize(dest):>7} bytes")
    print("done")

if __name__ == "__main__":
    main()
