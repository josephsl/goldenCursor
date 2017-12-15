# golden cursor#

* Author: salah atair
* Download [stable version][1]
* Download [development version][2]

This add-on allows you to move the mouse using a keyboard and save mouse positions for applications.

## Key commands

* nvda+shift+L: view a list of the saved positions.
* nvda+control+l: save a position.
* nvda+win+c: select the level of movement.
* nvda+win+r: toggle mouse restriction.
* nvda+win+s: toggle the reporting of pixels.
* nvda+win + j: open a dialog to type the X, Y position you want to jump to.
* nvda+win+ p: reporting the pixels for the current position pointer.
* nvda+win+arrowKeys: move the mouse in different directions.
* Note: these gestures can be reassigned from the input gestures dialog in the nvda preferences menu.

## Notes

* When sharing positions, each party should use same display resolution.
* For maximum compatibility, you should maximize windows by pressing Windows+Up arrow.
* When sharing positions, existing position labels should be renamed.

## Version 2.0

* Requires NVDA 2017.3 or later.
* The name of the currently focused app is shown as part of the title for positions list dialog.
* When saving positions, resolved an issue where NvDA may play error tones if the positions folder does not exist.

## Version 1.4

* Removed win32api dependency to make it compatible with past and future versions of NVDA.

## Version 1.0

* Initial release.

[1]: https://addons.nvda-project.org/files/get.php?file=gc

[2]: https://addons.nvda-project.org/files/get.php?file=gc-dev
