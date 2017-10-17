#!/usr/bin/python3
# -*- coding: utf-8 -*-
# encoding: utf-8
import subprocess
import sys
import i3


def main(projectName):
    print(projectName)
    if (projectName is None) or (len(projectName) == 0):
      sys.exit(0)
    
    new_workspaces = []
    for output in i3.filter(tree=i3.get_outputs(), active=True):
        current_workspace_name = output['current_workspace']
        print(current_workspace_name)
        current_workspace = i3.filter(tree=i3.get_workspaces(), name=current_workspace_name)
    
        if not current_workspace[0]['focused']:
            print("Current workspace, {}, not focussed".format(current_workspace_name))
            i3.workspace(current_workspace_name)
    
        i3.workspace(projectName + '-' + output['name'])

    subprocess.call(['startWorkOn', projectName])
    
if __name__=="__main__":
    if (len(sys.argv) > 1):
        projectName = sys.argv[1]
        projectName = projectName.replace('\n', '').replace('\r', '')
    else:
        proc = subprocess.Popen(['zenity', '--entry', '--title=I3', 
          "--text=Start a new project with the name:"],
          stdout=subprocess.PIPE)
        
        projectName = proc.stdout.read()
        
        projectName = projectName.decode().replace('\n', '').replace('\r', '')

    main(projectName)

