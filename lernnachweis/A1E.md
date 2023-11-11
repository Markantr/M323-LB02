# Lernnachweis zur Kompetenz A1E

## Kompetenz: A1E - Ich kann aufzeigen, wie Probleme in den verschiedenen Konzepten (OO, prozedural und funktional) gelöst werden und diese miteinander vergleichen

### Themenschwerpunkt: Implementierung von Event-Details-Abfrage in verschiedenen Programmierstilen

---

#### Einführung und Zielsetzung

In meiner Flask-Webanwendung habe ich ein Feature zur Abfrage von Event-Details in drei verschiedenen Programmierstilen implementiert: objektorientiert (OO), prozedural und funktional. Mein Ziel war es, die Unterschiede und Anwendungsfälle jedes Stils zu veranschaulichen.

---

### Umsetzung und Vergleich der Programmierstile

#### 1. Objektorientierter Ansatz (OO)

- **Endpunkt**: `/oo/event/<int:event_id>`
- **Umsetzung**: Nutzung einer Klasse `EventDetailsController` mit einer Methode `get_event_details`.
- **Vorteile**: Kapselung der Logik und Zustandsmanagement in Objekten, gute Modularität und Wiederverwendbarkeit.

#### 2. Prozeduraler Ansatz

- **Endpunkt**: `/procedural/event/<int:event_id>`
- **Umsetzung**: Direkte Implementierung der Logik in einer Funktion `get_event_details_procedural`.
- **Vorteile**: Einfachheit und Klarheit, geeignet für lineare und strukturierte Abläufe.

#### 3. Funktionaler Ansatz

- **Endpunkt**: `/functional/event/<int:event_id>`
- **Umsetzung**: Einsatz einer Lambda-Funktion in `query_event`, die eine reine Funktion darstellt.
- **Vorteile**: Förderung der Unveränderlichkeit und Reduzierung von Seiteneffekten, erhöht Vorhersagbarkeit und Wiederverwendbarkeit.

---

### Lernprozess und Reflexion

Durch die Implementierung des gleichen Features in unterschiedlichen Programmierstilen konnte ich ein tiefes Verständnis für die Stärken und Einschränkungen jedes Stils erlangen. Diese Erfahrung hat mir gezeigt, wie die Wahl des Programmierstils basierend auf den spezifischen Anforderungen eines Projekts getroffen werden kann.

---

### Zukünftige Schritte

Ich plane, diese Erkenntnisse zu nutzen, um in zukünftigen Projekten die geeignetsten Programmierstile und -muster zu wählen. Insbesondere bin ich daran interessiert, wie man diese Stile in komplexen Anwendungen kombinieren kann, um die Vorteile jedes Ansatzes optimal zu nutzen.

Die Erfahrung, die ich durch die Anwendung dieser verschiedenen Programmierstile gesammelt habe, wird mir helfen, flexibler und effektiver bei der Entwicklung von Software zu sein.
