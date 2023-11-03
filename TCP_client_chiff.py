#https://www.geeksforgeeks.org/file-transfer-using-tcp-socket-in-python/?ref=gcse
import socket
import sys
import subprocess as sp
# Creating Client Socket 
if __name__ == '__main__': 
	host = sys.argv[1]
	port = 8080

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# Connecting with Server 
	sock.connect((host, port))

	while True: 

		filename = sys.argv[2]
		try: 
		# Reading file and sending data to server 
			fi = open(filename, "rb") 
			cmd = "./aes " + filename + " c 1 0"
			sp.run(cmd, shell=True)

			data = fi.read() 
			if not data: 
				break
			while data: 
				sock.send(data) 
				data = fi.read() 
			# File is closed after data is sent 
			fi.close()
			cmd = "./aes " + filename + " d 1 0"
			sp.run(cmd, shell=True)
			break 

		except IOError: 
			print('You entered an invalid filename!\nPlease enter a valid name') 
