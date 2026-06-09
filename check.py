#!/usr/bin/env python3
"""
P1.6 — Automatische Konsistenztests fuer ki-verstehen.html
Aufruf: python3 check.py
Gibt PASS/FAIL fuer jeden Check aus und schliesst mit Exit-Code 0 (OK) oder 1 (Fehler).
"""

import re, json, subprocess, sys, os

HTML = os.path.join(os.path.dirname(__file__), "ki-verstehen.html")
BASE = os.path.dirname(__file__)

failures = []
passes   = []

def ok(msg):   passes.append(msg);   print(f"  \033[32m✓\033[0m  {msg}")
def fail(msg): failures.append(msg); print(f"  \033[31m✗\033[0m  {msg}")

with open(HTML, encoding="utf-8") as f:
    src = f.read()


# ── 1. JS-Syntax ──────────────────────────────────────────────────────────────
print("\n[1] JavaScript-Syntax")
try:
    js_blocks = re.findall(r'<script[^>]*>(.*?)</script>', src, re.DOTALL)
    main_js   = max(js_blocks, key=len)
    with open("/tmp/k_check.js", "w", encoding="utf-8") as f:
        f.write(main_js)
    result = subprocess.run(["node", "--check", "/tmp/k_check.js"],
                            capture_output=True, text=True)
    if result.returncode == 0:
        ok("JS-Syntax gueltig")
    else:
        fail(f"JS-Syntaxfehler: {result.stderr.strip()}")
except Exception as e:
    fail(f"JS-Check fehlgeschlagen: {e}")


# ── 2. Dateien vorhanden ──────────────────────────────────────────────────────
print("\n[2] Pflichtdateien")
for path in ["manifest.json", "sw.js", "icons/icon-192.png",
             "icons/icon-512.png", "icons/apple-touch-icon.png"]:
    full = os.path.join(BASE, path)
    if os.path.exists(full):
        ok(f"Vorhanden: {path}")
    else:
        fail(f"Fehlt: {path}")


# ── 3. P0-Phrases duerfen nicht mehr erscheinen ───────────────────────────────
print("\n[3] P0-Regressionen (verbotene Phrasen)")

# Quelle ohne Quiz-Optionen: entferne sowohl {t:"...",c:false} als auch
# alle opt:[...]-Arrays aus quizFragen, damit falsche Antwortoptionen
# nicht als inhaltliche Regressionen gewertet werden.
src_no_wrong_opts = re.sub(
    r'\{t:"[^"]*"\s*,\s*c\s*:\s*false\}', '', src)          # check-Format
src_no_wrong_opts = re.sub(
    r'opt\s*:\s*\[[^\]]+\]', '', src_no_wrong_opts)          # quiz-Array-Format

banned = [
    (src_no_wrong_opts,
     "PDFs koennen nie direkt gelesen werden",
     "P0.2: Alte falsche PDF-Aussage wieder vorhanden (ausserhalb Quiz-Fehlerantworte)"),
    (src_no_wrong_opts,
     "Claude kann keine PDFs",
     "P0.2: Alte falsche PDF-Aussage wieder vorhanden"),
    (src_no_wrong_opts,
     r"PDF.*nie.*direkt.*lesen",
     "P0.2: Variante der alten PDF-Aussage (ausserhalb Quiz-Fehlerantworte)"),
    (src,
     "vor jedem Task automatisch geladen",
     "P0.5: Alte CLAUDE.md-Formulierung wieder vorhanden"),
    (src,
     "Another Markup Language",
     "P0.6: YAML-Langform falsch (muss 'Ain't Markup Language' sein)"),
    (src,
     "LLMs verarbeiten ausschliesslich Text",
     "P0.1: Alte Aussage ueber LLM-Textverarbeitung"),
]
for text, pattern, label in banned:
    if re.search(pattern, text, re.IGNORECASE):
        fail(label)
    else:
        ok(f"Nicht gefunden: '{pattern[:45]}...'")


# ── 4. Karteikarten-IDs eindeutig ────────────────────────────────────────────
print("\n[4] Karteikarten-IDs")
ids = re.findall(r'\bid\s*:\s*"(k\d+)"', src)
if not ids:
    fail("Keine Karteikarten-IDs gefunden — Pattern pruefen")
else:
    seen = {}
    for kid in ids:
        seen[kid] = seen.get(kid, 0) + 1
    dupes = {k: v for k, v in seen.items() if v > 1}
    if dupes:
        fail(f"Doppelte Karteikarten-IDs: {dupes}")
    else:
        ok(f"{len(ids)} Karteikarten-IDs alle eindeutig")


# ── 5. Karteikarten-Fronts (Glossarbegriffe) eindeutig ───────────────────────
print("\n[5] Karteikarten-Fronts (Glossar-Duplikate)")
# Kommentarzeilen ausschliessen (// ...)
src_no_comments = re.sub(r'^\s*//.*$', '', src, flags=re.MULTILINE)
fronts = re.findall(r'\bfront\s*:\s*"([^"]+)"', src_no_comments)
if not fronts:
    fail("Keine Karteikarten-Fronts gefunden — Pattern pruefen")
else:
    seen_f = {}
    for f in fronts:
        key = f.lower().strip()
        seen_f[key] = seen_f.get(key, 0) + 1
    dupes_f = {k: v for k, v in seen_f.items() if v > 1}
    if dupes_f:
        fail(f"Doppelte Karteikarten-Fronts (normalisiert): {list(dupes_f.keys())}")
    else:
        ok(f"{len(fronts)} Karteikarten-Fronts alle eindeutig")


# ── 6. Quiz korrekt-Index im Bereich ─────────────────────────────────────────
print("\n[6] Quiz-Fragen: korrekt-Index im Bereich")
# Extrahiere alle Quiz-Objekte: { ..., opt:[...], korrekt:N }
quiz_pattern = re.compile(
    r'opt\s*:\s*\[([^\]]+)\]\s*,\s*korrekt\s*:\s*(\d+)', re.DOTALL)
quiz_matches = quiz_pattern.findall(src)
if not quiz_matches:
    fail("Keine Quiz-Fragen mit opt/korrekt gefunden — Pattern pruefen")
else:
    errors = []
    for opts_raw, korrekt_str in quiz_matches:
        # Zaehle Elemente im opt-Array (grob: Anzahl der Strings)
        opts_count = len(re.findall(r'"[^"]*"', opts_raw))
        korrekt    = int(korrekt_str)
        if opts_count > 0 and korrekt >= opts_count:
            errors.append(f"korrekt={korrekt} >= len(opt)={opts_count}")
    if errors:
        fail(f"Quiz-Index ausserhalb Bereich: {errors}")
    else:
        ok(f"{len(quiz_matches)} Quiz-Fragen: korrekt-Index immer im Bereich")


# ── 7. Abkuerzungschips referenzieren vorhandene abkGlossar-Eintraege ────────
print("\n[7] etappeAbk — alle Chips im abkGlossar vorhanden")
# abkGlossar-Schluessel extrahieren
abk_match = re.search(r'const abkGlossar\s*=\s*\{([^}]+)\}', src, re.DOTALL)
if not abk_match:
    fail("abkGlossar nicht gefunden")
else:
    abk_keys = set(re.findall(r'"([A-Z][^"]*)"', abk_match.group(1)))
    # etappeAbk-Werte extrahieren
    etabk_match = re.search(r'const etappeAbk\s*=\s*\{(.+?)\}\s*;', src, re.DOTALL)
    if not etabk_match:
        fail("etappeAbk nicht gefunden")
    else:
        chip_values = re.findall(r'"([A-Za-z][^"]*)"', etabk_match.group(1))
        # Filtere auf Chip-Bezeichner (keine Muster wie "0-0")
        chips = [c for c in chip_values if not re.match(r'^\d+-\d+$', c)]
        missing = [c for c in chips if c not in abk_keys]
        if missing:
            fail(f"Chips ohne abkGlossar-Eintrag: {list(set(missing))}")
        else:
            ok(f"{len(set(chips))} Chips alle im abkGlossar vorhanden")


# ── 8. Etappen-Pflichtfelder vorhanden ───────────────────────────────────────
print("\n[8] Etappen-Pflichtfelder (titel, kernsatz, punkte, merkbild, check)")
# kernsatz ist ein reines Etappenfeld — dessen Anzahl = Anzahl Etappen
# titel koennte auch Modul-Objekte haben, deshalb kernsatz als Referenz
MIN_ETAPPEN = 43  # bekannte Mindestanzahl
etappen_count = len(re.findall(r'\bkernsatz\s*:', src))
if etappen_count < MIN_ETAPPEN:
    fail(f"Zu wenige kernsatz-Felder: {etappen_count} (erwartet >= {MIN_ETAPPEN})")
else:
    ok(f"kernsatz-Felder: {etappen_count} (>= {MIN_ETAPPEN})")

for field in ["titel", "punkte", "merkbild", "check"]:
    count = len(re.findall(rf'\b{field}\s*:', src))
    if count == 0:
        fail(f"Pflichtfeld '{field}' nirgendwo gefunden")
    elif count >= etappen_count * 0.9:
        ok(f"Feld '{field}' vorhanden ({count}x)")
    else:
        fail(f"Feld '{field}' seltener als erwartet ({count}x bei {etappen_count} Etappen)")


# ── 9. Modul-Array vorhanden und nicht leer ───────────────────────────────────
print("\n[9] Strukturpruefung module-Array")
modul_entries = re.findall(r'\btitel\s*:"[^"]{3,}"', src)
if len(modul_entries) >= 43:
    ok(f"module-Array hat mindestens 43 Etappen ({len(modul_entries)} Titelfelder gefunden)")
else:
    fail(f"module-Array kleiner als erwartet: nur {len(modul_entries)} Titelfelder")


# ── 10. Manifest auf noetige Felder pruefen ──────────────────────────────────
print("\n[10] manifest.json")
manifest_path = os.path.join(BASE, "manifest.json")
try:
    with open(manifest_path, encoding="utf-8") as f:
        mf = json.load(f)
    for field in ["name", "short_name", "start_url", "icons"]:
        if field in mf:
            ok(f"manifest.json: Feld '{field}' vorhanden")
        else:
            fail(f"manifest.json: Pflichtfeld '{field}' fehlt")
except FileNotFoundError:
    fail("manifest.json nicht gefunden")
except json.JSONDecodeError as e:
    fail(f"manifest.json ungueltig: {e}")


# ── Zusammenfassung ───────────────────────────────────────────────────────────
print(f"\n{'='*60}")
print(f"  Bestanden: {len(passes)}  |  Fehlgeschlagen: {len(failures)}")
if failures:
    print("\n  Fehler:")
    for f in failures:
        print(f"    - {f}")
    print()
    sys.exit(1)
else:
    print("\n  Alle Checks bestanden.\n")
    sys.exit(0)
