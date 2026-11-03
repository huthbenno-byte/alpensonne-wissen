# Tools

**Zweck:** Verweise auf die Apps und Seiten, mit denen das Team arbeitet.

## Raten-Cockpit (Rezeption)
- Link: https://claude.ai/artifact/HAAE1FAsPnKerC9w5nJDbJ
- Quelle: `tools/raten-cockpit/` (`cockpit.template.html` + `build.py`; `cockpit.html` ist erzeugt)
- Inhalt: laufende Aktionen je Kanal, Preis prüfen (Matrix 2027 minus Aktionen), Raten-Spickzettel, Preis-Rätsel
- Daten: Preise kommen aus `stammdaten/raten/matrix-2027.yaml`. Aktionen und Preis-Rätsel liegen in der Datenbank des Cockpits (Sammlungen `aktionen` und `raetsel`), damit Revenue sie ohne Git pflegen kann. Claude kann sie lesen und schreiben.
- Zugang: Teilen-Menü des Artifacts → Rezeptions-Konto per E-Mail mit niedrigster Stufe (Ansehen) einladen. Lesezugang sieht alles, ändert nichts. Aktionen ändern nur Owner/Editor (Datenbank-Regel).
- Neu bauen nach Änderung der Excel: `python3 tools/raten-cockpit/build.py "<Pfad zur Ratenmatrix.xlsx>"`, danach Artifact neu veröffentlichen.

## Weitere (Verweise folgen)
- Reporting, Ankünfte, Preis-Check (alt), Mahnwesen
