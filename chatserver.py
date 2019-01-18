#!usr/bin/env python

import socket
import time
from thread import *
ip="127.0.0.1"  
port=9032  #port > 6000 are 
#calling UDP protocol
#if no arguements passed to socket() then by default it becomes TCP

#socket.SOCK_DGRAM  ---> UDP   socket.AF_INET----> ipv4
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#bindng ip and port
s.bind((ip,port))  #providing a way to connect

clients=[]
s.listen(100)

def c_thread(connect,addr):
	while True:
		message=connect.recv(1024)
		print(addr[0],"=>",message)
		messgae_to_send=addr[0]+"=>"+message
		broadcast(message_to_send,connect)
def broadcast(message,connection):
		mess=time.ctime(time.time())+message+addr[0]
		for client in clients:
			if client != connection:
				client.send(message)

while True:
	connect,addr=s.accept()
	if connect not in clients:	
		clients.append(connect)
	new_thread(c_thread(connect,addr))

	


    
