# Lernnachweis zur Kompetenz A1F

## Kompetenz: A1F: Ich kann das Konzept von *immutable values* erläutern und dazu Beispiele anwenden. Somit kann ich dieses Konzept funktionaler Programmierung im Unterschied zu anderen Programmiersprachen erklären (z.Bsp. im Vergleich zu referenzierten Objekten)

### Themenschwerpunkt: Unterschiede zwischen funktionaler Programmierung und anderen Programmierparadigmen aufzeigen.

---

#### Einführung und Zielsetzung

Im Rahmen meiner Flask-Webanwendung habe ich mich mit dem Konzept der Unveränderlichkeit (Immutable Values) beschäftigt. Mein Ziel war es, die Prinzipien der funktionalen Programmierung durch die Verwendung unveränderlicher Datenstrukturen zu demonstrieren.

---

### Umsetzung von Unveränderlichkeit in Flask

Unveränderliche Datenstrukturen spielen eine wichtige Rolle in der funktionalen Programmierung, da sie die Vorhersagbarkeit und Zuverlässigkeit des Codes erhöhen. In Python können unveränderliche Datentypen wie Tupel oder `namedtuple` verwendet werden.

#### Beispiel für die Implementierung

- **Verwendung von `namedtuple` in Flask-Routen**
   - **Route**: `/immutable_events`
   - **Methode**: GET
   - **Algorithmus**: 
     - Abfragen von Event-Daten aus der Datenbank.
     - Umwandlung der Event-Daten in ein `namedtuple`, um Unveränderlichkeit zu gewährleisten.
   - **Code-Ausschnitt**:
     ```python
     from collections import namedtuple

     EventTuple = namedtuple('EventTuple', ['name', 'date', 'location', 'description'])

     @event_bp.route('/immutable_events', methods=['GET'])
     def get_immutable_events():
         events = Event.query.all()
         immutable_events = [EventTuple(e.name, e.date, e.location, e.description) for e in events]
         return jsonify([e._asdict() for e in immutable_events])
     ```

---

### Lernprozess und Reflexion

Die Arbeit mit unveränderlichen Datenstrukturen hat mir die Bedeutung der Datenintegrität in der funktionalen Programmierung nähergebracht. Durch die Verwendung von `namedtuple` konnte ich sicherstellen, dass die Event-Daten nicht verändert werden, was die Zuverlässigkeit und Vorhersagbarkeit des Codes verbessert.

---

### Zukünftige Schritte

Ich plane, die Konzepte der Unveränderlichkeit und funktionalen Programmierung weiter zu erforschen, insbesondere in Bezug auf größere und komplexere Anwendungen. Diese Prinzipien sind essenziell für die Entwicklung zuverlässiger und wartbarer Software.

Durch das Verständnis und die Anwendung von Unveränderlichkeit in meiner Flask-App habe ich einen wichtigen Aspekt der funktionalen Programmierung gelernt und freue mich darauf, dieses Wissen in zukünftigen Projekten weiter anzuwenden.
