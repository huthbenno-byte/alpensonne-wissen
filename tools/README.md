# Eigene Tools

**Zweck:** Verweise auf die eigenen App-Repos. Code liegt dort, hier nur Überblick und Abhängigkeiten.

**Ist-Stand:** Hosting auf Railway, Projekt "thorough-perfection"; Deploy automatisch bei Commit auf `main`.
| Tool | Repo / Service | Stand |
|---|---|---|
| Reporting | alpensonne-reporting | läuft; Umsatz-Abgleich Management Summary vs. ibelsa-PDF offen |
| Ankunftsliste | alpensonne-ankuenfte | läuft |
| Preis-Check | huthbenno-byte/alpensonne-preischeck | läuft; Leitfaden: Google Doc "Preis-Check_Entwicklerleitfaden" (Stand 09.10.2026) |
| Mahnwesen | offen | Stufe 1; nächste Stufe Bankabgleich FinTS |

Regeln: API-Keys nur als Railway-Variablen. Beim Preis-Check `app.py` nie komplett hochladen (Passwörter stehen nur in der GitHub-Version).

**Ansprechpartner:** Benno

**Abhängigkeiten:**
- nutzt: ibelsa-API, DIRS21-IBE (inoffiziell), `stammdaten/raten/mapping.yaml`
- Bei Änderungen an Saisons, Kinderpreisen, Raten oder Kategorien: Pflegeaufgaben im jeweiligen Tool prüfen
