#!/usr/bin/python3
# -*- coding: utf-8 -*-
# encoding: utf-8
import subprocess
import sys
import i3
import newProjectWorkspaces

subprocess.Popen(['xterm', '-e', 'i3-scripts/listProjectWorkspaces.py | /home/local/ANT/tomrees/.fzf/bin/fzf | xargs -0 i3-scripts/newProjectWorkspaces.py'])

names = list(set(map(lambda x: x['name'].split("-")[0], i3.get_workspaces())))
for name in names:
  print(name)

