#!/usr/bin/env python3
"""
P1.5 — Einzige Quelle der Wahrheit: ki-verstehen.html (JS-Daten)

Dieses Skript liest ki-verstehen.html und erzeugt daraus
KI-Wissensbasis-Export.md — eine strukturierte Markdown-Datei
fuer NotebookLM, Sync-Pruefung und Dokumentation.

Aufruf: python3 export_md.py
Hinweis: ki-verstehen.html NICHT manuell bearbeiten und gleichzeitig
         diese MD-Datei pflegen — immer export_md.py neu ausfuehren.
"""

import re, os, datetime

HTML  = os.path.join(os.path.dirname(__file__), "ki-verstehen.html")
OUT   = os.path.join(os.path.dirname(__file__), "KI-Wissensbasis-Export.md")

with open(HTML, encoding="utf-8") as f:
    src = f.read()


# ── Hilfsfunktionen ────────────────────────────────────────────────────────────

def find_js_array(source, varname):
    """Gibt den Inhalt eines const varname = [...]; Blocks zurueck.
    String-aware: [ und ] innerhalb von Strings werden nicht gezaehlt."""
    pattern = rf'const {re.escape(varname)}\s*=\s*\['
    m = re.search(pattern, source)
    if not m:
        return ""
    start = m.end()
    depth = 1
    i = start
    in_str = False
    esc = False
    while i < len(source) and depth > 0:
        c = source[i]
        if esc:
            esc = False
        elif in_str:
            if c == '\\':
                esc = True
            elif c == '"':
                in_str = False
        else:
            if c == '"':
                in_str = True
            elif c == '[':
                depth += 1
            elif c == ']':
                depth -= 1
        i += 1
    return source[start:i - 1]


def split_objects(js):
    """Teilt ein JS-Array von Objekten in einzelne {…}-Strings auf.
    String-aware: { und } innerhalb von Strings werden nicht gezaehlt."""
    objects = []
    depth = 0
    start = -1
    in_str = False
    esc = False
    for i, c in enumerate(js):
        if esc:
            esc = False
            continue
        if in_str:
            if c == '\\':
                esc = True
            elif c == '"':
                in_str = False
        else:
            if c == '"':
                in_str = True
            elif c == '{':
                if depth == 0:
                    start = i
                depth += 1
            elif c == '}':
                depth -= 1
                if depth == 0 and start >= 0:
                    objects.append(js[start:i + 1])
                    start = -1
    return objects


def get_str(obj, key):
    """Extrahiert einen einfachen String-Wert aus einem JS-Objekt."""
    m = re.search(rf'\b{re.escape(key)}\s*:\s*"((?:[^"\\]|\\.)*)"', obj)
    return m.group(1).replace('\\"', '"').replace('\\n', '\n') if m else ""


def get_str_array(obj, key):
    """Extrahiert ein String-Array aus einem JS-Objekt."""
    m = re.search(rf'\b{re.escape(key)}\s*:\s*\[', obj)
    if not m:
        return []
    start = m.end()
    depth = 1
    i = start
    while i < len(obj) and depth > 0:
        if obj[i] == '[':
            depth += 1
        elif obj[i] == ']':
            depth -= 1
        i += 1
    content = obj[start:i - 1]
    return [s.replace('\\"', '"').replace('\\n', '\n')
            for s in re.findall(r'"((?:[^"\\]|\\.)*)"', content)]


def unescape(s):
    """Einfaches HTML/JS-Unescape fuer die MD-Ausgabe."""
    return (s.replace('&amp;', '&')
             .replace('&lt;', '<')
             .replace('&gt;', '>')
             .replace('&quot;', '"')
             .replace('&#8592;', '←')
             .replace('&#8594;', '→'))


# ── Module- und Etappen-Daten extrahieren ──────────────────────────────────────

# Modul-Array: titel + kurz je Modul
MOD_ARRAY_NAMES = ['etappen',
                   'etappenMod2', 'etappenMod3', 'etappenMod4',
                   'etappenMod5', 'etappenMod6', 'etappenMod7', 'etappenMod8']

MODULE_META = []
mod_arr_raw = find_js_array(src, 'module')
for obj in split_objects(mod_arr_raw):
    t = get_str(obj, 'titel')
    k = get_str(obj, 'kurz')
    if t:
        MODULE_META.append({'titel': t, 'kurz': k})

# Etappen je Modul
ALL_MODULES = []
for mod_idx, varname in enumerate(MOD_ARRAY_NAMES):
    raw = find_js_array(src, varname)
    etappen_objs = split_objects(raw)
    etappen = []
    for obj in etappen_objs:
        t  = unescape(get_str(obj, 'titel'))
        ks = unescape(get_str(obj, 'kernsatz'))
        mb = unescape(get_str(obj, 'merkbild'))
        ps = [unescape(p) for p in get_str_array(obj, 'punkte')]
        if t and ks:    # nur vollstaendige Etappen-Objekte
            etappen.append({'titel': t, 'kernsatz': ks, 'merkbild': mb, 'punkte': ps})
    if etappen:
        modul_titel = MODULE_META[mod_idx]['titel'] if mod_idx < len(MODULE_META) else f"Modul {mod_idx + 1}"
        modul_kurz  = MODULE_META[mod_idx]['kurz']  if mod_idx < len(MODULE_META) else ""
        ALL_MODULES.append({'id': mod_idx, 'titel': modul_titel, 'kurz': modul_kurz, 'etappen': etappen})


# ── Karteikarten extrahieren ──────────────────────────────────────────────────

KARTEN = []
raw_karten = find_js_array(src, 'karteikarten')
for obj in split_objects(raw_karten):
    kid   = get_str(obj, 'id')
    front = unescape(get_str(obj, 'front'))
    back  = unescape(get_str(obj, 'back'))
    m_id_match = re.search(r'\bmodul\s*:\s*(\d+)', obj)
    modul = int(m_id_match.group(1)) if m_id_match else -1
    if kid and front:
        KARTEN.append({'id': kid, 'front': front, 'back': back, 'modul': modul})


# ── Markdown generieren ────────────────────────────────────────────────────────

today = datetime.date.today().isoformat()
lines = []

lines.append(f"# KI & Große Sprachmodelle — Lerninhalt (exportiert aus ki-verstehen.html)")
lines.append("")
lines.append(f"> **Automatisch generiert** | Quelle: `ki-verstehen.html` | Stand: {today}")
lines.append(f"> Diese Datei NICHT manuell bearbeiten. Aenderungen gehoeren in `ki-verstehen.html`,")
lines.append(f"> danach `python3 export_md.py` ausfuehren, um diese Datei neu zu generieren.")
lines.append("")
lines.append(f"**Inhalt:** {len(ALL_MODULES)} Module · "
             f"{sum(len(m['etappen']) for m in ALL_MODULES)} Etappen · "
             f"{len(KARTEN)} Karteikarten")
lines.append("")
lines.append("---")
lines.append("")

# Lernmodule
lines.append("## Lernmodule")
lines.append("")

for mod in ALL_MODULES:
    lines.append(f"### Modul {mod['id'] + 1}: {mod['titel']}")
    if mod['kurz']:
        lines.append(f"*{mod['kurz']}*")
    lines.append("")

    for ei, et in enumerate(mod['etappen']):
        lines.append(f"#### {mod['id'] + 1}.{ei + 1} — {et['titel']}")
        lines.append("")
        lines.append(f"**Kernsatz:** {et['kernsatz']}")
        lines.append("")
        if et['punkte']:
            for p in et['punkte']:
                lines.append(f"- {p}")
            lines.append("")
        if et['merkbild']:
            lines.append(f"> 🧠 *{et['merkbild']}*")
            lines.append("")

lines.append("---")
lines.append("")

# Karteikarten-Glossar
lines.append("## Karteikarten / Glossar")
lines.append("")
lines.append("Die folgenden Definitionen entstammen den Lern-Karteikarten (Leitner-System).")
lines.append("")

# Gruppiert nach Modul
for mod_id in range(len(ALL_MODULES)):
    karten_mod = [k for k in KARTEN if k['modul'] == mod_id]
    if not karten_mod:
        continue
    modul_titel = ALL_MODULES[mod_id]['titel'] if mod_id < len(ALL_MODULES) else f"Modul {mod_id + 1}"
    lines.append(f"### Modul {mod_id + 1}: {modul_titel}")
    lines.append("")
    for k in karten_mod:
        lines.append(f"**{k['front']}**")
        lines.append(f": {k['back']}")
        lines.append("")

lines.append("---")
lines.append("")
lines.append(f"*Generiert: {today} — Quelle: ki-verstehen.html*")
lines.append("")

# Ausgabe schreiben
output = "\n".join(lines)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(output)

print(f"✓ Exportiert: {OUT}")
print(f"  {len(ALL_MODULES)} Module, "
      f"{sum(len(m['etappen']) for m in ALL_MODULES)} Etappen, "
      f"{len(KARTEN)} Karteikarten")
