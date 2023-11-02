#https://www.geeksforgeeks.org/file-transfer-using-tcp-socket-in-python/?ref=gcse
import socket
import sys
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
			fi = open(filename, "r") 
			data = fi.read() 
			if not data: 
				break
			while data: 
				sock.send(str(data).encode()) 
				data = fi.read() 
			# File is closed after data is sent 
			fi.close()
			break 

		except IOError: 
			print('You entered an invalid filename!\nPlease enter a valid name') 
