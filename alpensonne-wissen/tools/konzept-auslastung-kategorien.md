# Konzept: Auslastungsbericht auf Kategorieebene

**Ziel:** Entscheidungsgrundlage für die Renovierung. Welche Kategorien sind am besten ausgelastet, und wo fehlen Zimmer?
**Umsetzung in:** Repo `alpensonne-reporting`, neuer Tab "Kategorien" im Auslastungsbericht
**Stand:** 09.11.2026, umgesetzt in `alpensonne-reporting` (Branch `claude/friendly-rubin-l7kgp1`, noch nicht auf main/live): Modul `reports/auslastung_kategorien.py`, Tabs "Kategorien" und "Kategorien je Monat".

## Grundsatz
Hotel (01–06) und Apartments (07–09) werden **immer getrennt** ausgewertet: eigene Tabelle, eigene Summenzeile. Keine gemeinsame Gesamtsumme.

## Zimmerbestand (Quelle: `stammdaten/kategorien.yaml`, ibelsa 09.11.2026)
| Bereich | Kat. | Kurzname | Zimmer |
|---|---|---|---|
| Hotel | 01 | EZB | 3 |
| Hotel | 02 | DZM | 13 |
| Hotel | 03 | DZ | 12 |
| Hotel | 04 | DZB | 17 |
| Hotel | 05 | JAP | 3 |
| Hotel | 06 | APP | 3 |
| **Hotel gesamt** | | | **51** |
| Apartments | 07 | APP1 | 10 |
| Apartments | 08 | APPM | 10 |
| Apartments | 09 | APP2 | 4 |
| **Apartments gesamt** | | | **24** |

## Kennzahlen je Kategorie (Zeitraum frei wählbar, Ansicht je Monat oder Saison)
| Kennzahl | Formel | Wofür |
|---|---|---|
| Verfügbare Zimmernächte | Zimmer × Tage (abzgl. Sperren/Out of Order) | Basis |
| Belegte Zimmernächte | belegte Nächte in der Kategorie | Basis |
| Auslastung % | belegt / verfügbar | Grundvergleich |
| Durchschnittspreis pro belegter Nacht | Logisumsatz / belegte Nächte | Zahlungsbereitschaft |
| Umsatz pro verfügbarem Zimmer | Logisumsatz / verfügbare Nächte | Ertragskraft je Zimmer, fair zwischen großen und kleinen Kategorien |
| Ausverkaufte Tage | Tage mit 100 % Belegung in der Kategorie | stärkster Hinweis auf fehlende Zimmer |
| Upgrades | Buchungen mit gebuchter ≠ belegter Kategorie | verfälschen sonst die Nachfrage |
| Ø Aufenthaltsdauer, Ø Personen je Zimmer | | Gästestruktur je Kategorie |

**Gebuchte und belegte Kategorie:** Die Nachfrage wird nach der gebuchten Kategorie gezählt, die Auslastung nach der belegten. Beides wird angezeigt.

## Lesehilfe für die Renovierungsfrage
- Hohe Auslastung **und** viele ausverkaufte Tage **und** ein hoher Durchschnittspreis: Kandidat für mehr Zimmer.
- Geringe Auslastung, die nur über Upgrades oder Rabatte zustande kommt: Kandidat für Umbau oder Zusammenlegung.
- Kategorien mit 3 Zimmern (01, 05, 06) sind schnell "ausverkauft". Hier ausverkaufte Tage immer zusammen mit der absoluten Zahl der Zimmer lesen.

## Datenquelle
ibelsa (Belegung, Reservierungen, Zimmerkategorie je Zimmer). Zu prüfen ist, ob der Bericht die gebuchte Kategorie und Sperren schon abruft.
