# Code 2.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socked created!")

host = 'www.elixirdose.com'

remote_ip = socket.gethostbyname(host)

print("IP Address of " + host + " is " + remote_ip)
