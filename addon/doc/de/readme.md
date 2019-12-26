# Goldener Cursor #

* Autor: Salah Atair, Joseph Lee
* [Stabile Version herunterladen][1]
* NVDA compatibility: 2019.3 and beyond
* Download [older version][3] compatible with NVDA 2019.2.1 and earlier

Diese Erweiterung ermöglicht das Ziehen der Maus mit der Tastatur und das
Speichern der gewünschten Mauspositionen für die jeweilige Anwendung.

## Tastenkombinationen

* Strg+NVDA+L: Zeige gespeicherte Maus-Positionen für eine Anwendung, falls
  vorhanden.
* Umschalt+NVDA+l: Speichern eines Tags oder einer Bezeichnung für die
  aktuelle Mausposition in der aktuell fokussierten Anwendung.
* Windows+NVDA+C: ändert die Maus-Bewegungseinheit.
* NVDA+Windows+R: Beschränkung der Maus ein- oder ausschalten.
* Windows+NVDA+S: Neue Maus-Koordinaten in Pixel ansagen, wenn sich die Maus
  bewegt
* Windows+NVDA+J: bewegt die Maus zu einer bestimmten X- und Y-Position.
* NVDA+Windows+P: Maus-Position ausgeben
* Windows+NVDA+M: Mauszeiger ein- oder ausschalten.
* Windows+NVDA+Pfeiltasten (oder nur Pfeiltasten, wenn die Bewegung des
  Mauszeigers durch pfeiltasten eingeschaltet ist): Maus bewegen.

Anmerkung: Diese Tastenkombinationen können im NVDA-Menü unter Einstellungen
im Dialog Eingaben in der Kategorie "goldener Cursor" angepasst werden.

## Hinweise

* Wenn die Positionen geteilt werden, sollte jeder Teilnehmer die gleiche
  Bildschirmauflösung eingestellt haben.
* Für beste Kompatibilität sollten Sie mit der Tastenkombination
  Windows+Pfeiltaste nach oben das Fenster maximieren.
* Wenn Sie die Positionen teilen, sollten Sie die bereits vorhandenen
  Positionsbeschreibungen umbenennen.
* Die Versionen 1.x und 2.x der Mauspositions-Formate sind zueinander nicht
  kompatibel.
* Um Funktionen auszuführen, die die Verwendung von Pfeiltasten erfordern,
  schalten Sie zuerst die Bewegung des Mauszeigers durch Pfeiltasten aus.
* Wenn beim Löschen gespeicherter Positionen keine gespeicherten Positionen
  mehr vorhanden sind, werden die Positionen für die Anwendung gelöscht.

## Version 4.0

* Requires NVDA 2019.3 or later.
* Golden Cursor settings dialog has been replaced by Golden Cursor settings
  panel.

## Version 3.3

* Internal changes to support future NVDA releases.

## Version 3.2

* Die Erweiterung ist kompatibel mit NVDA 2018.3 (wxPython 4).

## Version 3.0

* Bei Verwendung von NVDA 2018.2 werden die Einstellungen für die
  Erweiterung in der neuen Multikategorie-Einstellungsseite unter der
  Kategorie "Goldener Cursor" angezeigt.

## Version 2.1

* Es wurde ein Unicode-Dekodierungsfehler beim Löschen des Tag-Namens
  behoben.
* Das öffnen mehrerer Instanzen verschiedener Erweiterungsdialoge ist nun
  nicht mehr möglich.
* Die Darstellung der Liste der Mauspositionen und des Dialogs für das
  Springen zu  bestimmten Positionen wurde verbessert.

## Version 2.0

* Benötigt NVDA 2017.3 oder neuer.
* Das neue Dateiformat ist inkompatibel zu 1.x-Versionen. Wenn Dateien der
  alten Version gefunden werden, werden diese während der Installation in
  das neue Format umgewandelt.
* Es wurde ein neuer Goldener-Cursor-Einstellungsdialog im
  NVDA-Menü/Einstellungen hinzugefügt, um die Mausbewegungseinheit und die
  Anzeige der Mauspositionen bei Mausbewegungen zu konfigurieren.
* Mehrere Meldungen dieser Erweiterung haben sich geändert.
* Beim Umschalten verschiedener Einstellungen ertönt kein Umschaltton mehr.
* Sie können nun den Mauszeiger einfach mit den Pfeiltasten in Regionen
  bewegen, in welchen die Maus durch Drücken der Pfeiltasten standardmäßig
  bewegt werden kann.
* Änderungen im Positionslistendialog, einschließlich des neuen Namens
  (jetzt Mauspositionen genannt) und des Layouts. Die Anzeige der
  Mauskoordinaten für eine Bezeichnung und die Anzeige des Namens der
  aktiven Anwendung sind nun Teil des Titels.
* Wenn Sie im Dialogfeld "Mauspositionen" die Eingabetaste auf einer
  gespeicherten Bezeichnung drücken, wird die Maus an die gespeicherte
  Position bewegt.
* Beim Umbenennen einer Mausposition wird ein Fehlerdialog angezeigt, wenn
  eine Bezeichnung mit dem gleichen Namen wie der neue Name bereits
  existiert.
* Beim Löschen von Mauspositionen müssen Sie jetzt mit Ja antworten, bevor
  Positionen gelöscht werden.
* Änderungen an der Maussprungfunktion, einschließlich eines neuen Namens
  (jetzt Neue Mausposition genannt). X- und Y-Koordinaten können jetzt
  getrennt oder mit den Pfeiltasten nach oben und unten eingegeben werden.
* Der Dialog, der beim Speichern der aktuellen Mausposition angezeigt wird,
  zeigt nun die Koordinaten der aktuellen Mausposition an.
* Beim Speichern von Mauspositionen wurde ein Problem behoben, bei dem NVDA
  Fehlertöne abspielte, wenn der Positionsordner nicht existiert.

## Version 1.4

* Die Abhängigkeit von der win32api  wurde aufgehoben, sodass die
  Erweiterung mit älteren und zukünftigen Versionen von NVDA funktioniert.

## Version 1.0

* Erste Veröffentlichung.

[[!tag stable dev]]

[1]: https://addons.nvda-project.org/files/get.php?file=gc

[2]: https://addons.nvda-project.org/files/get.php?file=gc-dev

[3]: https://addons.nvda-project.org/files/get.php?file=gc-2019
