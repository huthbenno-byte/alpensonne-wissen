# Learnings

- 
- ibelsa liefert keine feste Zuordnung Zimmernummer → Kategorie. Die belegte Kategorie wird aus der häufigsten Buchungskategorie je Zimmer abgeleitet. Daraus ergeben sich die Kategoriewechsel (gebucht ≠ belegt).
- Reservierungs-API für lange Zeiträume immer monatsweise abfragen und über die Reservierungs-ID deduplizieren (der Auslastungsbericht fragte vorher in einem Stück ab).
