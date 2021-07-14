# golden cursor#

* Author: salah atair, Joseph Lee
* Download [stable version][1]
* NVDA compatibility: 2019.3 and beyond

This add-on allows you to move the mouse using a keyboard and save mouse positions for applications.

## Key commands

* Control+NVDA+L: view saved mouse positions for an application if any.
* Shift+NVDA+l: save a tag or a label for the current mouse position in the currently focused application.
* Windows+NVDA+C: change mouse movement unit.
* Windows+NVDA+R: toggle mouse restriction.
* Windows+NVDA+S: toggle reporting of mouse position in pixels.
* Windows+NVDA+J: move mouse to a specific x and y position.
* Windows+NVDA+P: report mouse position.
* Windows+NVDA+M: sswitch mouse arrows on or off.
* Windows+NVDA+arrow keys (or just arrow keys if mouse arrows is on): move mouse.

Note: these gestures can be reassigned via NVDA's Input Gestures dialog under Golden Cursor category.

## Notes

* When sharing positions (tags), each party should use same display resolution.
* For maximum compatibility, you should maximize windows by pressing Windows+Up arrow.
* When sharing positions, existing position labels should be renamed.
* Version 1.x and 2.x mouse position formats are incompatible.
* To perform functions that require use of arrow keys, turn off mouse arrows first.
* When deleting saved positions, if there are no saved positions left, positions for the application will be cleared.

## Version 5.0

* Modernized add-on source code to make it compatible with NVDA 2021.1.
* Resolved many coding style issues and potential bugs with Flake8.

## Version 4.0

* Requires NVDA 2019.3 or later.
* Golden Cursor settings dialog has been replaced by Golden Cursor settings panel.

## Version 3.3

* Internal changes to support future NVDA releases.

## Version 3.2

* Add-on is compatible with NVDA 2018.3 (wxPython 4).

## Version 3.0

* If using NVDA 2018.2, add-on settings will be found in new multi-category settings screen under "Golden Cursor" category.

## Version 2.1

* Fixed unicode decode error when trying to delete tag name.
* Prevent Multiple Instances When Opening various add-on Dialogs.
* Improved appearance of mouse positions list and jump to position dialogs.

## Version 2.0

* Requires NVDA 2017.3 and later.
* Position file format is incompatible with 1.x versions. If 1.x position format is found, old positions will be migrated to the new format during installation.
* Added a new Golden Cursor settings dialog in NVDA's Preferences menu to configure mouse movement unit and announcement of mouse positions as mouse moves.
* Various messages from this add-on has changed.
* When toggling various settings, toggle tone will no longer be heard.
* You can now enter mouse arrows mode where you can move the mouse by pressing just arrow keys.
* Changes to positions list dialog, including new name (now called Mouse Positions) and layout, displaying mouse coordinates for a label, and showing the name of the active app as part of the title.
* From Mouse Positions dialog, pressing Enter on a saved label will move the mouse to the saved location.
* When renaming a mouse position, an error dialog will be shown if a label with the same name as the new name exists.
* When deleting or clearing mouse positions, you must now answer Yes before positions are deleted and/or cleared.
* Changes to mouse jump feature, including a new name (now called New mouse position) and ability to enter X and Y coordinates separately or by using up or down arrow keys.
* The dialog shown when saving the current mouse position now shows coordinates for current mouse location.
* When saving positions, resolved an issue where NvDA may play error tones if the positions folder does not exist.

## Version 1.4

* Removed win32api dependency to make it compatible with past and future versions of NVDA.

## Version 1.0

* Initial release.

[1]: https://addons.nvda-project.org/files/get.php?file=gc

[2]: https://addons.nvda-project.org/files/get.php?file=gc-dev
