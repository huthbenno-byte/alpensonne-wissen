# Ist-Kosten aobis (Rechnungen 08/2026 und 09/2026)

Quellen: `quellen/aobis_Rechnung_RG-268577_2026-08.pdf`, `quellen/aobis_Rechnung_RG-269008_2026-09.pdf`. Status: bestaetigt.

**1.490 € netto im Monat, also rund 17.900 € netto (21.300 € brutto) im Jahr.** Beide Monate sind bis auf die Gesprächsminuten identisch (1.489,68 € / 1.490,19 €).
Die Summe der ausgewiesenen Beträge ergibt exakt die Rechnungssumme. Positionen ohne Preis sind also **im Paket enthalten (0 €)**.

## Nach Vertrag
| Vertrag | Inhalt laut Rechnung | € / Monat | Anteil | Laufzeit bis |
|---|---|---|---|---|
| AGL-2022-754 Server | DC-vServer 154,53, Terminalserver 172,72, 4 RDS-Lizenzen 53,31, Server-Betreuung 2x 108,98, 16 GB vRAM 75,84, Managed LAN 0 (-100 %) | **565,38** | **38 %** | 31.10.2027 |
| AGL-2024-1172 WLAN-Erweiterung | **Firewall-Cluster Miete 360,40**, Betreuung von 4 Switches 85,09, 4 APs mit Flatrate 28,44 | **473,93** | **32 %** | 31.10.2027 |
| AGL-2026-1371 MBIT | Client-Betreuung 4x 17,90, „Managed Business IT User“ 4x 39,90 inkl. **M365 Business Premium** und **E-Mail Protection Level 3** (Spam, Verschlüsselung, ATP, Archiv, Continuity, M365-Backup) | 231,20 | 16 % | 30.11.2028 |
| AGL-2022-439 Online Backup | 500 GB „Tier 2 (Server lokal)“, Betreuung inklusive | 106,90 | 7 % | 30.06.2027 |
| AGL-2022-357 Telefonie | 3 Nebenstellen à 21,30 inkl. Flatrate, **9 Mietgeräte inklusive**, Auslandsminuten ca. 1 € | 64,93 | 4 % | 30.04.2028 |
| AGL-2022-440 Office 365 | 3x Business Standard à 15,95 | 47,85 | 3 % | 31.05.2027 |
| AGL-2026-1514 Netzwerk Apartments | **erscheint nicht auf der Rechnung** | ? | – | 30.04.2029 |

## Einordnung
- **Server und Firewall-Cluster machen 62 % der Kosten aus** (926 €/Monat). Beide Verträge enden am 31.10.2027.
- **Die Business-Premium-Lizenzen sind schon bezahlt.** Sie enthalten Entra ID P1 und Intune, also genau das, was die Server ersetzen würde. Heute zahlt ihr also doppelt: für die Cloud-Verwaltung und für Server.
- **Arbeitsplätze/Benutzer (MBIT) liegen preislich im Markt.** 39,90 € enthalten die Premium-Lizenz (Listenpreis ca. 20–23 €) und die E-Mail-Sicherheit. Hier ist wenig zu holen, und der Vertrag läuft bis 11/2028.
- **Telefonie ist günstig.** 21,30 € pro Nebenstelle inklusive Mietgeräten. Ein Wechsel spart höchstens 20–30 €/Monat, dafür kommen ca. 1.000–1.500 € für Gerätekäufe dazu. Telefonie ist **kein Kostenhebel**.
- aobis gewährt bereits Rabatte (-15 % Server, -25 % RAM, Managed LAN -100 %). Das zeigt, dass Verhandlungsspielraum besteht.
- „Server lokal“ beim Backup: Klären, ob es vor Ort einen Server gibt (z. B. für SALTO) und was gesichert wird.

## Zielbild nach Verschlankung (Schätzung)
| Block | heute | Ziel | Annahme |
|---|---|---|---|
| Server | 565 | 0 | Ablösung durch Entra ID / Intune / SharePoint (Lizenzen vorhanden) |
| Backup | 107 | 0–20 | M365-Backup ist in E-Mail Protection enthalten; Rest nur, falls ein lokaler Server bleibt |
| Firewall | 360 | 60–100 | Einzelgerät + LTE/5G-Backup statt Cluster |
| Switches / APs | 114 | 60–110 | Betreuung bleibt |
| Arbeitsplätze / M365 Premium | 231 | 200–240 | ungefähr Marktniveau |
| 3x Business Standard | 48 | 0–48 | freigegebene Postfächer brauchen keine Lizenz |
| Telefonie | 65 | 40–65 | kaum Potenzial |
| **Summe** | **1.490** | **ca. 400–600** | |

**Ersparnis ca. 900–1.100 € im Monat, also rund 11.000–13.000 € im Jahr.** Einmalkosten: Server-Migration ca. 2.500–6.000 €, Firewall bei Kauf ca. 1.000–2.000 €. Das sind Schätzwerte, die durch Angebote zu bestätigen sind.

**Jeder Monat, den die Server und der Cluster früher als 31.10.2027 wegfallen, spart rund 800–900 €.**
