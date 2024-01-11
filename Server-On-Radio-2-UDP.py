# server.py
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# get local machine name
host = socket.gethostname()
print(f"I am {host}")

port = 9000

server_address = ('', port)
sock.bind(server_address)

print(f"Listening for messages from 'radio-1' on {port}...")

while True:
    data, address = sock.recvfrom(4096)

    if data:
        print(f"Received message: {data.decode()} from {address}")