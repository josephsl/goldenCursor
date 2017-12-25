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
		self.positions = ConfigObj(os.path.join(GCSavedPositions, appName+".gc"), encoding="UTF-8")
		listBoxSizer = wx.BoxSizer(wx.VERTICAL)
		self.listBox = wx.ListBox(self,-1)
		listBoxSizer.Add(self.listBox,0,wx.ALL| wx.EXPAND,10)
		for entry in sorted(self.positions.keys()):
			self.listBox.Append(entry, self.positions[entry])
		buttonsSizer = wx.BoxSizer(wx.VERTICAL)
		b_rename = wx.Button(self, -1,_('&rename'))
		buttonsSizer.Add(b_rename,0, wx.ALL| wx.CENTER| wx.EXPAND,10)
		b_delete = wx.Button(self, -1,_('&delete'))
		buttonsSizer.Add(b_delete, 0, wx.ALL| wx.CENTER| wx.EXPAND,10)
		b_clear = wx.Button(self, -1,_('c&lear'))
		buttonsSizer.Add(b_clear, 0, wx.ALL| wx.CENTER| wx.EXPAND,10)
		buttonsSizer.Add(self.CreateButtonSizer(wx.OK), wx.ALL| wx.CENTER|wx.EXPAND,10)
		buttonsSizer.Add(self.CreateButtonSizer(wx.CANCEL), wx.ALL| wx.CENTER|wx.EXPAND,10)
		b_rename.Bind(wx.EVT_BUTTON, self.onRename)
		b_delete.Bind(wx.EVT_BUTTON, self.onDelete)
		b_clear.Bind(wx.EVT_BUTTON, self.onClear)
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		h = wx.BoxSizer(wx.HORIZONTAL)
		h.Add(listBoxSizer,1,wx.ALL|wx.EXPAND,20)
		h.Add(buttonsSizer)
		self.listBox.SetFocus()
		self.listBox.SetSelection(0)
		self.CenterOnScreen()
		self.SetSizer(h)
		self.Show()

	def onRename(self, event):
		index = self.listBox.Selection
		oldName = self.listBox.StringSelection
		name = wx.GetTextFromUser(_('Edit'),_('Rename'),self.listBox.StringSelection)
		# When escape is pressed, an empty string is returned.
		if name in ("", oldName): return
		self.listBox.SetString(index, name)
		self.listBox.SetSelection(index)
		self.listBox.SetFocus()
		self.positions[name] = self.positions[oldName]
		del self.positions[oldName]

	def onDelete(self,event):
		entry = self.listBox.GetStringSelection()
		del self.positions[entry]
		ui.message(_('the position has been deleted.'))
		self.listBox.Delete(self.listBox.GetSelection())
		if self.listBox.IsEmpty():
			os.remove(self.positions.filename)
			t1 = Timer(0.2,speech.cancelSpeech)
			t2 = Timer(0.4,ui.message,[_('the list has been cleared.')])
			t1.start()
			t2.start()
			self.Close()

	def onClear(self, event):
		os.remove(self.positions.filename)
		t1 = Timer(0.2,speech.cancelSpeech)
		t2 = Timer(0.4,ui.message,[_('the list has been cleared.')])
		t1.start()
		t2.start()
		self.Close()

	def onOk(self, event):
		self.positions.write()
		try:
			x, y= self.positions[self.listBox.GetStringSelection()].split(",")
		except:
			return
		self.positions = None
		winUser.setCursorPos(int(x), int(y))
		t = Timer(0.5, mouseHandler.executeMouseMoveEvent,[int(x), int(y)])
		t.start()
		self.Destroy()

	def onCancel(self,evt):
		self.positions.write()
		self.positions = None
		self.Destroy()


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
		ui.message(_('the position has been saved in %s.') % position.filename)
	script_savePosition.__doc__ = _('to save a the current position.')

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
	script_mouseMovementChange.__doc__ = _('to select a value for mouse movement (1, 10, 20, 50. 100.')

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
	script_sayPosition.__doc__ = _('report the positions of the mouse.')

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
	script_moveMouseRight.__doc__ = _('Moves the Mouse pointer right.')

	def script_moveMouseLeft(self,gesture):
		self.moveMouse(GCMouseLeft)
	script_moveMouseLeft.__doc__ = _('Moves the Mouse pointer left.')

	def script_moveMouseDown(self,gesture):
		self.moveMouse(GCMouseDown)
	script_moveMouseDown.__doc__ = _('Moves the Mouse pointer down.')

	def script_moveMouseUp(self,gesture):
		self.moveMouse(GCMouseUp)
	script_moveMouseUp.__doc__ = _('Moves the Mouse pointer up.')

	def script_goToPosition(self,gesture):
		try:
			d = PositionJumpDialog(gui.mainFrame)
			gui.mainFrame.prePopup()
			d.Raise()
			d.Show()
			gui.mainFrame.postPopup()
		except RuntimeError:
			pass
	script_goToPosition.__doc__ = _('type the x/y value you wish the cursor to jump to')

	def script_toggleMouseRestriction(self,gesture):
		self.getAppRestriction = self.getMouse()
		self.restriction = not self.restriction
		if self.restriction:
			ui.message(_('restriction on'))
			tones.beep(1000, 200)
		else:
			ui.message(_('restriction off'))
			tones.beep(500, 200)
	script_toggleMouseRestriction.__doc__ = _('Toggles the restriction between the 2 levels you can toggle between Application Window restriction and Unrestricted.')

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
