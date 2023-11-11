# Lernnachweis zur Kompetenz B3E

## Kompetenz: B3E - Ich kann Lambda-Ausdrücke verwenden, um den Programmfluss zu steuern, z.B. durch Sortieren von Listen basierend auf benutzerdefinierten Kriterien

### Themenschwerpunkt: Funktionale Programmierung umsetzen

---

#### Einführung und Zielsetzung

In der Weiterentwicklung meiner Flask-Event-App habe ich Lambda-Ausdrücke verwendet, um den Programmfluss zu steuern. Besonders habe ich mich auf das Sortieren von Listen basierend auf benutzerdefinierten Kriterien konzentriert.

---

### Umsetzung der Kompetenz in Flask

#### Anwendung von Lambda-Ausdrücken zur Steuerung des Programmflusses

- **Konzept**: Lambda-Ausdrücke können effektiv eingesetzt werden, um Operationen wie Sortierung oder Filterung in einer funktionalen und kompakten Weise durchzuführen.
- **Anwendung im Code**: Ich habe Lambda-Ausdrücke verwendet, um eine Liste von Events basierend auf verschiedenen Kriterien zu sortieren.

#### Beispiel-Implementierung

```python
sort_events_by_name = lambda events: sorted(events, key=lambda event: event.name)

sort_events_by_date = lambda events: sorted(events, key=lambda event: event.date)

@event_bp.route('/sorted_events', methods=['GET'])
def get_sorted_events():
    sort_criteria = request.args.get('sort_by', 'name')
    events = Event.query.all()
    if sort_criteria == 'date':
        sorted_events = sort_events_by_date(events)
    else:
        sorted_events = sort_events_by_name(events)
    return jsonify([e.to_di
```

---

### Lernprozess und Reflexion

Durch den Einsatz von Lambda-Ausdrücken zur Steuerung des Programmflusses habe ich gelernt, wie leistungsstark und flexibel diese in Python sein können. Die Fähigkeit, schnell und einfach benutzerdefinierte Sortier- und Filterfunktionen zu erstellen, hat die Entwicklung und Wartung meiner App erheblich vereinfacht.

---

### Zukünftige Schritte

Ich plane, die Verwendung von Lambda-Ausdrücken weiter zu erforschen, um komplexe Programmflusssteuerungen in meiner Flask-App zu implementieren. Dies wird mir helfen, effizientere und leistungsfähigere Anwendungen zu entwickeln.

Die Erfahrung mit B3E hat meine Fähigkeiten in der Softwareentwicklung erweitert und wird mir helfen, anspruchsvollere und benutzerfreundlichere Webanwendungen zu erstellen.
