#!/usr/bin/python3
import subprocess
import sys

if __name__=="__main__":
    proc = subprocess.Popen(['zenity', '--entry', '--title=I3', "--text=" + sys.argv[1]], stdout=subprocess.PIPE)

    projectName = proc.stdout.read()

    projectName = projectName.decode().replace('\n', '').replace('\r', '')

    print(projectName)
