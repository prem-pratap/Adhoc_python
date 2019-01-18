#!usr/bin/env python

import socket
ip="127.0.0.1"  #receivers ip
port=9032  #port > 6000 are 
#calling UDP protocol
#if no arguements passed to socket() then by default it becomes TCP

#socket.SOCK_DGRAM  ---> UDP   socket.AF_INET----> ipv4
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#sending message to target

clients=[]
while True:
	accpt=raw_input("Type message:")
	data,addr=s.recvfrom(100)
    #it will send data and create its own socket(own ip and any random port)
	for client in clients:
		s.send(data+accpt,client)
		s.sendt(accept,(ip,port))  
    	



