#!usr/bin/env python

import socket
ip="127.0.0.1"  #receivers ip
port=9090  #port > 6000 are 
#calling UDP protocol
#if no arguements passed to socket() then by default it becomes TCP

#socket.SOCK_DGRAM  ---> UDP   socket.AF_INET----> ipv4
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#sending message to target

while True:
	accept=raw_input()
	s.sendto(accept,(ip,port))      



