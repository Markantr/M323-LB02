# Lernnachweis zur Kompetenz B4G

## Kompetenz: B4G: Ich kann die Funktionen Map, Filter und Reduce einzeln auf Listen anwenden.

### Themenschwerpunkt: Funktionale Programmierung umsetzen	

---

#### Einführung und Zielsetzung

In meiner Flask-Webanwendung habe ich mich mit der Anwendung von funktionalen Programmiermethoden wie Map, Filter und Reduce beschäftigt. Mein Ziel war es, diese Methoden einzeln zu nutzen, um Listen von Daten effizient zu verarbeiten und zu transformieren.

---

### Anwendung funktionaler Programmierung in Flask

Die funktionalen Methoden Map, Filter und Reduce bieten mächtige Möglichkeiten, um Datenlisten zu verarbeiten. Diese Methoden werden in Python als eingebaute Funktionen bereitgestellt und eignen sich hervorragend zur Verarbeitung von Daten, die aus einer Flask-Route abgerufen werden.

#### Beispiele für die Implementierung

1. **Map**
   - **Ziel**: Extrahieren der Namen aller Events.
   - **Route**: `/event_names`
   - **Methode**: GET
   - **Algorithmus**: Nutzung von `map()` zur Transformation einer Liste von Event-Objekten in eine Liste ihrer Namen.
   - **Code-Ausschnitt**:
     ```python
     @event_bp.route('/event_names', methods=['GET'])
     def get_event_names():
         events = Event.query.all()
         event_names = list(map(lambda e: e.name, events))
         return jsonify(event_names)
     ```

2. **Filter**
   - **Ziel**: Finden aller zukünftigen Events.
   - **Route**: `/future_events`
   - **Methode**: GET
   - **Algorithmus**: Einsatz von `filter()` zur Filterung der Events nach Datum.
   - **Code-Ausschnitt**:
     ```python
     @event_bp.route('/future_events', methods=['GET'])
     def get_future_events():
         events = Event.query.all()
         future_events = list(filter(lambda e: e.date > datetime.now(), events))
         return jsonify([e.to_dict() for e in future_events])
     ```

3. **Reduce**
   - **Ziel**: Berechnung der Gesamtanzahl der Teilnehmer an allen Events.
   - **Route**: `/total_participants`
   - **Methode**: GET
   - **Algorithmus**: Verwendung von `reduce()` zur Berechnung der kumulativen Anzahl der Teilnehmer.
   - **Code-Ausschnitt**:
     ```python
     @event_bp.route('/total_participants', methods=['GET'])
     def get_total_participants():
         events = Event.query.all()
         total_participants = reduce(lambda acc, e: acc + len(e.participants), events, 0)
         return jsonify({'total_participants': total_participants})
     ```

---

### Lernprozess und Reflexion

Die Arbeit mit funktionalen Programmierkonzepten wie Map, Filter und Reduce hat mir ein tieferes Verständnis für effiziente Datenverarbeitung in Python gebracht. Ich lernte, wie diese Methoden in Echtzeitanwendungen eingesetzt werden können, um komplexe Datenmanipulationen auf saubere und effiziente Weise durchzuführen.

---

### Zukünftige Schritte

Mein Ziel ist es, diese Konzepte in zukünftigen Projekten weiter zu vertiefen, insbesondere in Kombination mit anderen fortgeschrittenen Techniken der Datenverarbeitung und -analyse. Ich plane auch, mein Wissen in anderen Bereichen der Webentwicklung zu erweitern, um vollständige und robuste Webanwendungen zu erstellen.

Mit den erworbenen Fähigkeiten in funktionaler Programmierung fühle ich mich nun besser gerüstet, um komplexe Datenverarbeitungsprobleme in meinen zukünftigen Projekten effektiv zu lösen.
