# Learnings

- FAQ-Inhalte existieren mehrfach: eigene FAQ-Seiten (hotel-faq, apartment-faq) UND Toggle-Widgets auf den Zimmerseiten (hotel-zimmer, apartment-zimmer) sowie ein Textblock auf der Apartment-Startseite. Änderungen immer an allen Stellen machen.
- Seiten-IDs: apartment 1134, apartment-zimmer 1517, apartment-faq 2141, apartment-agb 2145, hotel-zimmer 1060, hotel-faq 1166, hotel-agb 945.
- Zuverlässiger Weg für Textänderungen: Elementor-Editor öffnen, Element per elementor.getContainer(id) holen, $e.run('document/elements/settings'), dann $e.run('document/save/publish'). Danach öffentliche Seite gegenprüfen.
- WordPress-Login macht Benno selbst (Strato-Login).
