# Lernnachweis zur Kompetenz B3F

## Kompetenz: B3F - Ich kann Lambda-Ausdrücke schreiben, die mehrere Argumente verarbeiten können

### Themenschwerpunkt: Funktionale Programmierung umsetzen

---

#### Einführung und Zielsetzung

In meiner Flask-Event-App habe ich Lambda-Ausdrücke eingesetzt, die mehrere Argumente verarbeiten. Diese Fähigkeit ermöglichte es mir, komplexere Operationen auf eine prägnante und effiziente Weise auszudrücken.

---

### Umsetzung der Kompetenz in Flask

#### Anwendung von Lambda-Ausdrücken mit mehreren Argumenten

- **Konzept**: Lambda-Ausdrücke in Python können mehr als ein Argument akzeptieren, was sie für eine Vielzahl von Anwendungen nützlich macht.
- **Anwendung im Code**: Ich habe einen Lambda-Ausdruck verwendet, um zu überprüfen, ob Events innerhalb eines bestimmten Zeitraums liegen.

#### Beispiel-Implementierung

```python
event_in_range = lambda event, start_date, end_date: start_date <= event.date <= end_date

@event_bp.route('/events_in_range', methods=['GET'])
def get_events_in_range():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2020, 12, 31)
    events = Event.query.all()
    filtered_events = list(filter(lambda event: event_in_range(event, start_date, end_date), events))
    return jsonify([e.to_dict() for e in filtered_events])
```

---

### Lernprozess und Reflexion

Die Verwendung von Lambda-Ausdrücken mit mehreren Argumenten hat mir ein tieferes Verständnis für die Flexibilität und Kraft der funktionalen Programmierung in Python gegeben. Es hat mir geholfen, meine Ansätze zur Datenverarbeitung und -filterung in der App zu optimieren.

---

### Zukünftige Schritte

Ich beabsichtige, Lambda-Ausdrücke weiterhin zu nutzen, um komplexe Logik in meiner Flask-App effizient zu handhaben. Mein Ziel ist es, diese Techniken zu verwenden, um meinen Code noch flexibler und ausdrucksstärker zu gestalten.

Die Erfahrung mit B3F hat meine Fähigkeiten in der Entwicklung von Webanwendungen verbessert und wird ein wertvolles Werkzeug in meinem Entwicklungsarsenal bleiben.
