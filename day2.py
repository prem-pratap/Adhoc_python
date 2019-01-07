#!usr/bin/env python
#menu based programming

import webbrowser 

options='''
press 1 to check your os version:
press 2 to login your facebook account:
press 3 to check RAM and CPU in your current machine:
press 4 to search something in google search engine:
press 5 to lsit out all IP and mac address in your current network zone:
'''

print options
# to take input
choice=raw_input()
if int(choice)== 1:
	print "My OS "
elif int(choice)==4:
	data=raw_input("Type to search on gooogle:")
	webbrowser.open_new_tab('https://www.google.com/search?q='+data)
else:
	print "Invalid choice"
