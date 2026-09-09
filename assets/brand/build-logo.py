#!/usr/bin/env python3
"""ТазаКөр белгісін таза SVG етіп құрады (тек екі path, растр жоқ).

Барлық сан tazakor-logo-source.png файлының пикселдерінен өлшеніп алынған.

Құрылысы: диагональ жолағының ЖОҒАРҒЫ қыры сақинаның СЫРТҚЫ шеңберіне,
ТӨМЕНГІ қыры ІШКІ шеңберіне жанама болып жатыр (өлшеу дәлдігі 0.3 пиксель).
Сол себепті «O» мен «N» бір таспа болып үзіліссіз жалғасады, ал жалғау
сызығы центрден шыққан радиустың бойымен өтеді — сол жерде тігіс көрінбейді.
"""
import math, sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass

# ── Түпнұсқадан өлшенген шамалар (1080×1080 суреттің координаттары) ─────────
CX, CY   = 468.5, 540.0     # сақинаның центрі
R_OUT    = 135.5            # сыртқы радиус
R_IN     = 79.0             # ішкі радиус
STEM_R   = 747.0            # тік бағананың оң шеті
TOP, BOT = 405.0, 675.0     # белгінің жоғарғы / төменгі шегі
GAP      = 14.47            # «O» ұшы мен диагональ арасындағы саңылау

GU       = (0.7146, -0.6995)             # градиент осінің бағыты (−44.4°)
GS0, GS1 = -176.3, 247.7                 # ось бойындағы ұштық проекциялар
STOPS = [(0.00, "#03A8F1"), (0.19, "#379EF2"), (0.31, "#698DF4"),
         (0.44, "#8A7CF6"), (0.56, "#A16DF8"), (0.69, "#B65EFA"),
         (0.81, "#BB5BFA"), (1.00, "#BB5BFA")]

W      = R_OUT - R_IN                    # штрих қалыңдығы
STEM_L = STEM_R - W

# Диагональдың төменгі қыры: (STEM_L, BOT) арқылы өтіп, ішкі шеңберге жанама
_a = (CX - STEM_L)**2 - R_IN**2
_b = -2*(CX - STEM_L)*(CY - BOT)
_c = (CY - BOT)**2 - R_IN**2
M  = (-_b + math.sqrt(_b*_b - 4*_a*_c)) / (2*_a)
K  = math.hypot(M, 1.0)
C_BOT  = BOT - M*STEM_L
C_TOP  = C_BOT - W*K
C_GAP  = C_BOT + GAP*K                   # «O» ұшын кесетін сызық
NX, NY = M/K, -1.0/K

def ang(p): return math.degrees(math.atan2(p[1]-CY, p[0]-CX))

def chord(c, r):
    """y = M·x + c сызығы мен r радиусты шеңбердің қиылысы: (сол, оң)."""
    d = (M*CX - CY + c)/K
    fx, fy = CX - d*NX, CY - d*NY
    h = math.sqrt(max(r*r - d*d, 0.0))
    return (fx - h/K, fy - h*M/K), (fx + h/K, fy + h*M/K)

TAN_OUT  = (CX + R_OUT*NX, CY + R_OUT*NY)   # жоғарғы қырдың жанама нүктесі
TAN_IN   = (CX + R_IN*NX,  CY + R_IN*NY)    # төменгі қырдың жанама нүктесі
TH_SEAM  = ang(TAN_OUT)                     # жалғау радиусының бұрышы
_, A_IN  = chord(C_GAP, R_IN)               # «O» ұшы — ішкі нүкте
_, A_OUT = chord(C_GAP, R_OUT)              # «O» ұшы — сыртқы нүкте

class T:
    """Масштабтап, жылжытатын түрлендіру."""
    def __init__(s, k=1.0, dx=0.0, dy=0.0): s.k, s.dx, s.dy = k, dx, dy
    def __call__(s, p): return (p[0]*s.k + s.dx, p[1]*s.k + s.dy)

def svg(t, vb):
    f = lambda p: "%.2f %.2f" % t(p)
    sw_o = (TH_SEAM - ang(A_OUT)) % 360
    sw_i = (TH_SEAM - ang(A_IN)) % 360
    o = (f"M{f(A_OUT)}"
         f"A{R_OUT*t.k:.2f} {R_OUT*t.k:.2f} 0 {1 if sw_o > 180 else 0} 1 {f(TAN_OUT)}"
         f"L{f(TAN_IN)}"
         f"A{R_IN*t.k:.2f} {R_IN*t.k:.2f} 0 {1 if sw_i > 180 else 0} 0 {f(A_IN)}Z")
    v = [TAN_OUT, (STEM_L, M*STEM_L + C_TOP), (STEM_L, TOP), (STEM_R, TOP),
         (STEM_R, BOT), (STEM_L, BOT), TAN_IN]
    n = "M" + "L".join(f(p) for p in v) + "Z"
    p0 = t((GS0*GU[0], GS0*GU[1]))
    p1 = t((GS1*GU[0], GS1*GU[1]))
    stops = "\n".join('      <stop offset="%.2f" stop-color="%s"/>' % s for s in STOPS)
    return (
'<svg xmlns="http://www.w3.org/2000/svg" viewBox="%s" role="img" aria-label="TazaKor">\n'
'  <title>TazaKor</title>\n'
'  <defs>\n'
'    <linearGradient id="tazakor" gradientUnits="userSpaceOnUse"\n'
'      x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f">\n'
'%s\n'
'    </linearGradient>\n'
'  </defs>\n'
'  <g fill="url(#tazakor)">\n'
'    <path d="%s"/>\n'
'    <path d="%s"/>\n'
'  </g>\n'
'</svg>\n' % (vb, p0[0], p0[1], p1[0], p1[1], stops, o, n))

X0, Y0 = CX - R_OUT, TOP
w, h = STEM_R - X0, BOT - TOP
open('tazakor-logo.svg', 'w', encoding='utf-8').write(
    svg(T(1.0, -X0, -Y0), "0 0 %.0f %.0f" % (w, h)))
PAD, SIDE = 6.0, 128.0
k = (SIDE - 2*PAD)/w
open('tazakor-icon.svg', 'w', encoding='utf-8').write(
    svg(T(k, PAD - X0*k, (SIDE - h*k)/2 - Y0*k), "0 0 128 128"))

print("көлбеулік M   : %.4f (%.1f°)   өлшенгені 1.1481" % (M, math.degrees(math.atan(M))))
print("штрих         : %.1f" % W)
print("саңылау       : %.2f (штрихтың %.0f%%)" % (GAP, GAP/W*100))
print("жалғау бұрышы : %.1f°" % TH_SEAM)
print("белгі         : %.0f×%.0f (пропорция %.3f:1)" % (w, h, w/h))
print("иконка        : 128×128, штрих %.1fpx, 16px-те штрих %.2fpx, тесік %.2fpx"
      % (W*k, W*k/8, 2*R_IN*k/8))
