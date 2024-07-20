# Socket bound to IP/MAC Address
# Server listens to incoming connections, accept connections, handle incoming connections

import socket 

# Use socket.AI_INET for TCP
server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM) # RF COMM Protocol

# Bind to MAC Address
server.bind("e0:d4:e8:00:9d:cf", 4) # Bluetooth MAC Address, Specify a channel (20 Channels)
server.listen(1) # Listen to 1 connection at a time

# Client here is our client
client, address = server.accept() # Accept incoming connection