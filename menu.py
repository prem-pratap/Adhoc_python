#usr/bin/env python2
#menu based programming

import webbrowser
import commands 

options='''
press 1 to check your os version:
press 2 to login your facebook account:
press 3 to check RAM and CPU in your current machine:
press 4 to search something in google search engine:
press 5 to lsit out all IP and mac address in your current network zone:
'''

#lscpu command used to check cpu and free -m to check ram
#import commands to communicate with os through python
print options
# to take input
choice=raw_input()
if int(choice)== 1:
        print "My OS"
elif int(choice)==4:
        data=raw_input("Type to search on gooogle:")
        webbrowser.open_new_tab('https://www.google.com/search?q='+data)
elif int(choice)==3:
        execfile('raminfo.py')
	
else:
	print "Invalid choice"
