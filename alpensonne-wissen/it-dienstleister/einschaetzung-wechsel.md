# Einschätzung: Wechsel weg von aobis (Stand 03.11.2026)

> **Aktualisiert 03.11.2026 nach Auswertung der Rechnungen** (`kosten-ist.md`). Den verbindlichen Ablauf beschreibt `ablaufplan.md`.

## Kurzfazit
1. **Ein Wechsel ist machbar und sinnvoll.** Die Umgebung ist klein (4 Benutzer, 4 Geräte), die Fachanwendungen laufen in der Cloud und die Technik ist Standard.
2. **Der Kostenhebel ist die Verschlankung, nicht der Anbieter.** Server (565 €) und Firewall-Cluster (360 €) machen 62 % der 1.490 €/Monat aus. Beide Verträge enden am 31.10.2027. Ziel: 400–600 €/Monat, also rund 11–13 T€ Ersparnis im Jahr.
3. **Arbeitsplätze und M365 Premium sind marktüblich bepreist** und stecken im Vertrag MBIT (1371) bis 30.11.2028. Korrektur zur ersten Einschätzung: Los 1 ist **nicht** 06/2027 wechselbar, nur die 3 Standard-Lizenzen (440).
4. **Telefonie ist günstig** (21,30 € je Nebenstelle inkl. 9 Mietgeräten). Auslagern ist möglich, spart aber kaum. Korrektur: Ein Wechsel lohnt sich nur für Unabhängigkeit oder Funktionen, nicht wegen der Kosten.
5. **Die Firewall ist im Vertrag „Erweiterung WLAN-Infrastruktur“ (1172)**, mit 6 Monaten Frist (30.04.2027).

## Frühere Lösungen
Siehe `ablaufplan.md`, Phase 2 (Gespräch mit aobis): Server-Ablösung mit vorzeitiger Aufhebung von 754, Einzel-Firewall, Backup reduzieren, Sammelpostfächer, Laufzeiten auf ein gemeinsames Ende legen.

## Telefonie
- Geringe Priorität. Q4 2027 zwei bis drei Angebote einholen (Cloud-Telefonanbieter direkt, z. B. sipgate, Placetel, NFON, easybell, plus aobis), Entscheidung bis 10.01.2028.
- Wichtig ist vor allem, die **24-monatige Verlängerung zu vermeiden** (Kündigung bis 31.01.2028).
- Anforderungen: Portierung, Gruppen, Ansagen und Zeitsteuerung, SIP-Weiterleitung an Audavo, DECT an der Rezeption.
- Vorher klären: Auf wen laufen die Rufnummern?

## Änderungen an der Ausschreibung (Entwurf Oktober 2026)
1. **Los 4 Telefonie streichen** bzw. als „späteres separates Verfahren“ erwähnen.
2. **Übergangstermine je Los nennen** statt „[Monat JJJJ]“: Los 2 (Firewall, Switches, APs) und Los 3 = 01.11.2027, Los 1 = 01.12.2028 (nur die 3 Standard-Lizenzen ab 06/2027), Netzwerk Apartments 05/2029 bzw. nach Ablöse.
3. **Bindefrist**: 90 Tage reichen nicht. Preisgarantie bis Übergang verlangen bzw. Preise für Los 1 ab 12/2028 als Richtpreis.
4. **Hinweis zu Mietgeräten** präzisieren: Welche Hardware geht zurück und wann? Das bestimmt die Einmalkosten bei Los 2.
5. **Variante B für Los 3 als bevorzugte Lösung** formulieren (Server ablösen) und Kosten für die Migration auf Entra ID / Intune als Festpreis abfragen.
6. **Reaktionszeiten hotelgerecht definieren**: Priorität 1 auch am Wochenende, unabhängig von der Anzahl betroffener Personen (genau die Lücke im aobis-Vertrag, siehe `aobis-leistungsbeschreibung-client.md`).
7. **Exit-Klausel ergänzen**: Herausgabe aller Admin-Kennwörter, Bitlocker-Schlüssel und globaler M365-Admin bei uns, ohne Zusatzkosten.
8. Eckdaten ausfüllen: E-Mail, Telefon, Fristen.

## Marktrichtwerte zur Plausibilisierung von Angeboten
Grobe Größenordnungen (netto, Stand 2026). Das sind **keine Angebote**, sie dienen nur dazu, Ausreißer zu erkennen. Microsoft-Listenpreise vor Angebotsvergleich aktuell prüfen.

| Position | Richtwert |
|---|---|
| Client-Betreuung inkl. EDR, Patch, Monitoring | 15–40 € / Gerät / Monat |
| M365 Business Premium | ca. 20–23 € / Lizenz / Monat (Listenpreis) |
| M365 Business Standard | ca. 12–13 € / Lizenz / Monat (Listenpreis) |
| E-Mail-Sicherheit + GoBD-Archiv + M365-Backup | 4–10 € / Benutzer / Monat |
| Firewall (Einzelgerät) inkl. Lizenzen und Monitoring | 40–100 € / Monat (Miete) bzw. 800–2.000 € Kauf + Lizenz |
| Switch-/AP-Monitoring | 3–10 € / Gerät / Monat |
| Cloud-Telefonie | 5–15 € / Nebenstelle / Monat inkl. Flat DE |
| Stundensatz remote / vor Ort | 85–130 € / 95–140 € |
