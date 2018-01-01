# Golden Cursor installation tasks
# Copyright 2016-2018 Joseph Lee and others, released under GPL.

# Provides needed routines during add-on installation and removal.
# Routines are partly based on other add-ons, particularly Place Markers by Noelia Martinez (thanks add-on authors).
# File copying operation comes from StationPlaylist Studio add-on by Joseph Lee.

import addonHandler
import os
import shutil

def onInstall():
	# First and second generation positions storage format are incompatible.
	positions = os.path.join(os.path.dirname(__file__), "..", "goldenCursor", "mousePositions")
	oldPositions = os.path.join(os.path.dirname(__file__), "..", "goldenCursor", "globalPlugins", "files")
	# Without importing old positions, saved positions would be lost.
	newPositions = os.path.join(os.path.dirname(__file__), "mousePositions")
	# First, migrate second generation positions database.
	if os.path.exists(positions):
		try:
			shutil.copytree(positions, newPositions)
		except (IOError, WindowsError):
			pass
	if os.path.exists(oldPositions):
		# Manually migrate first generation database to the new format.
		import codecs, configobj
		os.mkdir(newPositions)
		for gcFile in os.listdir(oldPositions):
			path = os.path.join(oldPositions, gcFile)
			newPositionDatabase = configobj.ConfigObj(os.path.join(newPositions, gcFile), encoding="UTF-8")
			with codecs.open(path, "r", "utf-8") as f:
				data = f.read().strip()
			data = data.split("\n")
			for i in data:
				if i[0] == "[":
					newPositionDatabase[i[1:-1]] = data[data.index(i)+1]
			newPositionDatabase.write()
