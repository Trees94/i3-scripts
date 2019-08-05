#!/bin/bash

dbus-monitor --session "type=signal,interface=org.gnome.ScreenSaver,member=ActiveChanged" \
| while read line; do 
  if [ x"$(echo "$line" | grep 'boolean false')" != x ] ; then 
	  $HOME/bin/startWorkOn $($HOME/programs/i3-scripts/currentWorkspace.py); 
  fi; 
  done
