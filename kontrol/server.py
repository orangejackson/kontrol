#!/usr/bin/env python3

import socket

IP = "127.0.0.1"
Port = 9669

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", Port))

#s.connect(("www.google.com", 80))
#s.send(str.encode("GET / HTTP/1.0\n\n"))
#print(s.recv(8192))

s.listen(0)
print("Listening")

alive = 1
while alive:
	(cli_sock, cli_addr) = s.accept()
	#cli_sock.send("Jerk from %s" % cli_addr)
	msgin = cli_sock.recv(8192).decode('utf-8')
	print("%s:%d says: '%s'" % (cli_addr[0], cli_addr[1], msgin))
	cli_sock.shutdown(socket.SHUT_RDWR)
	cli_sock.close()
	if msgin == "kill":
		alive = 0

s.shutdown(socket.SHUT_RDWR)
s.close()