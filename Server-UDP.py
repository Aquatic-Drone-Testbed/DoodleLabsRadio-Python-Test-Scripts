# server.py
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# get local machine name
host = socket.gethostname()
print(host)


server_address = ('', 20000)
sock.bind(server_address)

print("Listening for messages on port 20000...")

while True:
    data, address = sock.recvfrom(4096)

    if data:
        print(f"Received message: {data.decode()} from {address}")