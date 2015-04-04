# Socket Programming In Python

## Introduction

Sockets are fundamentals. It's behind any kind of network communication done by the computers. It's the backbone behind world wide web. For example when you type "www.google.com" in your web browser, it will open a socket and connect to google.com to get a web page and show it to you in HTML format. Similar to chat client like google hangout, yahoo messenger or skype.

To begin our journey to the socket world, we will do programming tcp socket in python. To start, let's begin with creating a socket

## Create a Socket

To create a socket, we can use python's [socket](https://docs.python.org/2/library/socket.html). Now let's create one:

    import socket

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print "Socked created!"

The code was straight forward. We first import `socket` library. Then we create a socket using `socket.socket` function. We passed `AF_INET` as IPv4 as the address family like '100.50.200.5' and `SOCK_STREAM` means we used TCP protocol.

## Connect To The Server

After creating a socket, we now able to connect to the server via a certain port number
