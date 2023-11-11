# Lernnachweis zur Kompetenz B2E

## Kompetenz: B2E - Ich kann Funktionen als Objekte und Argumente verwenden, um komplexe Aufgaben zu lösen (Anwenden von Closures)

### Themenschwerpunkt: Funktionale Programmierung umsetzen

---

#### Einführung und Zielsetzung

In meiner Arbeit mit der Flask-Webanwendung habe ich mich auf die Anwendung von Closures konzentriert. Closures ermöglichen es, den Kontext einer äußeren Funktion zu bewahren, während eine innere Funktion ausgeführt wird. Dies ist besonders nützlich, um Zustände in einer funktionalen Programmierungsumgebung zu verwalten.

---

### Umsetzung der Kompetenz in Flask

#### Anwendung von Closures

- **Konzept**: Eine Closure ist eine Funktion, die eine andere Funktion umschließt und dabei den Kontext der äußeren Funktion bewahrt. Dies wird oft verwendet, um einen Zustand zwischen mehreren Aufrufen der inneren Funktion zu speichern.
- **Anwendung im Code**: Ich habe eine umschließende Funktion erstellt, die eine innere Funktion zurückgibt. Die innere Funktion behält dabei den Zugriff auf die Variablen der äußeren Funktion.

#### Beispiel-Implementierung

```python
# Umschließende Funktion, die eine Closure erstellt
def event_filter_closure(criteria):
    def filter_events(events):
        return [event for event in events if criteria(event)]
    return filter_events

# Verwendung der Closure
@event_bp.route('/filtered_events', methods=['GET'])
def get_filtered_events():
    future_event_filter = event_filter_closure(lambda e: e.date > datetime.now())
    events = Event.query.all()
    future_events = future_event_filter(events)
    return jsonify([e.to_dict() for e in future_events])
```

Dieser Abschnitt zeigt die Implementierung einer Closure in einer Flask-Anwendung. Die umschließende Funktion `event_filter_closure` erstellt eine innere Funktion, die auf eine Liste von Events angewendet wird, basierend auf einem übergebenen Kriterium.

---

### Lernprozess und Reflexion

Die Erstellung und Anwendung von Closures in meiner Flask-App hat mir ein tieferes Verständnis für funktionale Programmierungskonzepte vermittelt. Ich habe gelernt, wie Closures verwendet werden können, um Zustände effizient zu verwalten und wie sie die Wiederverwendbarkeit von Funktionen fördern.

---

### Zukünftige Schritte

Durch die Erfahrung mit Closures in Flask fühle ich mich ermutigt, weiterhin fortgeschrittene Konzepte der funktionalen Programmierung zu erforschen. Mein Ziel ist es, diese Techniken in zukünftigen Projekten einzusetzen, um komplexe Probleme effizient und elegant zu lösen.

Die Arbeit an B2E hat meine Fähigkeiten in der Softwareentwicklung erweitert und wird mich dabei unterstützen, komplexere und wartbare Codebasen zu erstellen.
