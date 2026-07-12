#!/usr/bin/env python3

import os

print("target > change ip target")
print("fart > call fart on target")
print("msg > send message to target")

target = "0.0.0.0"

def targetchg():
    global target
    target = input("ip: ")
    print(f"target: {target}")
    




def fart():
    wav_sound = "fart.wav"

    print(f"Farted on {target}")
    path = input("Sound path in .wav(n = default): ")
    if(path == "n"):
        print("default")      
        
        
    else:
        wav_sound = path
        if not os.path.exists(wav_sound):
            print("Does not exists.")
            return
    
    os.system(f'ncat {target} 3124 < {wav_sound}')
    print("sended")

    

def msg():
    message = input("Message: ")
    os.system(f'echo "{message}" | ncat {target} 3125')
    print(f"Message: {message} | Was sent to {target}")
    



def shell():
    while True:

        inp = input(">")

        if inp == "target":
            targetchg()
        elif inp == "fart":
            fart()
        elif inp == "msg":
            msg()

shell()
    
