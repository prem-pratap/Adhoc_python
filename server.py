#!usr/bin/env python

import socket
import os
import time
recv_ip="127.0.0.1"  
recv_port=9032  #port > 6000 are 
#calling UDP protocol
#if no arguements passed to socket() then by default it becomes TCP

#socket.SOCK_DGRAM  ---> UDP   socket.AF_INET----> ipv4
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#bindng ip and port
s.bind((recv_ip,recv_port))  #providing a way to connect
clients=[]

while(True):
        data=s.recvfrom(100)  # 100 is buffer size in char i.e maximum characters to be received
        check=(os.system(data[0]))
	if data[1] not in clients :
		clients.append(data[1])
	for client in clients:
		s.sendto(data[0],client)
	
        if (check==0):
            print (time.ctime(time.time()),data[1],data[0])
            s.sendto("Successfully run "+data[0],data[1])
        else:
            s.sendto(data[0]+"Not found "+data[1],data[1])
    

