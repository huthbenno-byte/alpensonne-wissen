# Channel Manager · DIRS21

**Zweck:** Verteilt Raten und Verfügbarkeiten an Website-Buchungsstrecke (IBE) und OTAs; Belegungspreise und Konditionen.

**Ist-Stand:**
- Zwei Channels: Hotel und Apartments (IDs in `stammdaten/raten/mapping.yaml`)
- IBE: reservation.one.dirs21.de/hotel und …/apartmennt (Tippfehler im Pfad ist echt)
- Hotel-NonRef wird direkt in DIRS21 gepflegt – immer "Erweiterte Preiseingabe" mit Belegungsmatrix, sonst rechnet DIRS21 Kinder mit ~91 € (Anleitung: Google Doc "DIRS21 – Belegungspreise NonRef pflegen", 13.10.2026). Matrix gültig bis 02.01.2028.
- Mindestaufenthalt Hotel auf der Website 3 Nächte ab Mai 2027
- Promo Apartments −14 % (Stand 06.10.2026)
- Google Hotels: nur Hotel angebunden

**Ansprechpartner:** Benno (intern); DIRS21-Ansprechpartner: offen

**Abhängigkeiten:**
- nutzt: ibelsa-Raten, `stammdaten/raten/mapping.yaml`, `stammdaten/policies.yaml` (Kinder, Storno)
- liefert an: Website, `kanaele/`, Preis-Check (inoffizielle IBE-Schnittstelle)
