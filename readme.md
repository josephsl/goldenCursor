# golden cursor#

* Author: salah atair, Joseph Lee
* Download [stable version][1]
* Download [development version][2]

This add-on allows you to move the mouse using a keyboard and save mouse positions for applications.

## Key commands

* Control+NVDA+L: view saved positions for an application if any.
* Shift+NVDA+l: save a tag for the current mouse position in the currently focused application.
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

## Version 2.0

* Requires NVDA 2017.3 or later.
* Position file format is incompatible with 1.x versions. If 1.x position format is found, old positions will be migrated to the new format during installation.
* The name of the currently focused app is shown as part of the title for positions list dialog.
* When saving positions, resolved an issue where NvDA may play error tones if the positions folder does not exist.
* You can now enter mouse arrows mode where you can move the mouse by pressing just arrow keys.

## Version 1.4

* Removed win32api dependency to make it compatible with past and future versions of NVDA.

## Version 1.0

* Initial release.

[1]: https://addons.nvda-project.org/files/get.php?file=gc

[2]: https://addons.nvda-project.org/files/get.php?file=gc-dev
