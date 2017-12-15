# -*- coding: utf-8 -*-
#golden cursor
# Copyright (C) 2015-2017
#Version 2.2
#License GNU GPL
# Date: 25/12/2015
#team work: author : salah atair, translation and keycommands are made by wafeeq taher
# Additional tweaking done by Joseph Lee and contributors, resetting version to 1.0.

# Control mouse from the keyboard, including specifying hotspots, different movement units, mouse restrictions and others.

import codecs
from threading import Timer
import wx
import gui
import os
import speech
import tones
import globalPluginHandler
import mouseHandler
import ui
import api
import winUser
import addonHandler
addonHandler.initTranslation()

# Each global constant is prefixed with "GC".

# Constants
GCFilesPath = os.path.join(os.path.dirname(__file__), "files")
# Mouse movement directions
GCMouseRight = 0
GCMouseLeft = 1
GCMouseDown = 2
GCMouseUp = 3

class PositionsList(wx.Dialog):

	def __init__(self, parent, appName):
		super(PositionsList, self).__init__(parent, title=_("Saved positions for %s")%(appName), size =(420, 300))
		self.path = os.path.join(GCFilesPath, appName+".gc")
		with codecs.open(self.path, "r", "utf-8") as f:
			self.data = f.read().strip()
		self.data = self.data.split("\n")
		listBoxSizer = wx.BoxSizer(wx.VERTICAL)
		st = wx.StaticText(self,-1,_('choose a item of this list'))
		listBoxSizer.Add(st,0.5, wx.ALL, 10)
		self.listBox = wx.ListBox(self,-1)
		listBoxSizer.Add(self.listBox,0,wx.ALL| wx.EXPAND,10)
		for i in self.data:
			if i [0] == "[":
				self.listBox.Append(i[1:-1], self.data [self.data.index(i)+1])
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
		try:
			index = self.data.index("["+self.listBox.GetStringSelection()+"]")
		except:
			ui.message(_('no selection'))
			return
		oldName = self.listBox.StringSelection
		name = wx.GetTextFromUser(_('Edit'),_('Rename'),self.listBox.StringSelection)
		# When escape is pressed, an empty string is returned.
		if name == "" or name == oldName:
			return
		self.listBox.SetFocus()
		x_y = self.listBox.GetClientData(self.listBox.GetSelection())
		del self.data [index]
		self.data.insert(index, "["+name+"]")
		data = "\n".join(self.data)
		with codecs.open(self.path, "w", "utf-8") as f:
			f.write(data)
		i = self.listBox.GetSelection()
		self.listBox.Delete(i)
		self.listBox.Insert(name,i)
		self.listBox.SetClientData(i,x_y)
		self.listBox.SetSelection(i)

	def onDelete(self,event):
		try:
			index = self.data.index("["+self.listBox.GetStringSelection()+"]")
		except:
			ui.message(_('no selection'))
			return
		del self.data [index]
		del self.data [index]
		ui.message(_('the position has been deleted.'))
		data = "\n".join(self.data)
		with codecs.open(self.path, "w", "utf-8") as f:
			f.write(data)
		self.listBox.Delete(self.listBox.GetSelection())
		if self.listBox.IsEmpty():
			os.remove(self.path)
			t1 = Timer(0.2,speech.cancelSpeech)
			t2 = Timer(0.4,ui.message,[_('the list has been cleared.')])
			t1.start()
			t2.start()
			self.Close()

	def onClear(self, event):
		os.remove(self.path)
		t1 = Timer(0.2,speech.cancelSpeech)
		t2 = Timer(0.4,ui.message,[_('the list has been cleared.')])
		t1.start()
		t2.start()
		self.Close()

	def onOk(self, event):
		try:
			x, y= self.listBox.GetClientData(self.listBox.GetSelection()).split(",")
		except:
			return
		x =int(x)
		y = int(y)
		winUser.setCursorPos(x,y)
		t = Timer(0.5, mouseHandler.executeMouseMoveEvent,[x, y])
		t.start()
		self.Close()

	def onCancel(self,evt):
		self.Destroy()


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	scriptCategory = "golden cursor"

	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		self.pixelMoving =5
		self.sayPixel = True
		self.getAppRestriction = None
		self.restriction = False

	def script_savedPositionsList(self, gesture):
		# Don't even think about opening this dialog if positions list does not exist.
		appName = api.getForegroundObject().appModule.appName
		if not os.path.exists(os.path.join(GCFilesPath, appName+".gc")):
			# Translators: message presented when no saved positions are available for the focused app.
			ui.message(_("No saved positions for %s.")%appName)
		else:
			PositionsList(gui.mainFrame, appName)
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
		if not os.path.exists(GCFilesPath): os.mkdir(filesPath)
		path = os.path.join(GCFilesPath, appName+".gc")
		name = "["+name+"]"
		p = name+"\n"+str(x)+","+str(y)
		try:
			with codecs.open(path, "r", "utf-8") as f:
				data = f.read().strip()
		except Exception as e:
			data = ""
		if name in data:
			data = data.split("\n")
			i = data.index(name)
			del data [i]
			del data [i]
			data = "\n".join(data)
			p = data+"\n"+p
		else:
			p = data+"\n"+p
		with codecs.open(path, "w", "utf-8") as f:
			f.write(p)
			ui.message(_('the position has been saved in %s.') % path)
	script_savePosition.__doc__ = _('to save a the current position.')

	def script_mouseMovementChange (self, gesture):
		pixelUnits = (1, 5, 10, 20, 50, 100)
		pixelUnitChoices = len(pixelUnits)
		index = pixelUnits.index(self.pixelMoving)
		self.pixelMoving = pixelUnits[(index+1) % pixelUnitChoices]
		ui.message(str(self.pixelMoving))
	script_mouseMovementChange.__doc__ = _('to select a value for mouse movement (1, 10, 20, 50. 100.')

	def script_toggleSpeakPixels(self, gesture):
		self.sayPixel = not self.sayPixel
		if self.sayPixel:
			ui.message(_('report pixels on'))
			tones.beep(1000, 200)
		else:
			ui.message(_('report pixels off'))
			tones.beep(500, 200)
	script_toggleSpeakPixels.__doc__ = _('toggle reporting of pixels')

	def script_sayPosition(self,gesture):
		x, y = winUser.getCursorPos()
		ui.message(_("%d , %d"%(x,y)))
	script_sayPosition.__doc__ = _('report the positions of the mouse.')

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
		d = wx.TextEntryDialog(gui.mainFrame, _("Enter the value for position number you wish to jump to"), _("Jump to position"))
		def callback(result):
			if result == wx.ID_OK:
				wx.CallLater(100,self.jumping, d.GetValue())
		gui.runScriptModalDialog(d, callback)

	def jumping(self,num):
		speech.cancelSpeech()
		if "," not in num:
			wx.CallAfter(gui.messageBox, _("please enter comma between the first and the second number"), _("Error"), wx.OK|wx.ICON_ERROR)
			return
		num = num.replace(" ", "")
		num = num.split(",")
		x = num [0]
		y = num [1]
		if x.isdigit() == False or y.isdigit() == False:
			wx.CallAfter(gui.messageBox, _("please enter an integer number."), _("Error"), wx.OK|wx.ICON_ERROR)
			return
		x = int(x)
		y = int(y)
		winUser.setCursorPos(x,y)
		self.getMouse()
		ui.message(str(x)+','+ str(y))
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
		if direction == GCMouseRight: x+=self.pixelMoving
		elif direction == GCMouseLeft: x-=self.pixelMoving
		elif direction == GCMouseDown: y+=self.pixelMoving
		elif direction == GCMouseUp: y-=self.pixelMoving
		# Just do a chain comparison, as it is a lot faster.
		if 0 <= x < w and 0 <= y < h:
			winUser.setCursorPos(x,y)
			mouseHandler.executeMouseMoveEvent(x, y)
		else:
			wx.Bell()
			return
		if self.restriction and self.getAppRestriction.appModule.appName != self.getMouse().appModule.appName:
			wx.Bell()
			winUser.setCursorPos(oldX,oldY)
			mouseHandler.executeMouseMoveEvent(oldX, oldY)
			if self.getAppRestriction.appModule.appName != self.getMouse().appModule.appName:
				x,y, w, h = self.getAppRestriction.location
				winUser.setCursorPos(x,y)
				mouseHandler.executeMouseMoveEvent(x, y)
			return
		if self.sayPixel:
			ui.message(str(x if direction in (GCMouseRight, GCMouseLeft) else y))

	def getMouse(self):
		x , y= winUser.getCursorPos()
		return api.getDesktopObject().objectFromPoint(x,y)

	__gestures = {
		"kb:nvda+windows+c":"mouseMovementChange",
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
