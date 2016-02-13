import socket
import threading
import time

tLock = threading.Lock()
shutdown = False

def receving(name, sock):
	while not shutdown:
		try:
			tLock.acquire()
			while True:
				data, addr = sock.recvfrom(1024)
				print(str(data))
		except:
			pass
		finally:
			tLock.release()

host = '172.16.100.20'
port = 0

server = ('172.16.100.10', 5000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

rT = threading.Thread(target=receving, args=("RecvThread", s))
rT.start()

alias = raw_input("Name: ")
message = raw_input(alias + "-> ")
while message != 'q':
	if message != '':
		s.sendto(alias + ": " + message, server)
	tLock.acquire()
	message = raw_input(alias + "-> ")
	tLock.release()
	time.sleep(0.2)

shutdown = True
rT.join()
s.close()
