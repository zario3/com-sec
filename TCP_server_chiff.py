#https://www.geeksforgeeks.org/file-transfer-using-tcp-socket-in-python/?ref=gcseimport socket 
import subprocess as sp
import socket
import sys

if __name__ == '__main__': 
	# Defining Socket 
	host = sys.argv[1]
	port = 8080

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	sock.bind((host, port)) 
	sock.listen(1) 
	# Establishing Connections 
	connections = [] 
	print('Initiating clients') 
	conn = sock.accept() 
	print('Connected with client') 


	# Receiving File Data 
	data = conn[0].recv(1024)

	if not data: 
		exit()
	# Creating a new file at server end and writing the data 
	filename = 'output'
	fo = open(filename, "wb") 
	while data: 
		if not data: 
			break
		else: 
			fo.write(data) 
			data = conn[0].recv(1024).decode('utf_16', 'strict') 

	print() 
	print('Receiving file from client') 
	print() 
	print('Received successfully! New filename is:', filename) 
	fo.close() 

	sp.run("./aes output d 1 0", shell=True)

	# Closing all Connections 
	conn[0].close() 
