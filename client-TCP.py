# client.py
import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()

# Port for your service
port = 9000

# Connection to hostname on the port
client_socket.connect((host, port))

# Send a message
client_socket.send("Hello World".encode('utf-8'))

# Close the socket
client_socket.close()