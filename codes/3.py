# Code 3.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socked created!")

host = 'www.google.com'
port = 81

remote_ip = socket.gethostbyname(host)

print("IP Address of " + host + " is " + remote_ip)

s.connect((remote_ip, port))

print("Socket connected to " + host + " on ip " + remote_ip)
