#!usr/bin/env python
import time
import os
x=raw_input("Enter a number:")
sum=int(x)+ 100
print("After adding 100 to it")
print("processinng........")
os.system("echo processing | festival --tts")
time.sleep(3)
voice_output="echo   Your output is " + str(sum) + " | festival --tts"
os.system(voice_output)
print(sum)
