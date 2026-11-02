"""Baut das Raten-Cockpit und die Stammdaten-Matrix aus der Excel-Ratenmatrix.

Aufruf (aus dem Repo-Ordner alpensonne-wissen/):
    python3 tools/raten-cockpit/build.py "Alpensonne_Ratenmatrix_2027.xlsx"

Ergebnis:
    stammdaten/raten/matrix-2027.yaml   Preise maschinenlesbar (eine Wahrheit)
    tools/raten-cockpit/cockpit.html    Seite für die Rezeption (wird als Artifact veröffentlicht)
"""
import json, sys, pathlib
import openpyxl

ROOT = pathlib.Path(__file__).resolve().parents[2]


def num(v):
    try:
        return round(float(v), 2)
    except (TypeError, ValueError):
        return None


def section(rs, marker, ncols):
    i = next(k for k, r in enumerate(rs) if r[0] and str(r[0]).startswith(marker)) + 2
    res, cat = {}, None
    while i < len(rs):
        r = rs[i]
        if r[0] is None and r[1] is None:
            break
        if r[0] and not str(r[0])[:2].isdigit():
            break
        if r[0]:
            cat = str(r[0]).strip()
        res.setdefault(cat, {})[str(int(r[1]))] = [num(x) for x in r[2:2 + ncols]]
        i += 1
    return res


def getaway(rs, marker):
    i = next(k for k, r in enumerate(rs) if r[0] and str(r[0]).startswith(marker))
    names = [str(x).strip().rstrip("0123456789") for x in rs[i + 1][2:11]]
    leist = [" ".join(str(x).replace("Leistungen:", "").split()) for x in rs[i + 2][2:11]]
    res, cat, j = {}, None, i + 3
    while j < len(rs) and rs[j][1] is not None and (rs[j][0] is None or str(rs[j][0])[:2].isdigit()):
        r = rs[j]
        if r[0]:
            cat = str(r[0]).strip()
        res.setdefault(cat, {})[str(int(r[1]))] = [num(x) for x in r[2:11]]
        j += 1
    return {"pakete": names, "leistungen": leist, "preise": res}


def main(xlsx):
    wb = openpyxl.load_workbook(xlsx, data_only=True)
    rows = lambda ws: [list(r) for r in ws.iter_rows(values_only=True)]
    h, a = rows(wb["Hotel 2027"]), rows(wb["Apartments 2027"])
    m = {
        "hotel": {
            "hs": section(h, "HAUPTSAISON RATE", 4),
            "ns": section(h, "NEBENSAISON RATE", 2),
            "ota_hs": section(h, "OTA´s - HAUPTSAISON", 4),
            "ota_ns": section(h, "OTA´s - NEBENSAISON", 2),
            "asi": section(h, "ASI RATE", 1),
            "feuer_eis": section(h, "FEUER & EIS", 1),
            "getaway_ns": getaway(h, "NEBENSAISON (NS) GETAWAY"),
            "getaway_hs": getaway(h, "HAUPTSAISON (HS) GETAWAY"),
        },
        "apartments": {
            "bar": section(a, "All YEAR RATE", 6),
            "ota": section(a, "OTA All YEAR RATE", 6),
            "paket_fw": section(a, "PAKET Frühstück", 3),
        },
    }
    tpl = (ROOT / "tools/raten-cockpit/cockpit.template.html").read_text(encoding="utf-8")
    (ROOT / "tools/raten-cockpit/cockpit.html").write_text(
        tpl.replace("/*MATRIX*/null", json.dumps(m, ensure_ascii=False, separators=(",", ":"))), encoding="utf-8")

    import yaml
    head = (
        "# Ratenmatrix 2027 – erzeugt aus \"Alpensonne Ratenmatrix 2027\" (Excel) mit tools/raten-cockpit/build.py\n"
        "# Nicht von Hand ändern: Excel pflegen, dann neu bauen.\n"
        "# Spalten je Personenanzahl:\n"
        "#   hotel.hs / ota_hs:      [Wochentag, Fr/Sa, NonRef Wochentag, NonRef Fr/Sa]\n"
        "#   hotel.ns / ota_ns:      [Rate, NonRef]\n"
        "#   apartments.bar / ota:   [2 N., 3–6 N. (Basis), ab 7 N., NonRef 2 N., NonRef 3–6 N., NonRef ab 7 N.]\n"
        "#   apartments.paket_fw:    [2 N., 3–6 N., ab 7 N.]  (nur Nebensaison)\n"
        "#   getaway_*:              Preis pro Person je Paket (Reihenfolge wie 'pakete')\n"
        "# Stellhebel: NonRef 5 %, OTA-Faktor 1,11, Apartment 2 N. +30 €, 7 N. −15 €, je Person > 2: +50 €\n"
        "# status: bestaetigt (Ratenmatrix von Benno) – Widersprüche siehe stammdaten/raten/README.md\n"
    )
    (ROOT / "stammdaten/raten/matrix-2027.yaml").write_text(
        head + yaml.safe_dump(m, allow_unicode=True, sort_keys=False, default_flow_style=None, width=200), encoding="utf-8")
    print("ok")


if __name__ == "__main__":
    main(sys.argv[1])
