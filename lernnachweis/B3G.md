# Lernnachweis zur Kompetenz B3G

## Kompetenz: B3G - Ich kann einfache Lambda-Ausdrücke schreiben, die eine einzelne Operation durchführen

### Themenschwerpunkt: Funktionale Programmierung umsetzen

---

#### Einführung und Zielsetzung

In der Entwicklung meiner Flask-Event-App habe ich einfache Lambda-Ausdrücke genutzt, um Datenmanipulationen durchzuführen. Dies ermöglichte eine kompakte und effiziente Codierung für einfache Operationen.

---

### Umsetzung der Kompetenz in Flask

#### Anwendung von Lambda-Ausdrücken

- **Konzept**: Ein Lambda-Ausdruck in Python ermöglicht es, anonyme Funktionen zu definieren. Dies ist besonders nützlich für kleine, einmalige Funktionen.
- **Anwendung im Code**: Ich habe Lambda-Ausdrücke verwendet, um das Datum von Events in einen formatierten String umzuwandeln.

#### Beispiel-Implementierung

```python
format_date = lambda event: event.date.strftime('%Y-%m-%d')

@event_bp.route('/format_dates', methods=['GET'])
def format_event_dates():
    events = Event.query.all()
    formatted_dates = list(map(format_date, events))
    return jsonify(formatted_dates)
```

---

### Lernprozess und Reflexion

Die Nutzung von Lambda-Ausdrücken für einfache Aufgaben wie das Formatieren von Daten hat die Code-Effizienz in meiner Flask-App erhöht. Es hat mir ermöglicht, Funktionen direkt dort zu definieren, wo sie benötigt werden, ohne separate benannte Funktionen erstellen zu müssen.

---

### Zukünftige Schritte

Ich plane, Lambda-Ausdrücke weiterhin für kleine Aufgaben einzusetzen, um die Klarheit und Kompaktheit meines Codes zu verbessern. Dies wird besonders nützlich sein, wenn ich mit höherwertigen Funktionen arbeite, die kleine Callback-Funktionen erfordern.

Die Erfahrungen mit B3G haben meine Fähigkeiten in der funktionalen Programmierung erweitert und werden meine zukünftige Arbeit in Python bereichern.
