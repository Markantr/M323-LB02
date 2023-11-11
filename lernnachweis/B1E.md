# Lernnachweis zur Kompetenz B1E

## Kompetenz: B1E - Ich kann Funktionen in zusammenhängende Algorithmen implementieren

### Themenschwerpunkt: Funktionale Programmierung umsetzen.

---

#### Einführung und Zielsetzung

Im Rahmen meiner Arbeit an einer Flask-Webapplikation habe ich mich intensiv mit der Implementierung von Funktionen in zusammenhängende Algorithmen beschäftigt. Das Hauptziel war es, eine strukturierte und effiziente Webanwendung zu entwickeln, die verschiedene Endpunkte und zugehörige Logik umfasst.

---

### Funktionale Umsetzung in Flask

In Flask werden Routen durch Dekoratoren definiert, die Funktionen als Handler für spezifische HTTP-Anfragen zuweisen. Diese Funktionen bilden zusammenhängende Algorithmen, die bestimmte Aufgaben erfüllen, wie das Abrufen, Erstellen, Aktualisieren und Löschen von Daten.

#### Beispiele für Algorithmen-Implementierung

1. **POST-Anfrage für das Hinzufügen von Events:**
   - Route: `/event`
   - Methode: POST
   - Algorithmus: Empfang von JSON-Daten, Umwandlung in ein Event-Objekt und Speicherung in der Datenbank.
   - Code-Ausschnitt:
     ```python
     @event_bp.route('/event', methods=['POST'])
     def add_event():
         data = request.get_json()
         new_event = Event(...)
         db.session.add(new_event)
         db.session.commit()
     ```

2. **GET-Anfrage für das Abrufen aller Events:**
   - Route: `/events`
   - Methode: GET
   - Algorithmus: Abrufen aller Event-Daten aus der Datenbank und Rückgabe als JSON.
   - Code-Ausschnitt:
     ```python
     @event_bp.route('/events', methods=['GET'])
     def get_events():
         events = Event.query.all()
         ...
         return jsonify(events)
     ```

---

### Lernprozess und Reflexion

Zu Beginn des Projekts war ich mit der Strukturierung einer Flask-App und dem Zusammenspiel verschiedener Komponenten noch nicht vertraut. Durch die Arbeit an der App lernte ich, wie wichtig es ist, den Code in logische Module aufzuteilen und klare Schnittstellen zwischen verschiedenen Funktionen zu schaffen. Insbesondere die Nutzung von Blueprints half mir, die App in übersichtliche Segmente zu gliedern.

---

### Zukünftige Schritte

Ich plane, mein Wissen in der Entwicklung von Webanwendungen weiter zu vertiefen, insbesondere in Bezug auf fortgeschrittene Datenverarbeitung und die Integration von Drittanbieter-Diensten. Außerdem möchte ich mich mit modernen Frontend-Technologien vertraut machen, um Full-Stack-Entwicklungsprojekte umsetzen zu können.

Mit den erworbenen Kenntnissen und Fähigkeiten fühle ich mich nun sicher in der Entwicklung und Strukturierung von Backend-Logik für Webanwendungen und freue mich darauf, diese Fähigkeiten in zukünftigen Projekten weiter auszubauen.
