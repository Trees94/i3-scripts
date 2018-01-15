#!/usr/bin/python3
# -*- coding: utf-8 -*-
# encoding: utf-8
import subprocess
import sys
import i3
import newProjectWorkspaces

focussed_workspace = next(filter(lambda x: x['focused'], i3.get_workspaces()))
ws_name = "-".join(focussed_workspace['name'].split("-")[:-1])
print(ws_name)

