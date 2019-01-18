#!usr/bin/env python

import socket
import thread

ip="127.0.0.1"  #receivers ip
port=9055  #port > 6000 are 
#calling UDP protocol
#if no arguements passed to socket() then by default it becomes TCP

#socket.SOCK_DGRAM  ---> UDP   socket.AF_INET----> ipv4
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#sending message to target
s.bind((ip,port))
clients=[]
def sending():
	while True:
		accpt=raw_input()
		s.sendto("Otheruser:"+accpt,(ip,9056))
def recving():
	while True:
		data=s.recvfrom(1024)
		print(data[0])
try:
	thread.start_new_thread(sending,())
	thread.start_new_thread(recving,())
except:
	print("BUg")
while True:
	pass



