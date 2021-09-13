import socket

RecievingIP = "127.0.0.1"
RecievingPort = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((RecievingIP, RecievingPort))

while True:
	data, addr = sock.recvfrom(1024) #buffer size is 1024 bytes
	print ("recieved message") 
