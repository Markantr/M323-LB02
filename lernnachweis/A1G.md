# Lernnachweis zur Kompetenz A1G

## Kompetenz: A1G: Ich kann die Eigenschaften von Funktionen beschreiben (z.Bsp. pure function) und den Unterschied zu anderen Programmier-Strukturen erläutern (z.Bsp. zu Prozedur).

### Themenschwerpunkt: Unterschiede zwischen funktionaler Programmierung und anderen Programmierparadigmen aufzeigen.

---

#### Einführung und Zielsetzung

Während der Entwicklung meiner Flask-Webanwendung konzentrierte ich mich auf die Nutzung und Implementierung reiner Funktionen. Mein Ziel war es, die Prinzipien der funktionalen Programmierung zu veranschaulichen, indem ich Funktionen erstelle, die keine Seiteneffekte haben und deren Ausgaben ausschließlich von ihren Eingaben abhängen.

---

### Umsetzung reiner Funktionen in Flask

Reine Funktionen sind ein zentraler Bestandteil der funktionalen Programmierung. Sie erhöhen die Vorhersagbarkeit und Testbarkeit des Codes, indem sie Seiteneffekte vermeiden und für gleiche Eingaben stets gleiche Ausgaben liefern.

#### Beispiel für die Implementierung

- **Implementierung einer reinen Funktion zur Formatierung von Event-Daten**
   - **Funktion**: `format_event`
   - **Zweck**: Nimmt ein Event-Objekt entgegen und gibt einen formatierten String zurück.
   - **Eigenschaften**: Die Funktion ist rein, da sie keine externen Zustände verändert und bei gleichen Eingaben stets das gleiche Ergebnis liefert.
   - **Code-Ausschnitt**:
     ```python
     def format_event(event):
         return f"{event.name} takes place on {event.date} in {event.location}."

     @event_bp.route('/formatted_events', methods=['GET'])
     def get_formatted_events():
         events = Event.query.all()
         formatted_events = [format_event(e) for e in events]
         return jsonify(formatted_events)
     ```

---

### Lernprozess und Reflexion

Durch die Implementierung reiner Funktionen in meiner Flask-Anwendung habe ich ein besseres Verständnis für die Konzepte der funktionalen Programmierung gewonnen. Ich lernte, wie wertvoll es ist, Funktionen zu erstellen, deren Verhalten leicht vorhersehbar und testbar ist. Dies hat nicht nur die Qualität meines Codes verbessert, sondern auch die Wartung und Erweiterung der Anwendung vereinfacht.

---

### Zukünftige Schritte

Ich beabsichtige, die Prinzipien der funktionalen Programmierung weiter zu vertiefen, insbesondere in Bezug auf größere Anwendungen und die Integration mit anderen Programmierparadigmen. Die Fähigkeit, reine Funktionen zu schreiben und zu verstehen, ist ein wertvolles Werkzeug in meinem Entwicklerarsenal.

Diese Erfahrung hat mir die Bedeutung und den Nutzen funktionaler Programmierprinzipien in der Praxis gezeigt, und ich bin gespannt darauf, diese Kenntnisse in meinen zukünftigen Projekten anzuwenden und weiterzuentwickeln.
