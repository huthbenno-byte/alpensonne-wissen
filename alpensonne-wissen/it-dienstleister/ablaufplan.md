# Ablaufplan IT-Neuausrichtung (Stand 03.11.2026)

## Die Strategie in drei Sätzen
1. **Erst verschlanken, dann den Anbieter wählen.** 62 % der Kosten stecken in Servern und Firewall-Cluster. Die fallen weg, egal wer euch betreut.
2. **aobis bekommt zuerst die Chance, das selbst umzusetzen, und zwar früher als 10/2027.** Gleichzeitig holt ihr Vergleichsangebote ein. Das Wettbewerbsangebot ist euer Hebel.
3. **Ende Februar 2027 entscheidet ihr: Weg A oder Weg B.** Danach laufen nur noch Fristen und Umsetzung.

| | Weg A: aobis bleibt, verschlankt | Weg B: Wechsel in zwei Stufen |
|---|---|---|
| Wann | Verschlankung ab Q2 2027 | Netz + Server zum 01.11.2027, Arbeitsplätze zum 01.12.2028 |
| Vorteil | keine Übergabe, keine zwei Dienstleister parallel | bessere Servicezeiten, Neustart ohne Altlasten |
| Nachteil | Abhängigkeit bleibt | 13 Monate zwei Dienstleister (aobis behält MBIT bis 11/2028) |
| Bedingung | aobis setzt Server-Ablösung und Einzel-Firewall vor 10/2027 um, verkürzt Laufzeiten, sagt Wochenend-Störungsdienst zu und liegt höchstens ca. 10 % über dem besten Angebot | aobis lehnt ab oder ist deutlich teurer |

---

## Phase 1: Datenbasis und Vorbereitung (bis 27.11.2026)

| Bis | Was | Wer |
|---|---|---|
| 13.11. | **E-Mail an aobis**: Unterlagen anfordern (Entwurf unten) und Gesprächstermin für KW 49/50 erbitten | Benno |
| 13.11. | **Alle Kündigungstermine in den Kalender** mit 3 Wochen Vorlauf (Liste unten) | Benno |
| 20.11. | Intern klären: Wer arbeitet noch auf dem Terminalserver, und wofür? Welche Dateien liegen auf den Servern? | Benno + Rezeption/Büro |
| 20.11. | **Wo läuft die SALTO-Software (ProAccess Space)?** Lokal, auf dem Terminalserver oder in der Cloud? Das ist die wichtigste technische Frage vor jeder Server-Ablösung | Benno, ggf. SALTO-Support |
| 20.11. | Welche der 3 Business-Standard-Postfächer sind Personen, welche Sammelpostfächer (info@, rezeption@ …)? | Benno |
| 27.11. | Inhaber prüfen: M365-Tenant (globaler Admin), Domains/DNS, Rufnummern | Benno (Registrar-Login, Telefon-Vertrag) |
| 27.11. | **Bieter-Shortlist** mit 4–6 Firmen (siehe „Wen anfragen“) und erster kurzer Anruf: Interesse, Kapazität, Hotelreferenzen | Benno |

**Ab sofort gilt:** Nichts Neues bei aobis bestellen oder unterschreiben, ohne dass schriftlich steht „keine Laufzeitverlängerung bestehender Verträge“. Die beiden Verträge aus 2025/2026 haben die Bindung jeweils um 3 Jahre verlängert.

## Phase 2: Gespräch mit aobis (KW 49/50, bis 11.12.2026)

Persönliches Gespräch mit der Geschäftsführung bzw. dem Account-Verantwortlichen. Ton: sachlich, fair, klar. Ihr seid nicht im Streit, ihr kauft neu ein.

### So platzieren
**Einstieg (Rahmen setzen):**
> „Wir zahlen knapp 18.000 € netto im Jahr für 4 Arbeitsplätze. Unsere Anwendungen laufen inzwischen komplett in der Cloud. Das steht nicht mehr im Verhältnis. Wir holen deshalb Anfang 2027 Vergleichsangebote ein, möchten euch aber vorher die Möglichkeit geben, ein Konzept vorzulegen.“

Ausschreibung **erwähnen, aber keine Termine und keine Mitbewerber nennen**. Nicht sagen, dass ihr ohnehin bis 2028 an MBIT gebunden seid. Das wissen sie selbst.

**Die Themen in dieser Reihenfolge:**

| # | Thema | Eure Forderung | Argument |
|---|---|---|---|
| 1 | **Server ablösen** (565 €/Mon.) | Konzept + Festpreis für die Ablösung von DC und Terminalserver durch Entra ID / Intune / SharePoint, **Vertrag 754 endet mit der Umstellung**, Ziel 30.04.2027 | Business Premium (Entra ID, Intune) zahlt ihr schon über MBIT, das ist doppelte Infrastruktur |
| 2 | **Firewall-Cluster** (360 €/Mon.) | Begründung für Hochverfügbarkeit oder Tausch gegen ein Einzelgerät mit LTE/5G-Backup, neuer Preis ab Q2 2027 | Ein Cluster für 4 Arbeitsplätze ist überdimensioniert, eine Internet-Störung trifft euch ohnehin |
| 3 | **Backup 500 GB** (107 €/Mon.) | Aufstellung, was gesichert wird; Wegfall bzw. Reduktion mit den Servern | M365-Backup ist schon in E-Mail Protection enthalten |
| 4 | **3x Business Standard** (48 €/Mon.) | Umstellung auf freigegebene Postfächer zum nächstmöglichen Termin | Microsoft verlangt dafür keine Lizenz |
| 5 | **Laufzeiten** | Alle Verträge auf ein **gemeinsames Enddatum** bringen (z. B. 30.11.2028) mit 12 Monaten Verlängerung und 3 Monaten Frist; Telefonie nicht mehr 24 Monate | Planbarkeit; Voraussetzung, dass ihr bleibt |
| 6 | **Servicezeiten** | Störungsdienst Priorität 1 auch am Wochenende/Feiertag für Rezeption, Internet, WLAN, SALTO, unabhängig von „mehr als 5 Personen“ | Hotelbetrieb läuft 7 Tage, die Definition „kritisch“ greift bei 4 Benutzern nie |
| 7 | **Transparenz / Notfallzugang** | Notfall-Admin-Zugang für M365 bei euch, Export der Bitlocker-Schlüssel, aktuelle Netzwerkdokumentation | „Für unsere Notfalldokumentation“: legitim, egal wie ihr entscheidet |
| 8 | **Klärungen** | Was beinhalten 1514 (Netzwerk Apartments, nicht auf der Rechnung) und 1371 („Hardwaresetup“)? Gemietet oder gekauft? | Grundlage für jede Entscheidung |

**Abschluss:** Schriftliches Angebot bis **15.01.2027** erbitten, mit Monatspreisen vorher/nachher, Einmalkosten und Umsetzungstermin.

**Nicht im Gespräch zusagen:** keine neue Laufzeit, keine Unterschrift. „Wir prüfen das zusammen mit den anderen Angeboten.“

**Was realistisch ist:** Server-Ablösung und Einzel-Firewall bringen aobis weniger Umsatz. Erwartet ein Gegenangebot mit Rabatten statt echter Verschlankung. Genau dafür braucht ihr die Vergleichsangebote.

## Phase 3: Ausschreibung (Dezember 2026 bis Februar 2027)

| Bis | Was |
|---|---|
| 18.12.2026 | Ausschreibung überarbeiten (Änderungen siehe `einschaetzung-wechsel.md`; mache ich gerne). Ergänzen: Ist-Kosten **nicht** nennen, aber Mengen und Laufzeiten je Los; Variante B (Server ablösen, Einzel-Firewall) ausdrücklich bevorzugt |
| 15.01.2027 | **Versand** an 4–6 Bieter |
| 15.–29.01. | Vor-Ort-Besichtigungen (1–2 Stunden je Bieter, einen Termin pro Bieter anbieten) |
| 29.01. | Frist für Rückfragen |
| 12.02. | **Angebotsfrist** |
| 15.–19.02. | Auswertung (Preisblatt-Zusammenfassung + Bewertungsmatrix), aobis-Angebot daneben legen |
| 19.–24.02. | Bietergespräche mit den besten 2 (je 1 Stunde), letzte Verhandlungsrunde mit aobis |
| **24.02.2027** | **Entscheidung Weg A oder B** |

## Phase 4: Fristen und Umsetzung (2027–2029)

Kündigungen immer **nachweisbar** (Einschreiben mit Rückschein oder E-Mail mit Eingangsbestätigung) und spätestens zum Versanddatum unten:

| Versand bis | Frist | Vertrag | Was | Weg A | Weg B |
|---|---|---|---|---|---|
| **12.02.2027** | 28.02.2027 | 440 Office 365 (3x Standard) | kündigen bzw. auf Sammelpostfächer umstellen | ✔ | ✔ |
| **09.04.2027** | 30.04.2027 | 1172 Firewall, Switches, APs | kündigen (6 Monate Frist!) | wenn neuer Preis nicht schriftlich steht | ✔ |
| **10.05.2027** | 31.05.2027 | 439 Online Backup | kündigen | ✔ (sofern Server wegfallen) | ✔ |
| **09.07.2027** | 31.07.2027 | 754 Server | kündigen | ✔ (falls nicht schon aufgehoben) | ✔ |
| **10.01.2028** | 31.01.2028 | 357 Telefonie | kündigen, sonst +24 Monate | ✔ (neuer Vertrag mit 12 Monaten) | ✔ |
| **10.08.2028** | 31.08.2028 | 1371 MBIT | kündigen | – | ✔ |
| **10.01.2029** | 31.01.2029 | 1514 Netzwerk Apartments | je nach Inhalt | – | ✔ |

Bei Weg A sind die Kündigungen 1172/439/754 **vorsorglich**: Ihr kündigt, und aobis bietet die verschlankte Lösung als neuen Vertrag an. Das funktioniert nur, wenn die Nachfolgelösung rechtzeitig steht.

**Umsetzung Server-Ablösung (beide Wege):** März–Juni 2027 Konzept und Migration (Benutzer in Entra ID, Geräte in Intune, Dateien nach SharePoint/OneDrive, SALTO-Frage gelöst), Juli–August Parallelbetrieb, spätestens 31.10.2027 Server aus. **Nicht in der Hauptsaison (Juli/August) umstellen**, wenn es sich vermeiden lässt: Ziel Mai/Juni oder Oktober/November.

**Telefonie:** Oktober–Dezember 2027 zwei bis drei Angebote einholen (Cloud-Telefonanbieter direkt und aobis), dabei Audavo-Kompatibilität prüfen. Entscheidung bis 10.01.2028. Geringe Priorität, da kaum Ersparnis.

---

## Wen anfragen

**IT-Dienstleister (4–6 Firmen).** Kriterien: Sitz max. ca. 45 Minuten von Bad Wiessee (Landkreise Miesbach, Rosenheim, Bad Tölz-Wolfratshausen, München-Süd), Microsoft-365-/Intune-Erfahrung, mindestens 2 Hotel- oder Gastro-Referenzen, idealerweise SALTO- und Hotspot-Erfahrung, Größe 5–30 Mitarbeiter (groß genug für Vertretung, klein genug, dass ihr wichtig seid).

So findet ihr sie, nach Erfolgsaussicht:
1. **Kollegen im Tegernseer Tal fragen**, wer sie betreut und ob sie zufrieden sind. Das ist die beste Quelle, weil ihr dann gleich die Referenz habt.
2. **SALTO Partnersuche** auf saltosystems.com und den SALTO-Vertrieb Deutschland fragen, welche IT-Partner im Raum Miesbach/Rosenheim Hotels betreuen.
3. Eure Softwareanbieter fragen: **ibelsa**, **Straiv**, **DIRS21**. Sie kennen IT-Dienstleister, mit denen Hotels gut fahren.
4. **DEHOGA Bayern** (Kreisverband Miesbach) und **IHK München und Oberbayern** (Firmenverzeichnis).
5. Bei der Websuche aufgetaucht, **ungeprüft**: IT NEXT GEN GmbH (Rosenheim, nennt Hotellerie als Branche) und tbs Computer-Systeme GmbH (Waakirchen, Hinweis auf Hotel-Kunden im Tal). Beide nur als Startpunkt, Referenzen selbst prüfen.

**Telefonie (erst Q4 2027):** z. B. sipgate, Placetel, NFON, easybell, Telekom CloudPBX; zusätzlich aobis zum Vergleich.

---

## Entwurf E-Mail an aobis (Phase 1)

> Betreff: Kundennr. 40927 – Unterlagen und Gesprächstermin
>
> Hallo [Name],
>
> wir bereiten gerade unsere IT-Planung für 2027 vor und möchten dazu gerne einen Termin mit Ihnen vereinbaren, idealerweise in KW 49 oder 50 bei uns im Haus.
>
> Vorab bitten wir um folgende Unterlagen bis zum 27.11.2026:
> 1. Vertragsdokumente zu AGL-2026-1514, AGL-2026-1371, AGL-2024-1172, AGL-2022-754, AGL-2022-357, AGL-2022-440 und AGL-2022-439
> 2. Leistungsumfang und Kosten des Vertrags „Netzwerk-Infrastruktur für die Apartments“ (1514), der auf den Monatsrechnungen nicht erscheint
> 3. Inventarliste aller Geräte bei uns (Firewall, Switches, Access Points, Telefone), jeweils mit Vermerk Miete oder Eigentum
> 4. Übersicht, welche Daten und Systeme im Online-Backup (500 GB) gesichert werden
> 5. Die aktuelle technische Dokumentation unserer Umgebung inkl. Netzwerkplan
> 6. Für unsere Notfalldokumentation: einen Notfall-Administratorzugang für unseren Microsoft-365-Tenant und die Bitlocker-Wiederherstellungsschlüssel unserer Geräte (bitte auf sicherem Weg, nicht per E-Mail)
>
> Vielen Dank und viele Grüße
> Benjamin Huth
