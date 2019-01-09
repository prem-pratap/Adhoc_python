#!usr/bin/env python2
import commands
ram=commands.getoutput('free -m')       #type of it would be string therefore convert it into list
final_memory=ram.split()[7]
print "My ram is ",final_memory,"MB"
cpu=commands.getoutput('lscpu | grep -i model | tail -1')
print('processing..............')
pro='''
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@                                    @@
@@                                    @@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''
print pro
print "CPU information is "+cpu
execfile('menu.py')
