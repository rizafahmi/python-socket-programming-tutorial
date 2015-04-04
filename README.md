# Socket Programming In Python

## Introduction

Sockets are fundamentals. It's behind any kind of network communication done by the computers. It's the backbone behind world wide web. For example when you type "www.google.com" in your web browser, it will open a socket and connect to google.com to get a web page and show it to you in HTML format. Similar to chat client like google hangout, yahoo messenger or skype.

To begin our journey to the socket world, we will do programming tcp socket in python. To start, let's begin with creating a socket

## Create a Socket

To create a socket, we can use python's [socket](https://docs.python.org/2/library/socket.html). Now let's create one:

    # Code 1.py
    import socket

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("Socked created!")

The code was straight forward. We first import `socket` library. Then we create a socket using `socket.socket` function. We passed `AF_INET` as IPv4 as the address family like '100.50.200.5' and `SOCK_STREAM` means we used TCP protocol.

## Connect To The Server

After creating a socket, we now able to connect to the server via a certain port number. We need an IP address and port number to connect to. We will use port 80 which is http default port and ip address of google.com as an example.

### Get IP Address From The Host

It's simple. We can use `gethostbyname` function to get IP address from hostname.

# Code 2.py
    import socket

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("Socked created!")

    host = 'www.google.com'

    remote_ip = socket.gethostbyname(host)

    print("IP Address of " + host + " is " + remote_ip)

### Connect Into IP Address and Port

Then we add port and do connect through the socket we've created earlier.

    # Code 3.py
    import socket

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("Socked created!")

    host = 'www.google.com'
    port = 80

    remote_ip = socket.gethostbyname(host)

    print("IP Address of " + host + " is " + remote_ip)

    s.connect((remote_ip, port))

    print("Socket connected to " + host + " on ip " + remote_ip)


Now run the program by executing `3.py` file.

    $> python 3.py
    Socked created!
    IP Address of www.google.com is 173.194.126.49
    Socket connected to www.google.com on ip 173.194.126.49



Let's be a little bit adventurous by changing the port. For example just change to port 81 and let's see the result by execute the file once again.

    $ python 3.py 
    Socked created!
    IP Address of www.google.com is 128.199.209.228
    Traceback (most recent call last):
      File "3.py", line 15, in <module>
        s.connect((remote_ip, port))
    ConnectionRefusedError: [Errno 111] Connection refused

As you can see, the connection was refused because port 81 most likely not opened.

Ok, now let's back to the track by moving our topic forward.

### Send Data

`sendall` function will simply send all data. Let's send some data to google.com


    # Code 4.py
    import socket

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("Socked created!")

    host = 'www.google.com'
    port = 80

    remote_ip = socket.gethostbyname(host)

    print("IP Address of " + host + " is " + remote_ip)

    s.connect((remote_ip, port))

    print("Socket connected to " + host + " on ip " + remote_ip)

    message = "GET / HTTP/1.1\r\n\r\n"
    s.sendall(message)

The code above simply send the string message "GET / HTTP/1.1\r\n\r\n" to google.com. This message is actually an "http command" to get the mainpage of a website. We can't see anything return yet, we need to implement receiving data first.

### Receive Data

We can receive data from the server we contacted before using `recv` function. Below are example on how to receive data after we sent one.


    # Code 5.py
    import socket

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("Socked created!")

    host = 'www.google.com'
    port = 80

    remote_ip = socket.gethostbyname(host)

    print("IP Address of " + host + " is " + remote_ip)

    s.connect((remote_ip, port))

    print("Socket connected to " + host + " on ip " + remote_ip)

    message = b"GET / HTTP/1.1\r\n\r\n"
    s.sendall(message)

    reply = s.recv(4096)

    print(reply)

The code now will return the content of the page that we requested before.
Last thing to do is to close the socket.

### Close Socket

Easy enough, we should use `close` function provided by `socket` package.

    # Code 6
    s.close()

And that's it folks.

## Conclusion

In this article learned how to:

1. Create a socket
2. Connect to the server
3. Send some data
4. Receive a reply from the server

What we did above represents a client side. And we use google.com
as the server side. Web server provided by google is one example
of server which use port 80. The web server duty is to receipt
the request and return it with respective reply in form of HTML page.
