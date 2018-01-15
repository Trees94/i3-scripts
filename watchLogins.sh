#!/bin/bash

dbus-monitor --session "type=signal,interface=org.gnome.ScreenSaver,member=ActiveChanged" \
| while read line; do 
  if [ x"$(echo "$line" | grep 'boolean false')" != x ] ; then 
	  $HOME/bin/startWorkOn $(/home/local/ANT/tomrees/code/i3-scripts/currentWorkspace.py); 
  fi; 
  done
