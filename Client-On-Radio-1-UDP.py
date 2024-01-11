# client.py
import socket
from time import sleep

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 9000
server_address = ('10.223.75.168', port) 

try:
    while True:
        message = 'Hello World'
        print(f"Sending: {message}")
        sent = sock.sendto(message.encode(), server_address)
        sleep(1)
        
finally:
    print("Closing socket")
    sock.close()