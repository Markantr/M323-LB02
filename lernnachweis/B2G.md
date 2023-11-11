# Lernnachweis zur Kompetenz B2G

## Kompetenz: B2G - Ich kann Funktionen als Objekte behandeln und diese in Variablen speichern und weitergeben.

### Themenschwerpunkt: Funktionale Programmierung umsetzen

---

#### Einführung und Zielsetzung

In der Entwicklung meiner Flask-Webanwendung habe ich Funktionen als Objekte behandelt, indem ich sie in Variablen gespeichert und übergeben habe. Dieser Ansatz ermöglicht eine flexible Verwendung von Funktionen und fördert die Wiederverwendbarkeit des Codes.

---

### Umsetzung der Kompetenz in Flask

#### Funktionen als Erste-Klasse-Bürger

- **Konzept**: In Python sind Funktionen "Erste-Klasse-Bürger", was bedeutet, dass sie wie jedes andere Objekt behandelt werden können. Sie können in Variablen gespeichert, als Argumente an andere Funktionen übergeben oder von Funktionen zurückgegeben werden.
- **Anwendung im Code**: Ich habe eine Funktion definiert und sie einer Variablen zugewiesen, um zu demonstrieren, wie sie in anderen Teilen der Anwendung wiederverwendet werden kann.

#### Beispiel-Implementierung

```python
# Funktion in einer Variablen speichern
format_event_variable = format_event

# Verwendung der Funktion über die Variable
@event_bp.route('/formatted_events_variable', methods=['GET'])
def get_formatted_events_variable():
    events = Event.query.all()
    formatted_events = [format_event_variable(e) for e in events]
    return jsonify(formatted_events)
 ```

Beschreibung: Im obigen Beispiel wird die format_event-Funktion einer Variablen format_event_variable zugewiesen. Diese Variable wird dann verwendet, um die Funktionalität in einem anderen Kontext anzuwenden, was die Flexibilität und Wiederverwendbarkeit der Funktion demonstriert.

---

### Lernprozess und Reflexion

Die Arbeit mit Funktionen als Objekten hat meine Sichtweise auf die Strukturierung von Code und die Erstellung wiederverwendbarer Komponenten erweitert. Ich habe gelernt, wie wichtig es ist, Funktionen flexibel zu gestalten, sodass sie in verschiedenen Kontexten der Anwendung genutzt werden können.

---

### Zukünftige Schritte

Diese Erfahrung hat mein Interesse an funktionaler Programmierung und insbesondere an der Verwendung von Funktionen als flexible, wiederverwendbare Objekte geweckt. In zukünftigen Projekten plane ich, diesen Ansatz weiter zu verfolgen, um die Effizienz und Flexibilität meiner Anwendungen zu verbessern.

Die Umsetzung von B2G hat mein Verständnis für die Möglichkeiten der funktionalen Programmierung in Python vertieft und wird mein zukünftiges Software-Design positiv beeinflussen.