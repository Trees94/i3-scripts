#!/usr/bin/python3
# -*- coding: utf-8 -*-
# encoding: utf-8
import subprocess
import sys
import i3
import newProjectWorkspaces
import constants

subprocess.Popen(['xterm', '-e', constants.SCRIPT_DIR + 'listProjectWorkspaces.py | ' + constants.HOME_DIR + '.fzf/bin/fzf | xargs -0 ' + constants.SCRIPT_DIR + 'newProjectWorkspaces.py'])

names = list(set(map(lambda x: x['name'].split("-")[0], i3.get_workspaces())))
for name in names:
  print(name)

