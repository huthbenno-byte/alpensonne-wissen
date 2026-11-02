# Raten

- `matrix-2027.yaml`: alle Preise 2027, erzeugt aus "Alpensonne Ratenmatrix 2027" (Excel) mit `tools/raten-cockpit/build.py`. Nicht von Hand ändern.
- `mapping.yaml`: je Rate ibelsa-Code → DIRS21 → Name/ID je Kanal. Bekannt: HHS, HNS und das OTA-Paket Frühstück & Wellness auf Booking.com.

## Ratenfamilien 2027
| Rate | Gilt für | Logik |
|---|---|---|
| BAR Hotel HS (HHS) | 01–06 | Wochentag und Fr/Sa getrennt |
| BAR Hotel NS (HNS) | 01–06 | alle Tage gleich |
| NonRef | alle | BAR − 5 %, nicht stornierbar, ab 60 Tage vor Anreise |
| Apartments ganzjährig | 07–09 | nur Aufenthaltsdauer: 2 N. = Basis +30 €, 3–6 N. = Basis, ab 7 N. = Basis −15 € |
| OTA-Raten | alle | Direktrate × 1,11 (Website bleibt günstigster Kanal) |
| Paket Frühstück & Wellness | 07–09 | direkt +40 € auf Standardrate, OTA = Direktpaket × 1,12, nur NS |
| ASI, Feuer & Eis | 01–03 | feste Sonderraten (Zielgruppe offen) |
| Getaway Group, Winterzauber | Hotel | Paketpreise pro Person, NS/HS getrennt |

## Widersprüche (status: konflikt)
- Saisongrenzen: AGB/Hotel-Blatt HS bis 31.10., NS ab 04.01.; Blatt "Saison & Setup" HS bis 30.10., NS ab 03.01. Cockpit rechnet nach AGB.
- Fr/Sa-Aufschlag: Steuerung +16 € (Junior Apartment) / +10 € (Apartment 06), Preistabelle +15 € (254 € / 295 €).
- Belegung: Matrix hat Preise für mehr Personen als `kategorien.yaml` erlaubt (04: 4, 05: bis 5, 06: bis 6, 07: bis 4).

## Aktionsrabatte (Stand 02.11.2026, gepflegt im Raten-Cockpit)
| Kanal | Rate | Rabatt | Hinweis |
|---|---|---|---|
| Website (DIRS21 IBE) | Apartment Standard | 14 % | Direktbuchung, immer günstigster Preis |
| Website (DIRS21 IBE) | Paket Frühstück & Wellness | 19 % | Direktbuchung Paket |
| Booking / OTAs | OTA Standard (MLS 2 N.) + NonRef | 20 % | Late Escape Deal, Aufenthalt 01.10.2026–07.01.2027 |
| Booking / OTAs | OTA-Paket Frühstück & Wellness | 25 % | Late Escape Deal, Aufenthalt 01.10.2026–07.01.2027 |

Rabatte sind untereinander nicht kombinierbar, nur mit Genius (10–15 %). Regel: Das Paket muss nach Rabatt immer teurer sein als die Standardrate (Preischeck in der Matrix, z. B. 07 / 2 Pers. / 3–6 N.: direkt 224 € vs. 243 €, OTA 231 € vs. 252 €).
