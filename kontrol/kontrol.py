#!/usr/bin/python

import socket

IP = "192.168.100.116"
Port = 9669

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind(("", 0))

#s.connect(("www.google.com", 80))
#s.send(str.encode("GET / HTTP/1.0\n\n"))
#print(s.recv(8192))

#s.connect((IP, Port))

alive = 1
while alive:
	msg = input("Enter text: ")
	if msg == "die":
		alive = 0
	else:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((IP, Port))
		s.send(str.encode(msg))
		s.shutdown(socket.SHUT_RDWR)
		s.close()
#s.close()