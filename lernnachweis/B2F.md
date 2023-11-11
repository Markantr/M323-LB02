# Lernnachweis zur Kompetenz B2F

## Kompetenz: B2F - Ich kann Funktionen als Argumente für andere Funktionen verwenden und dadurch höherwertige Funktionen erstellen

### Themenschwerpunkt: Funktionale Programmierung umsetzen

---

#### Einführung und Zielsetzung

In meiner Flask-Webanwendung habe ich die Anwendung höherwertiger Funktionen (Higher-Order Functions) erforscht, indem ich Funktionen als Argumente an andere Funktionen übergeben habe. Dieser Ansatz erlaubt eine größere Flexibilität und Modularität im Code.

---

### Umsetzung der Kompetenz in Flask

#### Höherwertige Funktionen

- **Konzept**: Höherwertige Funktionen sind Funktionen, die andere Funktionen als Argumente annehmen oder Funktionen als Ergebnis zurückgeben. Diese ermöglichen es, Code dynamisch zu gestalten und wiederzuverwenden.
- **Anwendung im Code**: Ich habe eine höherwertige Funktion erstellt, die eine Funktion als Argument nimmt und diese auf eine Liste von Events anwendet.

#### Beispiel-Implementierung

```python
# Höherwertige Funktion, die eine andere Funktion als Argument nimmt
def apply_to_all_events(func):
    events = Event.query.all()
    return [func(event) for event in events]

# Verwendung der höherwertigen Funktion
@event_bp.route('/apply_to_all', methods=['GET'])
def apply_function_to_all_events():
    formatted_events = apply_to_all_events(format_event)
    return jsonify(formatted_events)
```

Beschreibung: In diesem Beispiel nimmt apply_to_all_events eine Funktion func als Argument und wendet sie auf jeden Event in der Datenbank an. Diese Art von Funktion erlaubt es, verschiedene Operationen auf eine konsistente Datenmenge anzuwenden, was den Code flexibler und wiederverwendbarer mach

---

### Lernprozess und Reflexion

Die Arbeit mit höherwertigen Funktionen hat mir gezeigt, wie mächtig Funktionen in Python sein können. Diese Art von Funktionen ermöglicht es, generische Lösungen für verschiedene Probleme zu schreiben, die dann mit spezifischen Funktionen erweitert werden können.

---

### Zukünftige Schritte

Die Erfahrungen, die ich mit der Anwendung von höherwertigen Funktionen gemacht habe, motivieren mich, diesen Ansatz in zukünftigen Projekten weiter zu erforschen. Insbesondere interessiert mich die Anwendung in komplexeren Szenarien, wo Funktionen als Argumente die Flexibilität und Erweiterbarkeit der Software erhöhen können.

Die Anwendung von B2F in meiner Flask-App hat mein Verständnis für funktionale Programmierung vertieft und wird meine zukünftige Arbeit als Softwareentwickler bereichern.