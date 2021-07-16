# -*- coding: utf-8 -*-
# golden cursor
# Copyright (C) 2015-2021
# Version 2.2
# License GNU GPL
# Date: 25/12/2015
# team work: author : salah atair, translation and keycommands are made by wafeeq taher
# Additional tweaking done by Joseph Lee and contributors, resetting version to 1.0.

# Control mouse from the keyboard,
# including specifying hotspots, different movement units, mouse restrictions and others.

import os
from configobj import ConfigObj
import globalPluginHandler
import gui
import wx
import config
import globalVars
import scriptHandler
import mouseHandler
import ui
import api
import winUser
import addonHandler
addonHandler.initTranslation()

# Each global constant is prefixed with "GC".

# Constants
GCMousePositions = os.path.join(globalVars.appArgs.configPath, "addons", "goldenCursor", "mousePositions")
# Mouse movement directions
GCMouseRight = 0
GCMouseLeft = 1
GCMouseDown = 2
GCMouseUp = 3


# Reports mouse position, used in various places.
def reportMousePosition(x=None, y=None):
	# The coordinates are keywords so specific position can be announced if needed.
	cursorPos = winUser.getCursorPos()
	if x is None:
		x = cursorPos[0]
	if y is None:
		y = cursorPos[1]
	ui.message("{0}, {1}".format(x, y))


def setMousePosition(x, y, announceMousePosition=False):
	# Setter version of report mouse position function.
	# The new position announcement is to be used if needed.
	winUser.setCursorPos(x, y)
	mouseHandler.executeMouseMoveEvent(x, y)
	if announceMousePosition:
		# Announce this half a second later to give the appearance of mouse movement.
		wx.CallLater(500, reportMousePosition, x=x, y=y)


class EnterPositionName(wx.TextEntryDialog):
	"""
	This subclass of the wx.TextEntryDialog class was created to
	prevent multiple instances of the dialog box that propose to give a name to the current mouse position.
	This dialog can be opened via the script_saveMousePosition accessible with the nvda+shift+l shortcut.
	"""
	# The following comes from exit dialog class from GUI package (credit: NV Access and Zahari from Bulgaria).
	_instance = None

	def __new__(cls, parent, *args, **kwargs):
		inst = cls._instance() if cls._instance else None
		if not inst:
			return super(cls, cls).__new__(cls, parent, *args, **kwargs)
		return inst

	def __init__(self, *args, **kwargs):
		inst = EnterPositionName._instance() if EnterPositionName._instance else None
		if inst:
			return
		# Use a weakref so the instance can die.
		import weakref
		EnterPositionName._instance = weakref.ref(self)

		super(EnterPositionName, self).__init__(*args, **kwargs)


class PositionsList(wx.Dialog):
	"""
	This common dialogue has been created to facilitate access to the following choices:
	1. The list of x / y positions proposed by the script_goToPosition,
	accessible via the nvda+windows+j shortcut.
	2. The list of mouse positions saved for the current application proposed by the script_mousePositionsList,
	accessible via the nvda+control+l shortcut.
	It also prevents multiple instances for these 2 dialogs.
	"""
	# The following comes from exit dialog class from GUI package (credit: NV Access and Zahari from Bulgaria).
	_instance = None

	def __new__(cls, parent, *args, **kwargs):
		inst = cls._instance() if cls._instance else None
		if not inst:
			return super(cls, cls).__new__(cls, parent, *args, **kwargs)
		return inst

	def __init__(self, parent, appName=None, goto=False):
		inst = PositionsList._instance() if PositionsList._instance else None
		if inst:
			return
		# Use a weakref so the instance can die.
		import weakref
		PositionsList._instance = weakref.ref(self)

		if appName:
			super(PositionsList, self).__init__(parent, title=_("Mouse positions for %s") % (appName), size=(420, 300))
			self.mousePositionsList(appName=appName)
		elif goto:
			super(PositionsList, self).__init__(parent, title=_("New mouse position"))
			self.jumpToPosition()

	def mousePositionsList(self, appName):
		self.appName = appName
		self.positions = ConfigObj(os.path.join(GCMousePositions, f"{appName}.gc"), encoding="UTF-8")
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		sHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		# Translators: The label for the list view of the mouse positions in the current application.
		mousePositionsText = _("&Saved mouse positions")
		self.mousePositionsList = sHelper.addLabeledControl(
			mousePositionsText, wx.ListCtrl, style=wx.LC_REPORT | wx.LC_SINGLE_SEL, size=(550, 350)
		)
		# Translators: the column in mouse positions list to identify the position name.
		self.mousePositionsList.InsertColumn(0, _("Name"), width=150)
		# Translators: the column in mouse positions list to identify the X coordinate.
		self.mousePositionsList.InsertColumn(1, _("Position X"), width=50)
		# Translators: the column in mouse positions list to identify the Y coordinate.
		self.mousePositionsList.InsertColumn(2, _("Position Y"), width=50)
		self.mousePositionsList.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.onJump)

		for entry in sorted(self.positions.keys()):
			x, y = self.positions[entry].split(",")
			self.mousePositionsList.Append((entry, x, y))
		self.mousePositionsList.Select(0, on=1)
		self.mousePositionsList.SetItemState(0, wx.LIST_STATE_FOCUSED, wx.LIST_STATE_FOCUSED)

		bHelper = gui.guiHelper.ButtonHelper(orientation=wx.HORIZONTAL)

		jumpButtonID = wx.NewIdRef()
		# Translators: the button to jump to the selected position.
		bHelper.addButton(self, jumpButtonID, _("&Jump"), wx.DefaultPosition)

		renameButtonID = wx.NewIdRef()
		# Translators: the button to rename a mouse position.
		bHelper.addButton(self, renameButtonID, _("&Rename"), wx.DefaultPosition)

		deleteButtonID = wx.NewIdRef()
		# Translators: the button to delete the selected mouse position.
		bHelper.addButton(self, deleteButtonID, _("&Delete"), wx.DefaultPosition)

		clearButtonID = wx.NewIdRef()
		# Translators: the button to clear all mouse positions for the focused app.
		bHelper.addButton(self, clearButtonID, _("C&lear positions"), wx.DefaultPosition)

		# Translators: The label of a button to close the mouse positions dialog.
		bHelper.addButton(self, wx.ID_CLOSE, _("&Close"), wx.DefaultPosition)

		sHelper.addItem(bHelper)

		self.Bind(wx.EVT_BUTTON, self.onJump, id=jumpButtonID)
		self.Bind(wx.EVT_BUTTON, self.onRename, id=renameButtonID)
		self.Bind(wx.EVT_BUTTON, self.onDelete, id=deleteButtonID)
		self.Bind(wx.EVT_BUTTON, self.onClear, id=clearButtonID)
		self.Bind(wx.EVT_BUTTON, lambda evt: self.Close(), id=wx.ID_CLOSE)

		# Borrowed from NVDA Core (add-ons manager).
		# To allow the dialog to be closed with the escape key.
		self.Bind(wx.EVT_CLOSE, self.onClose)
		self.EscapeId = wx.ID_CLOSE

		mainSizer.Add(sHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		self.Sizer = mainSizer
		mainSizer.Fit(self)
		self.mousePositionsList.SetFocus()
		self.CenterOnScreen()

	def jumpToPosition(self):
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		mouseJumpHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		x, y = winUser.getCursorPos()
		w, h = api.getDesktopObject().location[2:]
		self.xPos = mouseJumpHelper.addLabeledControl(
			_("&X position"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=0, max=w - 1, initial=x
		)
		self.yPos = mouseJumpHelper.addLabeledControl(
			_("&Y position"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=0, max=h - 1, initial=y
		)

		mouseJumpHelper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Add(mouseJumpHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.SetSizer(mainSizer)
		self.CenterOnScreen()
		self.xPos.SetFocus()

	def onRename(self, event):
		index = self.mousePositionsList.GetFirstSelected()
		oldName = self.mousePositionsList.GetItemText(index)
		name = wx.GetTextFromUser(
			# Translators: The label of a field to enter a new name for a mouse position/tag.
			_("New name"),
			# Translators: The title of the dialog to rename a mouse position.
			_("Rename"), oldName
		)
		# When escape is pressed, an empty string is returned.
		if name in ("", oldName):
			return
		if name in self.positions:
			gui.messageBox(
				# Translators: An error displayed when renaming a mouse position
				# and a tag with the new name already exists.
				_("Another mouse position has the same name as the entered name. Please choose a different name."),
				_("Error"), wx.OK | wx.ICON_ERROR, self
			)
			return
		self.mousePositionsList.SetItemText(index, name)
		self.mousePositionsList.SetFocus()
		self.positions[name] = self.positions[oldName]
		del self.positions[oldName]

	def deletePosition(self, clearPositions=False):
		message, title = "", ""
		entry = self.mousePositionsList.GetFirstSelected()
		name = self.mousePositionsList.GetItemText(entry)
		if not clearPositions:
			message = _(
				# Translators: The confirmation prompt displayed when the user requests to delete the selected tag.
				"Are you sure you want to delete the position named {name}? This cannot be undone."
			).format(name=name)
			# Translators: The title of the confirmation dialog for deletion of selected position.
			title = _("Delete position")
		else:
			message = _(
				# Translators: The confirmation prompt displayed when the user is about to clear positions.
				"Are you sure you want to clear mouse positions for the current application ({appName})? "
				"This cannot be undone."
			).format(appName=self.appName)
			# Translators: The title of the confirmation dialog for clearing mouse positions.
			title = _("Clear mouse positions")
		if gui.messageBox(
			message, title, wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION, self
		) == wx.NO:
			return
		if not clearPositions:
			del self.positions[name]
			self.mousePositionsList.DeleteItem(entry)
			self.positions.write()
			if self.mousePositionsList.GetItemCount() > 0:
				self.mousePositionsList.Select(0, on=1)
		if clearPositions or self.mousePositionsList.GetItemCount() == 0:
			os.remove(self.positions.filename)
			self.positions.clear()
			gui.messageBox(
				# Translators: A dialog message shown when tags for the application is cleared.
				_("All mouse positions for the application {appName} have been deleted.").format(appName=self.appName),
				# Translators: Title of the tag clear confirmation dialog.
				_("Mouse positions cleared"), wx.OK | wx.ICON_INFORMATION
			)
			self.Close()

	def onDelete(self, event):
		self.deletePosition()

	def onClear(self, event):
		self.deletePosition(clearPositions=True)

	def onJump(self, event):
		self.Destroy()
		self.positions.write()
		try:
			x, y = self.positions[self.mousePositionsList.GetItemText(
				self.mousePositionsList.GetFirstSelected()
			)].split(",")
		except Exception:
			return
		self.positions = None
		wx.CallLater(500, setMousePosition, int(x), int(y))

	def onClose(self, evt):
		self.Destroy()
		if len(self.positions):
			self.positions.write()
		self.positions = None

	def onOk(self, evt):
		x, y = self.xPos.GetValue(), self.yPos.GetValue()
		self.Destroy()
		wx.CallAfter(setMousePosition, x, y, announceMousePosition=True)

	def onCancel(self, evt):
		self.Destroy()


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	scriptCategory = _("Golden Cursor")

	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		self.getAppRestriction = None
		self.restriction = False
		self.mouseArrows = False
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(GoldenCursorSettings)

	def terminate(self):
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(GoldenCursorSettings)

	@scriptHandler.script(
		# Translators: input help message for a Golden Cursor command.
		description=_("Opens a dialog listing mouse positions for the current application"),
		gesture="kb:nvda+control+l"
	)
	def script_mousePositionsList(self, gesture):
		# Don't even think about opening this dialog if positions list does not exist.
		appName = api.getForegroundObject().appModule.appName
		if not os.path.exists(os.path.join(GCMousePositions, f"{appName}.gc")):
			# Translators: message presented when no mouse positions are available for the focused app.
			ui.message(_("No mouse positions for %s.") % appName)
		else:
			try:
				d = PositionsList(parent=gui.mainFrame, appName=appName)
				gui.mainFrame.prePopup()
				d.Raise()
				d.Show()
				gui.mainFrame.postPopup()
			except RuntimeError:
				pass

	@scriptHandler.script(
		# Translators: Input help message for a Golden Cursor command.
		description=_("Opens a dialog to label the current mouse position and saves it"),
		gesture="kb:nvda+shift+l"
	)
	def script_saveMousePosition(self, gesture):
		x, y = winUser.getCursorPos()
		# Stringify coordinates early.
		x, y = str(x), str(y)
		d = EnterPositionName(
			# Translators: edit field label for new mouse position.
			gui.mainFrame, _("Enter the name for the current mouse position (x: {positionX}, Y: {positionY}").format(
				positionX=x, positionY=y
			),
			# Translators: title for save mouse position dialog.
			_("Save mouse position")
		)

		def callback(result):
			if result == wx.ID_OK:
				name = d.GetValue().rstrip()
				if name == "":
					return
				appName = self.getMouse().appModule.appName
				# If the files path does not exist, create it now.
				if not os.path.exists(GCMousePositions):
					os.mkdir(GCMousePositions)
				position = ConfigObj(os.path.join(GCMousePositions, f"{appName}.gc"), encoding="UTF-8")
				position[name] = ",".join([x, y])
				position.write()
				# Translators: presented when position (tag) has been saved.
				ui.message(_("Position saved in %s.") % position.filename)
		gui.runScriptModalDialog(d, callback)

	@scriptHandler.script(
		# Translators: input help message for a Golden Cursor command.
		description=_("Changes mouse movement unit"),
		gesture="kb:nvda+windows+c"
	)
	def script_mouseMovementChange(self, gesture):
		pixelUnits = (1, 5, 10, 20, 50, 100)
		movementUnit = config.conf["goldenCursor"]["mouseMovementUnit"]
		pixelUnitChoices = len(pixelUnits)
		try:
			index = pixelUnits.index(movementUnit)
			movementUnit = pixelUnits[(index + 1) % pixelUnitChoices]
		except ValueError:
			for unit in pixelUnits:
				# No need to check for equality because the try block does this already.
				if movementUnit < unit:
					movementUnit = unit
					break
		config.conf["goldenCursor"]["mouseMovementUnit"] = movementUnit
		ui.message(str(movementUnit))

	@scriptHandler.script(
		# Translators: Input help message for a Golden Cursor add-on command.
		description=_("toggles reporting of mouse coordinates in pixels when mouse moves"),
		gesture="kb:nvda+windows+s"
	)
	def script_toggleSpeakPixels(self, gesture):
		sayPixel = config.conf["goldenCursor"]["reportNewMouseCoordinates"]
		sayPixel = not sayPixel
		if sayPixel:
			# Translators: reported when new mouse coordinate announcement is on.
			ui.message(_("Report new mouse coordinates on"))
		else:
			# Translators: reported when new mouse coordinate announcement is on.
			ui.message(_("Report new mouse coordinates off"))
		config.conf["goldenCursor"]["reportNewMouseCoordinates"] = sayPixel

	@scriptHandler.script(
		# Translators: Input help message for a Golden Cursor command.
		description=_("Reports current X and Y mouse position"),
		gesture="kb:nvda+windows+p"
	)
	def script_sayPosition(self, gesture):
		reportMousePosition()

	@scriptHandler.script(
		# Translators: input help mode message for a Golden Cursor add-on command.
		description=_("Toggles mouse arrows to move the mouse with the arrow keys"),
		gesture="kb:nvda+windows+m"
	)
	def script_toggleMouseArrows(self, gesture):
		self.mouseArrows = not self.mouseArrows
		if self.mouseArrows:
			self.bindGesture("kb:rightArrow", "moveMouseRight")
			self.bindGesture("kb:leftArrow", "moveMouseLeft")
			self.bindGesture("kb:downArrow", "moveMouseDown")
			self.bindGesture("kb:upArrow", "moveMouseUp")
			# Translators: presented when toggling mouse arrows feature.
			ui.message(_("Mouse arrows on"))
		else:
			self.clearGestureBindings()
			self.bindGestures(self.__gestures)
			# Translators: presented when toggling mouse arrows feature.
			ui.message(_("Mouse arrows off"))

	@scriptHandler.script(
		# Translators: Input help message for a Golden Cursor command.
		description=_("Moves the Mouse pointer to the right"),
		gesture="kb:nvda+windows+rightArrow"
	)
	def script_moveMouseRight(self, gesture):
		self.moveMouse(GCMouseRight)

	@scriptHandler.script(
		# Translators: Input help message for a Golden Cursor command.
		description=_("Moves the Mouse pointer to the left"),
		gesture="kb:nvda+windows+leftArrow"
	)
	def script_moveMouseLeft(self, gesture):
		self.moveMouse(GCMouseLeft)

	@scriptHandler.script(
		# Translators: Input help message for a Golden Cursor command.
		description=_("Moves the Mouse pointer down"),
		gesture="kb:nvda+windows+downArrow"
	)
	def script_moveMouseDown(self, gesture):
		self.moveMouse(GCMouseDown)

	@scriptHandler.script(
		# Translators: Input help message for a Golden Cursor command.
		description=_("Moves the Mouse pointer up"),
		gesture="kb:nvda+windows+upArrow"
	)
	def script_moveMouseUp(self, gesture):
		self.moveMouse(GCMouseUp)

	@scriptHandler.script(
		# Translators: Input help message for a Golden Cursor command.
		description=_("Opens a dialog to enter the X and Y coordinates for the mouse to move to"),
		gesture="kb:nvda+windows+j"
	)
	def script_goToPosition(self, gesture):
		try:
			d = PositionsList(parent=gui.mainFrame, goto=True)
			gui.mainFrame.prePopup()
			d.Raise()
			d.Show()
			gui.mainFrame.postPopup()
		except RuntimeError:
			pass

	@scriptHandler.script(
		# Translators: Input help message for a Golden Cursor command.
		description=_("Toggles mouse movement restriction between current application and unrestricted"),
		gesture="kb:nvda+windows+r"
	)
	def script_toggleMouseRestriction(self, gesture):
		self.getAppRestriction = self.getMouse()
		self.restriction = not self.restriction
		if self.restriction:
			# Translators: presented when mouse movement is restricted to current application.
			ui.message(_("Mouse movement restricted to current application"))
		else:
			# Translators: presented when mouse movement is unrestricted.
			ui.message(_("Mouse movement unrestricted"))

	def moveMouse(self, direction):
		w, h = api.getDesktopObject().location[2:]
		x, y = winUser.getCursorPos()
		oldX, oldY = x, y
		pixelMoving = config.conf["goldenCursor"]["mouseMovementUnit"]
		if direction == GCMouseRight:
			x += pixelMoving
		elif direction == GCMouseLeft:
			x -= pixelMoving
		elif direction == GCMouseDown:
			y += pixelMoving
		elif direction == GCMouseUp:
			y -= pixelMoving
		# Just do a chain comparison, as it is a lot faster.
		if 0 <= x < w and 0 <= y < h:
			setMousePosition(x, y)
		else:
			wx.Bell()
			return
		if self.restriction and self.getAppRestriction.appModule.appName != self.getMouse().appModule.appName:
			wx.Bell()
			setMousePosition(oldX, oldY)
			if self.getAppRestriction.appModule.appName != self.getMouse().appModule.appName:
				x, y, w, h = self.getAppRestriction.location
				setMousePosition(x, y)
			return
		if config.conf["goldenCursor"]["reportNewMouseCoordinates"]:
			ui.message(str(x if direction in (GCMouseRight, GCMouseLeft) else y))

	def getMouse(self):
		return api.getDesktopObject().objectFromPoint(*winUser.getCursorPos())


# Add-on config database
# Borrowed from Enhanced Touch Gestures by Joseph Lee
confspec = {
	"reportNewMouseCoordinates": "boolean(default=true)",
	"mouseMovementUnit": "integer(min=1, max=100, default=5)",
}
config.conf.spec["goldenCursor"] = confspec


class GoldenCursorSettings(gui.settingsDialogs.SettingsPanel):
	# Translators: This is the label for the Golden Cursor settings category in NVDA Settings screen.
	title = _("Golden Cursor")

	def makeSettings(self, settingsSizer):
		gcHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		self.mouseCoordinatesCheckBox = gcHelper.addItem(
			# Translators: This is the label for a checkbox in the
			# Golden Cursor settings dialog.
			wx.CheckBox(self, label=_("&Announce new mouse coordinates when mouse moves"))
		)
		self.mouseCoordinatesCheckBox.SetValue(config.conf["goldenCursor"]["reportNewMouseCoordinates"])
		self.mouseMovementUnit = gcHelper.addLabeledControl(
			# Translators: The label for a setting in Golden Cursor settings dialog to change mouse movement units.
			_("Mouse movement &unit (in pixels)"), gui.nvdaControls.SelectOnFocusSpinCtrl,
			min=1, max=100, initial=config.conf["goldenCursor"]["mouseMovementUnit"]
		)

	def onSave(self):
		config.conf["goldenCursor"]["reportNewMouseCoordinates"] = self.mouseCoordinatesCheckBox.IsChecked()
		config.conf["goldenCursor"]["mouseMovementUnit"] = self.mouseMovementUnit.Value
