#!/usr/bin/env python3
import os
import sys
import pathlib
filename=sys.argv[1]
path='.'
files=os.listdir(path)
x=pathlib.Path(filename)
os.system("echo processing | festival --tts")
print("processing........")
if x.exists():
	voice_output="echo  File already exists  | festival --tts"
	os.system(voice_output)
	print("File already exists.")
else:
	ex='touch '+filename	
	os.system(ex)
	os.system("echo File created | festival --tts")
	print("File created")			




			
	

