#!usr/bin/env python

import socket
recv_ip="127.0.0.1"  #receivers ip
recv_port=9010  #port > 6000 are 
#calling UDP protocol
#if no arguements passed to socket() then by default it becomes TCP

#socket.SOCK_DGRAM  ---> UDP   socket.AF_INET----> ipv4
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#sending message to target

while True:
	accept=raw_input("Type command:")
    #it will send data and create its own socket(own ip and any random port)
	s.sendto(accept,(recv_ip,recv_port))  
    	print (s.recvfrom(20))




