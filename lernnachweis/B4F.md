# Lernnachweis zur Kompetenz B4F

## Kompetenz: B4F: Ich kann Map, Filter und Reduce kombiniert verwenden, um Daten zu verarbeiten und zu manipulieren, die komplexere Transformationen erfordern.

### Themenschwerpunkt: Funktionale Programmierung umsetzen	

---

#### Einführung und Zielsetzung

In meiner Flask-Webapplikation habe ich die kombinierte Anwendung von Map, Filter und Reduce erforscht, um komplexe Datenverarbeitungsaufgaben zu lösen. Mein Ziel war es, die Effizienz und Lesbarkeit des Codes zu steigern, indem ich diese funktionalen Programmiermethoden nutze.

---

### Fortgeschrittene Nutzung funktionaler Programmierung in Flask

Die Kombination von Map, Filter und Reduce ermöglicht es, komplexe Datenverarbeitungslogiken aufzubauen, die sowohl leistungsstark als auch elegant sind. Diese Methoden wurden verwendet, um Daten aus der Datenbank abzurufen und in einer sinnvollen Weise zu transformieren.

#### Beispiel für die Implementierung

- **Durchschnittliche Anzahl von Teilnehmern für zukünftige Events berechnen**
   - **Route**: `/average_future_participants`
   - **Methode**: GET
   - **Algorithmus**: 
     - Verwendung von `filter()` zum Filtern zukünftiger Events.
     - Einsatz von `reduce()` zur Berechnung der Gesamtanzahl der Teilnehmer.
     - Berechnung des Durchschnitts basierend auf der Anzahl der zukünftigen Events.
   - **Code-Ausschnitt**:
     ```python
     @event_bp.route('/average_future_participants', methods=['GET'])
     def get_average_future_participants():
         events = Event.query.all()
         future_events = list(filter(lambda e: e.date > datetime.now(), events))
         total_participants = reduce(lambda acc, e: acc + len(e.participants), future_events, 0)
         average_participants = total_participants / len(future_events) if future_events else 0
         return jsonify({'average_participants': average_participants})
     ```

---

### Lernprozess und Reflexion

Durch das Kombinieren von Map, Filter und Reduce konnte ich die Macht der funktionalen Programmierung in realen Anwendungsfällen erkennen. Diese Techniken erlaubten es mir, komplexe Datentransformationen effizient und mit weniger Code zu bewältigen. Die Herausforderung bestand darin, die richtige Balance zwischen Funktionalität und Lesbarkeit zu finden.

---

### Zukünftige Schritte

Ich plane, diese fortgeschrittenen Konzepte in zukünftigen Projekten weiter zu erforschen, um noch komplexere Datenverarbeitungsanforderungen zu erfüllen. Zudem möchte ich meine Kenntnisse in der Anwendung dieser Techniken auf Datenströme und asynchrone Verarbeitung erweitern.

Durch die Anwendung dieser fortgeschrittenen funktionalen Programmierungstechniken fühle ich mich gut gerüstet, um effiziente und leistungsstarke Webanwendungen zu entwickeln und weiter zu optimieren.
