# -*- coding: utf-8 -*-
#golden cursor
# Copyright (C) 2015-2017
#Version 2.2
#License GNU GPL
# Date: 25/12/2015
#team work: author : salah atair, translation and keycommands are made by wafeeq taher
# Additional tweaking done by Joseph Lee and contributors, resetting version to 1.0.

# Control mouse from the keyboard, including specifying hotspots, different movement units, mouse restrictions and others.

import os
from threading import Timer
from configobj import ConfigObj
import globalPluginHandler
import gui
import wx
import config
import speech
import tones
import globalVars
import mouseHandler
import ui
import api
import winUser
import addonHandler
addonHandler.initTranslation()

# Each global constant is prefixed with "GC".

# Constants
GCSavedPositions = os.path.join(globalVars.appArgs.configPath, "addons", "goldenCursor", "savedPositions")
# Mouse movement directions
GCMouseRight = 0
GCMouseLeft = 1
GCMouseDown = 2
GCMouseUp = 3

# Reports mouse position, used in various places.
def reportMousePosition(x=None, y=None):
	# The coordinates are keywords so specific position can be announced if needed.
	cursorPos = winUser.getCursorPos()
	if x is None: x = cursorPos[0]
	if y is None: y = cursorPos[1]
	ui.message("{0}, {1}".format(x, y))

def setMousePosition(x, y, announceMousePosition=False):
	# Setter version of report mouse position function.
	# The new position announcement is to be used if needed.
	winUser.setCursorPos(x, y)
	mouseHandler.executeMouseMoveEvent(x, y)
	if announceMousePosition:
		# Announce this half a second later to give the appearance of mouse movement.
		wx.CallLater(500, reportMousePosition, x=x, y=y)
	

class PositionsList(wx.Dialog):

	def __init__(self, parent, appName):
		super(PositionsList, self).__init__(parent, title=_("Saved positions for %s")%(appName), size =(420, 300))
		self.appName = appName
		self.positions = ConfigObj(os.path.join(GCSavedPositions, appName+".gc"), encoding="UTF-8")
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		listBoxSizer = wx.BoxSizer(wx.VERTICAL)
		self.listBox = wx.ListCtrl(self,-1,style=wx.LC_REPORT|wx.LC_SINGLE_SEL,size=(550,350))
		# Translators: the column in saved positions list to identify the position name.
		self.listBox.InsertColumn(0,_("Name"),width=150)
		# Translators: the column in saved positions list to identify the X coordinate.
		self.listBox.InsertColumn(1,_("Position X"),width=50)
		# Translators: the column in saved positions list to identify the Y coordinate.
		self.listBox.InsertColumn(2,_("Position Y"),width=50)
		self.listBox.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.onJump)
		listBoxSizer.Add(self.listBox,proportion=8)
		for entry in sorted(self.positions.keys()):
			x, y = self.positions[entry].split(",")
			self.listBox.Append((entry, x, y))
		self.listBox.Select(0,on=1)
		self.listBox.SetItemState(0,wx.LIST_STATE_FOCUSED,wx.LIST_STATE_FOCUSED)
		buttonsSizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: the button to jump to the selected position.
		jumpButton= wx.Button(self, -1,_("&Jump"))
		jumpButton.Bind(wx.EVT_BUTTON, self.onJump)
		buttonsSizer.Add(jumpButton,0, wx.ALL| wx.CENTER| wx.EXPAND,10)
		# Translators: the button to rename a saved position.
		renameButton= wx.Button(self, -1,_("&Rename"))
		renameButton.Bind(wx.EVT_BUTTON, self.onRename)
		buttonsSizer.Add(renameButton,0, wx.ALL| wx.CENTER| wx.EXPAND,10)
		# Translators: the button to delete the selected saved position.
		deleteButton = wx.Button(self, -1,_("&Delete"))
		deleteButton.Bind(wx.EVT_BUTTON, self.onDelete)
		buttonsSizer.Add(deleteButton, 0, wx.ALL| wx.CENTER| wx.EXPAND,10)
		# Translators: the button to clear all saved positions for the focused app.
		clearButton = wx.Button(self, -1,_("C&lear positions"))
		clearButton.Bind(wx.EVT_BUTTON, self.onClear)
		buttonsSizer.Add(clearButton, 0, wx.ALL| wx.CENTER| wx.EXPAND,10)
		mainSizer.Add(listBoxSizer,1,wx.ALL|wx.EXPAND,20)
		mainSizer.Add(buttonsSizer)
		# Translators: The label of a button to close the saved positions dialog.
		closeButton = wx.Button(self, label=_("&Close"), id=wx.ID_CLOSE)
		closeButton.Bind(wx.EVT_BUTTON, lambda evt: self.Close())
		mainSizer.Add(closeButton,border=20,flag=wx.LEFT|wx.RIGHT|wx.BOTTOM|wx.CENTER|wx.ALIGN_RIGHT)
		self.Bind(wx.EVT_CLOSE, self.onClose)
		self.EscapeId = wx.ID_CLOSE
		# Borrowed from NVDA Core (add-ons manager).
		self.listBox.SetFocus()
		self.Center(wx.BOTH | 6)
		mainSizer.Fit(self)
		self.SetSizer(mainSizer)
		# 6 = wx.CENTER_ON_SCREEN.
		self.Center(wx.BOTH | 6)

	def onRename(self, event):
		index = self.listBox.GetFirstSelected()
		oldName = self.listBox.GetItemText(index)
		# Translators: The label of a field to enter a new name for a saved position/tag.
		name = wx.GetTextFromUser(_("New name"),
		# Translators: The title of the dialog to rename a saved position.
		_("Rename"), oldName)
		# When escape is pressed, an empty string is returned.
		if name in ("", oldName): return
		if name in self.positions:
			# Translators: An error displayed when renaming a saved position
			# and a tag with the new name already exists.
			gui.messageBox(_("Another saved position has the same name as the new name. Please choose a different name."),
				_("Error"), wx.OK | wx.ICON_ERROR, self)
			return
		self.listBox.SetItemText(index, name)
		self.listBox.SetFocus()
		self.positions[name] = self.positions[oldName]
		del self.positions[oldName]

	def deletePosition(self, clearPositions=False):
		message, title = "", ""
		entry = self.listBox.GetFirstSelected()
		name = self.listBox.GetItemText(entry)
		if not clearPositions:
			# Translators: The confirmation prompt displayed when the user requests to delete the selected tag.
			message = _("Are you sure you want to delete the position named {name}? This cannot be undone.".format(name = name))
			# Translators: The title of the confirmation dialog for deletion of selected position.
			title = _("Delete position")
		else:
			# Translators: The confirmation prompt displayed when the user is about to clear positions.
			message = _("Are you sure you want to clear saved positions for the current application ({appName})? This cannot be undone.".format(appName= self.appName))
			# Translators: The title of the confirmation dialog for clearing saved positions.
			title = _("Clear saved positions")
		if gui.messageBox(message, title, wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION, self
		) == wx.NO:
			return
		if not clearPositions:
			del self.positions[name]
			self.listBox.DeleteItem(entry)
			self.positions.write()
			if self.listBox.GetItemCount() > 0: self.listBox.Select(0,on=1)
		if clearPositions or self.listBox.GetItemCount() == 0:
			os.remove(self.positions.filename)
			self.positions.clear()
			# Translators: A dialog message shown when tags for the application is cleared.
			gui.messageBox(_("All saved positions for the application {appName} has been deleted.".format(appName = self.appName)),
			# Translators: Title of the tag clear confirmation dialog.
			_("Saved positions cleared"), wx.OK|wx.ICON_INFORMATION)
			self.Close()

	def onDelete(self,event):
		self.deletePosition()

	def onClear(self, event):
		self.deletePosition(clearPositions=True)

	def onJump(self, event):
		self.Destroy()
		self.positions.write()
		try:
			x, y= self.positions[self.listBox.GetItemText(self.listBox.GetFirstSelected())].split(",")
		except:
			return
		self.positions = None
		wx.CallLater(500, setMousePosition, int(x), int(y))

	def onClose(self,evt):
		self.Destroy()
		if len(self.positions): self.positions.write()
		self.positions = None


class PositionJumpDialog(wx.Dialog):

	# The following comes from exit dialog class from GUI package (credit: NV Access and Zahari from Bulgaria).
	_instance = None

	def __new__(cls, parent, *args, **kwargs):
		inst = cls._instance() if cls._instance else None
		if not inst:
			return super(cls, cls).__new__(cls, parent, *args, **kwargs)
		return inst

	def __init__(self, parent, level=0):
		inst = PositionJumpDialog._instance() if PositionJumpDialog._instance else None
		if inst:
			return
		# Use a weakref so the instance can die.
		import weakref
		PositionJumpDialog._instance = weakref.ref(self)

		super(PositionJumpDialog, self).__init__(parent, wx.ID_ANY, _("New mouse position"))
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		mouseJumpHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		x, y = winUser.getCursorPos()
		w,h = api.getDesktopObject().location[2:]
		self.xPos = mouseJumpHelper.addLabeledControl(_("&X position"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=0, max=w-1, initial=x)
		self.yPos = mouseJumpHelper.addLabeledControl(_("&Y position"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=0, max=h-1, initial=y)

		mouseJumpHelper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Add(mouseJumpHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.SetSizer(mainSizer)
		self.Center(wx.BOTH | 6)
		self.xPos.SetFocus()

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
		self.prefsMenu = gui.mainFrame.sysTrayIcon.preferencesMenu
		self.gcSettings = self.prefsMenu.Append(wx.ID_ANY, _("&Golden Cursor..."), _("Golden Cursor add-on settings"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onConfigDialog, self.gcSettings)

	def onConfigDialog(self, evt):
		gui.mainFrame._popupSettingsDialog(GoldenCursorSettings)

	def terminate(self):
		try:
			self.prefsMenu.RemoveItem(self.gcSettings)
		except (RuntimeError, AttributeError, wx.PyDeadObjectError):
			pass

	def script_savedPositionsList(self, gesture):
		# Don't even think about opening this dialog if positions list does not exist.
		appName = api.getForegroundObject().appModule.appName
		if not os.path.exists(os.path.join(GCSavedPositions, appName+".gc")):
			# Translators: message presented when no saved positions are available for the focused app.
			ui.message(_("No saved positions for %s.")%appName)
		else:
			try:
				d = PositionsList(gui.mainFrame, appName)
				gui.mainFrame.prePopup()
				d.Raise()
				d.Show()
				gui.mainFrame.postPopup()
			except RuntimeError:
				pass
	# Translators: input help message for a Golden Cursor command.
	script_savedPositionsList.__doc__ = _("Opens a dialog listing saved positions for the current application")

	def script_savePosition(self, gesture):
		d = wx.TextEntryDialog(gui.mainFrame, _("Enter the value for position name you wish to save."), _("save position"))
		def callback(result):
			if result == wx.ID_OK:
				wx.CallLater(100,self.saving, d.GetValue())
		gui.runScriptModalDialog(d, callback)

	def saving(self,name):
		name = name.rstrip()
		speech.cancelSpeech()
		if name == "":
			wx.CallAfter(gui.messageBox, _("please enter the value for the name of the position."), _("Error"), wx.OK|wx.ICON_ERROR)
			return
		x, y = winUser.getCursorPos()
		appName = self.getMouse().appModule.appName
		# If the files path does not exist, create it now.
		if not os.path.exists(GCSavedPositions): os.mkdir(GCSavedPositions)
		position = ConfigObj(os.path.join(GCSavedPositions, appName+".gc"), encoding="UTF-8")
		position[name] = ",".join([str(x), str(y)])
		position.write()
		# Translators: presented when position (tag) has been saved.
		ui.message(_("Position has been saved in %s.") % position.filename)
	# Translators: Input help message for a Golden Cursor command.
	script_savePosition.__doc__ = _("Opens a dialog to label the current mouse position and saves it")

	def script_mouseMovementChange (self, gesture):
		pixelUnits = (1, 5, 10, 20, 50, 100)
		movementUnit = config.conf["goldenCursor"]["mouseMovementUnit"]
		pixelUnitChoices = len(pixelUnits)
		try:
			index = pixelUnits.index(movementUnit)
			movementUnit = pixelUnits[(index+1) % pixelUnitChoices]
		except ValueError:
			for unit in pixelUnits:
				# No need to check for equality because the try block does this already.
				if movementUnit < unit:
					movementUnit = unit
					break
		config.conf["goldenCursor"]["mouseMovementUnit"] = movementUnit
		ui.message(str(movementUnit))
	# Translators: input help message for a Golden Cursor command.
	script_mouseMovementChange.__doc__ = _("Changes mouse movement unit")

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
	# Translators: Input help message for a Golden Cursor add-on command.
	script_toggleSpeakPixels.__doc__ = _("toggles reporting of mouse coordinates in pixels when mouse moves")

	def script_sayPosition(self,gesture):
		reportMousePosition()
	# Translators: Input help message for a Golden Cursor command.
	script_sayPosition.__doc__ = _("Reports current X and Y mouse position")

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
	# Translators: input help mode message for a Golden Cursor add-on command.
	script_toggleMouseArrows.__doc__=_("Toggles mouse arrows to move the mouse with the arrow keys")

	def script_moveMouseRight(self,gesture):
		self.moveMouse(GCMouseRight)
	
	# Translators: Input help message for a Golden Cursor command.
	script_moveMouseRight.__doc__ = _("Moves the Mouse pointer to the right")

	def script_moveMouseLeft(self,gesture):
		self.moveMouse(GCMouseLeft)
	# Translators: Input help message for a Golden Cursor command.
	script_moveMouseLeft.__doc__ = _("Moves the Mouse pointer to the left")

	def script_moveMouseDown(self,gesture):
		self.moveMouse(GCMouseDown)
	# Translators: Input help message for a Golden Cursor command.
	script_moveMouseDown.__doc__ = _("Moves the Mouse pointer down")

	def script_moveMouseUp(self,gesture):
		self.moveMouse(GCMouseUp)
	# Translators: Input help message for a Golden Cursor command.
	script_moveMouseUp.__doc__ = _("Moves the Mouse pointer up")

	def script_goToPosition(self,gesture):
		try:
			d = PositionJumpDialog(gui.mainFrame)
			gui.mainFrame.prePopup()
			d.Raise()
			d.Show()
			gui.mainFrame.postPopup()
		except RuntimeError:
			pass
	# Translators: Input help message for a Golden Cursor command.
	script_goToPosition.__doc__ = _("Opens a dialog to enter the X and Y coordinates for the mouse to move to")

	def script_toggleMouseRestriction(self,gesture):
		self.getAppRestriction = self.getMouse()
		self.restriction = not self.restriction
		if self.restriction:
			ui.message(_('restriction on'))
			tones.beep(1000, 200)
		else:
			ui.message(_('restriction off'))
			tones.beep(500, 200)
	# Translators: Input help message for a Golden Cursor command.
	script_toggleMouseRestriction.__doc__ = _("Toggles mouse movement restriction between current application and unrestricted")

	def moveMouse(self, direction):
		w,h = api.getDesktopObject().location[2:]
		x , y= winUser.getCursorPos()
		oldX, oldY = x, y
		pixelMoving = config.conf["goldenCursor"]["mouseMovementUnit"]
		if direction == GCMouseRight: x+=pixelMoving
		elif direction == GCMouseLeft: x-=pixelMoving
		elif direction == GCMouseDown: y+=pixelMoving
		elif direction == GCMouseUp: y-=pixelMoving
		# Just do a chain comparison, as it is a lot faster.
		if 0 <= x < w and 0 <= y < h:
			setMousePosition(x, y)
		else:
			wx.Bell()
			return
		if self.restriction and self.getAppRestriction.appModule.appName != self.getMouse().appModule.appName:
			wx.Bell()
			setMousePosition(oldX,oldY)
			if self.getAppRestriction.appModule.appName != self.getMouse().appModule.appName:
				x,y, w, h = self.getAppRestriction.location
				setMousePosition(x, y)
			return
		if config.conf["goldenCursor"]["reportNewMouseCoordinates"]:
			ui.message(str(x if direction in (GCMouseRight, GCMouseLeft) else y))

	def getMouse(self):
		return api.getDesktopObject().objectFromPoint(*winUser.getCursorPos())

	__gestures = {
		"kb:nvda+windows+c":"mouseMovementChange",
		"kb:nvda+windows+m":"toggleMouseArrows",
		"kb:nvda+windows+rightArrow":"moveMouseRight",
		"kb:nvda+windows+leftArrow":"moveMouseLeft",
		"kb:nvda+windows+downArrow":"moveMouseDown",
		"kb:nvda+windows+upArrow":"moveMouseUp",
		"kb:nvda+windows+j":"goToPosition",
		"kb:nvda+windows+p":"sayPosition",
		"kb:nvda+windows+s":"toggleSpeakPixels",
		"kb:nvda+windows+r":"toggleMouseRestriction",
		"kb:nvda+shift+l": "savePosition",
		"kb:nvda+control+l": "savedPositionsList",
	}

# Add-on config database
# Borrowed from Enhanced Touch Gestures by Joseph Lee
confspec = {
	"reportNewMouseCoordinates": "boolean(default=true)",
	"mouseMovementUnit": "integer(min=1, max=100, default=5)",
}
config.conf.spec["goldenCursor"] = confspec

class GoldenCursorSettings(gui.SettingsDialog):
	# Translators: This is the label for the Golden Cursor settings dialog.
	title = _("Golden Cursor Settings")

	def makeSettings(self, settingsSizer):
		gcHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		# Translators: This is the label for a checkbox in the
		# Golden Cursor settings dialog.
		self.mouseCoordinatesCheckBox=gcHelper.addItem(wx.CheckBox(self, label=_("&Announce new mouse coordinates when mouse moves")))
		self.mouseCoordinatesCheckBox.SetValue(config.conf["goldenCursor"]["reportNewMouseCoordinates"])
		# Translators: The label for a setting in Golden Cursor settings dialog to change mouse movement units.
		self.mouseMovementUnit=gcHelper.addLabeledControl(_("Mouse movement &unit (in pixels)"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=1, max=100, initial=config.conf["goldenCursor"]["mouseMovementUnit"])

	def postInit(self):
		self.mouseCoordinatesCheckBox.SetFocus()

	def onOk(self,evt):
		config.conf["goldenCursor"]["reportNewMouseCoordinates"] = self.mouseCoordinatesCheckBox.IsChecked()
		config.conf["goldenCursor"]["mouseMovementUnit"] = self.mouseMovementUnit.Value
		super(GoldenCursorSettings, self).onOk(evt)
