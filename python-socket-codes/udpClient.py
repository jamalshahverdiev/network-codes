import socket

def Main():
	host = '172.16.100.20'
	port = 5001

	server = ('172.16.100.10', 5100)	

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))

	message = raw_input("-> ")
	while message != 'q':
		s.sendto(message, server)
		data, addr = s.recvfrom(1024)
		print('Recieved from server: ' + str(data))
		message = raw_input("-> ")
	s.close()

if __name__ == '__main__':
	Main() 
