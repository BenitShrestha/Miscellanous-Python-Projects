# Client Side
import socket

client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect("e0:d4:e8:00:9d:cf", 4) 
