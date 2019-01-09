#!usr/bin/env python

import socket
ip="127.0.0.1"  
port=9090  #port > 6000 are 
#calling UDP protocol
#if no arguements passed to socket() then by default it becomes TCP

#socket.SOCK_DGRAM  ---> UDP   socket.AF_INET----> ipv4
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#bindng ip and port
s.bind((ip,port))  #providing a way to connect

while(True):
	print  s.recvfrom(100)  # 100 is buffer size in char i.e maximum characters to be received
