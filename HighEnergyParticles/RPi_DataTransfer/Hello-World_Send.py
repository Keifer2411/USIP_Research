import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
recievingIP = "127.0.0.1"
recievingPort = 5005



message = "Hello World"
sock.sendto(message,(recievingIP, recievingPort)) 
print ("Sent")
