#Houdini Task Profiler
#Author :   Timucin OZGER
#Date   :   19.05.2018
#This little code executes a node in Houdini and 
#outputs a report and a graph for  system Usage

import os
import subprocess

pid = str(os.getpid()) #get the pid for this task
cmd = "psrecord " + pid + " --log activity.txt --interval 5 --plot plot.png " #builds the string to run

p = subprocess.Popen(cmd,shell=True) #launches subprocess

#opens file and runs the node
hou.hipFile.load("/home/tricecold/Work/Masters_of_the_Sea/Prep_07.hiplc") 
cacheFlip = hou.node('/out/Cache_Sea_FLIP')
cacheFlip.render(verbose=True)

