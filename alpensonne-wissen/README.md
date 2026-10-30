# Alpensonne Wissen

Zentrale Wissensbasis für die Alpensonne Tegernsee (Hotel und Apartments).
Systemlandkarte: https://claude.ai/artifact/GaJae1y5Z6heYMGfeyDuKh

## Prinzip
Stammdaten sind die eine Wahrheit. ibelsa, DIRS21, Kanäle, COM25, MARA und die Website werden dagegen gepflegt und geprüft.

## Module
| Ordner | Inhalt |
|---|---|
| stammdaten/ | Basisdaten, Kategorien, Ausstattung, Policies, Raten |
| pms-ibelsa/ | ibelsa: Ratenpläne, Importe, API |
| channel-manager-dirs21/ | DIRS21: Mapping, Konditionen, IBE |
| kanaele/ | Eine Datei pro OTA/Partner |
| gaeste/ | COM25, MARA, Tone of Voice, Straiv, Audavo, Brevo |
| tools/ | Verweise auf die App-Repos (Reporting, Ankünfte, Preis-Check, Mahnwesen) |
| web/ | Websites, Landingpages, KI-Sichtbarkeit |
| finanzen/ | Budget, Steuerbüro, Archiv |
| betrieb/ | SALTO, IT, Housekeeping, Bauprojekte, Personal-/Organisationskonzepte |
| logbuch/ | Monatliches Änderungsprotokoll |
| _vorlage/ | Bauplan für neue Module |

## Neues Modul
`_vorlage/` kopieren, umbenennen, hier in die Tabelle eintragen.

## Regeln
- Keine Passwörter, API-Keys oder Zugangsdaten im Repo.
- Status je Fakt: bestaetigt, website, offen, konflikt.
