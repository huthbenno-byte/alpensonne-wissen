# aobis Managed Service Paket „Client“ (V3.00): Kernpunkte

Quelle: `quellen/aobis_Leistungsbeschreibung_Paket_Client_V3.00.pdf` (5 Seiten). Es gibt die Stufen Basic, Standard und Premium. **Welche Stufe wir haben, ist offen.**

## Was enthalten ist
- Fernwartung, Inventarisierung, monatlicher Bericht, technische Dokumentation „laut aobis-Standard“
- Windows-Sicherheitsupdates (kritisch/wichtig), automatisch ohne vorherige Prüfung
- Managed Antivirus / EDR, Monitoring (täglich / 60 Min. / 30 Min. je nach Stufe)
- Standard/Premium: 1x jährlich Vor-Ort-Check inkl. Anfahrt, Beratungsgespräch (jährlich/halbjährlich)
- Bitlocker-Verschlüsselung (Schlüssel liegen bei aobis)
- Optionen: Flatrate Support/Administration, Cloud-Backup je 100 GB, SOC

## Schwachstellen für einen Hotelbetrieb
| Punkt | Was drin steht | Warum das für uns schwach ist |
|---|---|---|
| Servicezeit | Mo–Fr 8:30–17:30 | Rezeption, Gäste-WLAN und SALTO laufen 24/7, am Wochenende ist kein Support zugesagt |
| „Kritisch“ | erst ab Arbeitsausfall für **mehr als 5 Personen** oder deutlicher Beeinträchtigung von Kernprozessen | Wir haben 4 Benutzer, die Personen-Schwelle greift bei uns nie |
| Reaktionszeit kritisch | 24 h (Basic), 8 h (Standard), 4 h (Premium), nur innerhalb der Servicezeit | Freitag 17:00 gemeldet bedeutet bei Basic einen Beginn erst am Montag |
| Reaktionszeit unkritisch | 48 h | – |
| Flatrate-Option | ohne Drucker, Scanner, Switche, NAS, Schulungen, Change Requests; Anfahrt extra | Was „Change“ ist, entscheidet aobis, dadurch viel Spielraum für Zusatzrechnungen |
| Backup-Verfügbarkeit | 98,5 % im Jahresmittel, abzüglich Wartung | erlaubt rund 5 Tage Ausfall pro Jahr |
| Backup-Mehrmenge | 0,75 € netto je angefangenem GB über dem Paket | – |
| Voraussetzung | Hardware max. 5 Jahre alt, Software mit Herstellersupport | ältere Geräte können als Hebel für Neukäufe dienen |
| Inhalt | Defragmentierung, Bereinigung von Temp-Dateien, Flash/Java/IE | veraltete Positionen, die als Leistung zählen |
| Formales | verweist auf „Ziffer 11“ für Interventionszeiten, gemeint ist Ziffer 9 | Dokument ist nicht sauber gepflegt |

## Lock-in-Punkte: vor dem Wechsel zwingend herausverlangen
- **Administrator-Kennwörter**: liegen laut Vertrag nur bei aobis, wir dürfen sie nur versiegelt im Tresor haben
- **Bitlocker-Wiederherstellungsschlüssel** aller Geräte
- **Microsoft-365-Tenant**: globaler Admin muss bei uns liegen. Lizenzen laufen vermutlich über aobis als CSP-Partner; ein Partnerwechsel ist möglich, ohne den Tenant zu migrieren
- Technische Dokumentation, Netzwerkplan, Firewall- und Switch-Konfiguration, WLAN-/Hotspot-Konfiguration
- Domain/DNS (wer ist Inhaber und wer verwaltet?), Rufnummern (wer ist Anschlussinhaber?)
- Zugriff auf die Backup-Daten bzw. deren Export vor Vertragsende
