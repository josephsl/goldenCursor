# Goldener Cursor #

* Autor: Salah Atair, Joseph Lee
* Herunterladen der [stabilen Version][1]
* Herunterladen der [Entwicklerversion][2]

Diese Erweiterung ermöglicht das Ziehen der Maus mit der Tastatur und das
Speichern der gewünschten Mauspositionen für die jeweilige Anwendung.

## Tastenkombinationen

* Control+NVDA+L: view saved mouse positions for an application if any.
* Shift+NVDA+l: save a tag or a label for the current mouse position in the
  currently focused application.
* Windows+NVDA+C: ändert die Maus-Bewegungseinheit.
* Windows+NVDA+R: toggle mouse restriction.
* Windows+NVDA+S: toggle reporting of mouse position in pixels.
* Windows+NVDA+J: bewegt die Maus zu einer bestimmten X- und Y-Position.
* NVDA+Windows+P: Maus-Position ausgeben
* Windows+NVDA+M: sswitch mouse arrows on or off.
* Windows+NVDA+arrow keys (or just arrow keys if mouse arrows is on): move
  mouse.

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
* To perform functions that require use of arrow keys, turn off mouse arrows
  first.
* When deleting saved positions, if there are no saved positions left,
  positions for the application will be cleared.

## Version 2.1

* Fixed unicode decode error when trying to delete tag name.
* Das öffnen mehrerer Instanzen verschiedener Erweiterungsdialoge ist nun
  nicht mehr möglich.
* Improved appearance of mouse positions list and jump to position dialogs.

## Version 2.0

* Benötigt NVDA 2017.3 oder neuer.
* Position file format is incompatible with 1.x versions. If 1.x position
  format is found, old positions will be migrated to the new format during
  installation.
* Added a new Golden Cursor settings dialog in NVDA's Preferences menu to
  configure mouse movement unit and announcement of mouse positions as mouse
  moves.
* Mehrere Meldungen dieser Erweiterung haben sich geändert.
* When toggling various settings, toggle tone will no longer be heard.
* You can now enter mouse arrows mode where you can move the mouse by
  pressing just arrow keys.
* Changes to positions list dialog, including new name (now called Mouse
  Positions) and layout, displaying mouse coordinates for a label, and
  showing the name of the active app as part of the title.
* From Mouse Positions dialog, pressing Enter on a saved label will move the
  mouse to the saved location.
* When renaming a mouse position, an error dialog will be shown if a label
  with the same name as the new name exists.
* When deleting or clearing mouse positions, you must now answer Yes before
  positions are deleted and/or cleared.
* Changes to mouse jump feature, including a new name (now called New mouse
  position) and ability to enter X and Y coordinates separately or by using
  up or down arrow keys.
* The dialog shown when saving the current mouse position now shows
  coordinates for current mouse location.
* When saving positions, resolved an issue where NvDA may play error tones
  if the positions folder does not exist.

## Version 1.4

* Die Abhängigkeit von der win32api  wurde aufgehoben, sodass die
  Erweiterung mit älteren und zukünftigen Versionen von NVDA funktioniert.

## Version 1.0

* Erste Veröffentlichung.

[[!tag stable dev]]

[1]: https://addons.nvda-project.org/files/get.php?file=gc

[2]: https://addons.nvda-project.org/files/get.php?file=gc-dev
