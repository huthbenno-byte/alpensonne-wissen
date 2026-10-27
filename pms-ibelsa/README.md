# PMS · ibelsa

**Zweck:** Property-Management-System für Hotel und Apartments: Kategorien, Ratenpläne, Tagespreise, Reservierungen, Rechnungen. Datenquelle für alle eigenen Tools.

**Ist-Stand:**
- Kategorien 01–09 angelegt, Kategoriename beginnt mit dem Code (z. B. "07 Apartment 1 Zimmer")
- Ratenpläne 2027 angelegt: BAR, NonRef, OTA, OTA NonRef (nur Hotel) – Namen und IDs in `stammdaten/raten/mapping.yaml`
- Rate-Namen schreiben "Appartment" (Altlast) – Tools suchen per exaktem Namen
- ASI-Import montags und donnerstags per CSV (Vorlage 52 Spalten)
- Aufbettung Kinder als ibelsa-Produkte (5 / 20 / 35 €), Kurtaxe-Artikel Kur5 / Kur15 / Kur16
- API wird genutzt von Reporting, Ankunftsliste, Preis-Check (Key nur als Railway-Variable)

**Ansprechpartner:** Benno (intern); ibelsa-Support: offen

**Abhängigkeiten:**
- nutzt: `stammdaten/kategorien.yaml`, `stammdaten/raten/`, `stammdaten/policies.yaml` (Kinder, Kurtaxe)
- liefert an: DIRS21 (Raten/Verfügbarkeit), `tools/`
