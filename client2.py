import socket
import os

s = socket.socket()
ip = input(str("Please enter the host address of the server: "))
port = 8000
s.connect((ip,port))
print("Connected ...")

filename = input(str("Please enter a filename for the incoming file: "))
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
print("File has been received succesfully.")

s.close()
