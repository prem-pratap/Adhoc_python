#!usr/bin/env python2
import webbrowser

data=raw_input("Type to search on gooogle:")
webbrowser.open_new_tab('https://www.google.com/search?q='+data)
execfile('menu.py')
