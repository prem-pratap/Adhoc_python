#!/usr/bin/env python3

import  urllib.request as urllib2
#urllib or urllib2 in python2
from googlesearch import search
# now put a keyword
webdata=search('hello',num=3,tld="co.in")
#webdata=search('hello',num=3,stop=2,pause=1)
#  generator type  iterable 
print(type(webdata))
for  i  in   webdata:
	print(i)
	link=urllib2.urlopen(i)
print(link.read())
