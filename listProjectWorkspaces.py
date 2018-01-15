#!/usr/bin/python3
# -*- coding: utf-8 -*-
# encoding: utf-8
import subprocess
import sys
import i3

names = list(set(map(lambda x: "-".join(x['name'].split("-")[:-1]), i3.get_workspaces())))
for name in names:
  print(name)

