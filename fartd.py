#!/usr/bin/env python3

import time
import socket
import sys
import subprocess
from pathlib import Path


def main():
    HOST = '0.0.0.0'
    PORT = 3124
    SOUND_PATH = Path.home() / ".fartd" / "fart.wav"
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((HOST, PORT))

    server_socket.listen(5)

    print(f"fartd Listening: {PORT}")



    print("fartd started", flush=True)
    while True:
        try:
            client_socket, client_address = server_socket.accept()
            print(f"Contact! FIRE!")
            
            subprocess.run(["paplay", SOUND_PATH])

            client_socket.close()


        except KeyboardInterrupt:
            print("daemon done")
            break




if __name__ == "__main__":
    main()
