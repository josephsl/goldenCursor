# Golden Cursor installation tasks
# Copyright 2016-2021 Joseph Lee and others, released under GPL.

# Provides needed routines during add-on installation and removal.
# Routines are partly based on other add-ons,
# particularly Place Markers by Noelia Martinez (thanks add-on authors).
# File copying operation comes from StationPlaylist Studio add-on by Joseph Lee.

import os
import shutil


def onInstall():
	positions = os.path.join(os.path.dirname(__file__), "..", "goldenCursor", "mousePositions")
	# Without importing old positions, saved positions would be lost.
	newPositions = os.path.join(os.path.dirname(__file__), "mousePositions")
	# Migrate positions database.
	if os.path.exists(positions):
		try:
			shutil.copytree(positions, newPositions)
		except (IOError, WindowsError):
			pass
