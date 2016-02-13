import socket 

def Main():
	host = '172.16.100.10'
	port = 5100

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))

	print("Server started.")
	while True:
		data, addr = s.recvfrom(1024)
		print("message from: " + str(addr))
		print("from connect user: " + str(data))
		data = str(data).upper()
		print("sending: " + str(data))
		s.sendto(data, addr)
	s.close()

if __name__ == '__main__':
	Main()
