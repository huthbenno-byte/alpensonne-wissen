# Einschätzung: Wechsel weg von aobis (Stand 03.11.2026)

## Kurzfazit
1. **Ein Wechsel ist machbar und sinnvoll.** Die Umgebung ist klein (4 Benutzer, 4 Geräte), die Fachanwendungen laufen in der Cloud und die Technik ist Standard. Jeder regionale Managed-Service-Anbieter kann das übernehmen.
2. **Er geht aber nicht auf einen Schlag.** Die Verträge binden gestaffelt bis 06/2027, 11/2027, 05/2028, 12/2028 und 05/2029 (siehe `vertraege.md`). Realistisch ist ein Wechsel in 3–4 Wellen, mit 2027 als Hauptjahr.
3. **Der größte Sparhebel ist nicht der Anbieterwechsel, sondern die Verschlankung.** Zwei gehostete Server mit Terminalserver, Managed LAN, 500 GB Online-Backup und ein Hochverfügbarkeits-Firewall-Cluster sind für ein Hotel mit 4 Benutzern und reinen Cloud-Anwendungen sehr wahrscheinlich überdimensioniert.
4. **Telefonie auslagern: ja, aber nicht als das Einfachste und nicht früh.** CloudPhone läuft bis 30.04.2028 (Kündigung bis 31.01.2028) und verlängert sich sonst um **24 Monate**. Technisch ist der Wechsel einfach, vertraglich ist er der zweitlängste Brocken.
5. **Es fehlen noch die Ist-Kosten.** Ohne Monatsbeträge je Vertrag lässt sich weder die Ersparnis beziffern noch ein Angebot bewerten. Das ist der erste Schritt.

## Fahrplan
| Welle | Zeitpunkt | Was | Voraussetzung |
|---|---|---|---|
| 0 – Datenbasis | Nov–Dez 2026 | Rechnungen der letzten 3 Monate, Vertragstexte AGL-*, Inventarliste (gemietet/gekauft), Paketstufe Client, Inhaber von Tenant, Domain und Rufnummern | Anfrage an aobis. **Bis dahin nichts Neues bei aobis unterschreiben**, jede Bestellung kann Laufzeiten verlängern |
| 1 – Ausschreibung | Mitte Jan 2027 versenden, Angebote bis Mitte Feb | Lose 1–3, Telefonie getrennt (siehe unten) | Entscheidung zu Los 1 vor dem **28.02.2027** |
| 2 – Arbeitsplätze, M365, Backup | Übergang 01.06./01.07.2027 | Clients, Benutzer, M365 (CSP-Partnerwechsel, keine Tenant-Migration), E-Mail-Sicherheit, M365-Backup | Kündigung 440 bis 28.02., 439 bis 31.05. |
| 3 – Server und WLAN | Übergang 01.11.2027 | Server ablösen (Entra ID / Intune statt DC + RDS), Backup neu aufsetzen, WLAN-Erweiterung | Kündigung 1172 bis **30.04.2027**, 754 bis 31.07.2027. Klären, ob APs gemietet sind und zurückgehen, sonst Ersatz bis 31.10. |
| 4 – Telefonie | Übergang 01.05.2028 | Cloud-Telefonanlage bei einem Spezialanbieter, Endgeräte kaufen, Rufnummern portieren, Audavo-Weiterleitung umziehen | Kündigung 357 bis **31.01.2028** |
| 5 – Netzwerk-Rest | 12/2028 bzw. 05/2029 | MBIT-Hardware, Netzwerk Apartments | Ablöse vorher verhandeln oder bis Laufzeitende behalten |

## Frühere Lösungen: sparen, bevor die Verträge enden
1. **Nachverhandeln mit aobis, mit der Ausschreibung im Rücken (stärkster Hebel, sofort).** Offen kommunizieren, dass ausgeschrieben wird. Konkret fordern:
   - Preisreduktion auf die Monatspositionen ab sofort, alternativ ein Gegenangebot zu Variante A der Ausschreibung
   - **Aufhebungsvereinbarung** für den Server-Vertrag (754), sobald die Server durch M365/Intune abgelöst sind, statt bis 10/2027 doppelt zu zahlen
   - Ablösepreis (Restwert) für die Hardware aus 1371 und 1514, damit Los 2 nicht bis 2029 blockiert ist
2. **Lizenzen bereinigen (Sofortmaßnahme).** Die 3 Business-Standard-Lizenzen dienen laut Ausschreibung u. a. für Funktions-/Shared-Postfächer. Freigegebene Postfächer in Exchange Online brauchen bis 50 GB **keine Lizenz**. Prüfen, welche der 3 wirklich Personen gehören. Mögliche Ersparnis: rund 12 € je Lizenz und Monat (Listenpreis, Rabatte über aobis unbekannt).
3. **Backup-Menge prüfen.** Was liegt in den 500 GB? Wenn das hauptsächlich die Server sind, schrumpft die Menge mit deren Ablösung. Der Vertrag hat nur 1 Monat Frist und ist damit der flexibelste.
4. **Firewall-Cluster hinterfragen.** Für diese Betriebsgröße reicht in der Regel eine Firewall mit LTE/5G-Backup-Leitung. Ein Cluster heißt doppelte Miete und doppelte Lizenz.
5. **Vorsorglich fristgerecht kündigen.** Kündigungen zu den Terminen 2027 vorsorglich aussprechen, auch wenn noch nicht feststeht, ob man wechselt. Ein neuer Vertrag mit aobis zu besseren Konditionen bleibt möglich. Risiko: Fällt die Kündigung durch und es gibt keinen Nachfolger, endet der Service. Deshalb nur zusammen mit dem Fahrplan oben.

## Telefonie: Vorschlag
- **Aus der IT-Ausschreibung herausnehmen** (Los 4 streichen) und Mitte 2027 separat 2–3 Angebote von Cloud-Telefonanbietern einholen (z. B. sipgate, Placetel, NFON, easybell, Telekom CloudPBX). Bei 3 Nebenstellen ist das ein Standardprodukt, ein IT-Dienstleister schlägt nur Marge auf.
- Anforderungen: Rufnummernportierung, Gruppen, Ansagen und Zeitsteuerung, **SIP-Weiterleitung an Audavo** (vorher mit Audavo klären, welche Anbieter getestet sind), DECT für die Rezeption.
- **Endgeräte kaufen statt mieten** (Größenordnung 80–200 € je Gerät, DECT-Basis 150–300 €). Das amortisiert sich gegenüber Miete meist nach 1–2 Jahren.
- Vorher klären: Wer ist Anschlussinhaber der Rufnummern? Gehen die Nummern bei aobis/CloudPhone auf Hotelplan? Ohne das ist keine Portierung möglich.

## Änderungen an der Ausschreibung (Entwurf Oktober 2026)
1. **Los 4 Telefonie streichen** bzw. als „späteres separates Verfahren“ erwähnen.
2. **Übergangstermine je Los nennen** statt „[Monat JJJJ]“: Los 1 = 01.06.2027, Los 3 = 01.11.2027, Los 2 = gestaffelt (WLAN-Erweiterung 11/2027, übrige Netzwerk-Hardware 12/2028 und 05/2029, Ablöse in Verhandlung).
3. **Bindefrist**: 90 Tage reichen nicht für Übergänge im November 2027. Preisgarantie bis mindestens 31.12.2027 verlangen.
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
