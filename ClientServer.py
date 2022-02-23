#!/usr/bin/env python3
# Project 2 - TCP Web Server Lab
 
# import socket module
from socket import *
import sys # In order to terminate the program
import argparse # For command line parsing

message = input("Enter Server_Host:Server_Port/Filename here: ") # User inputs IP, Port, and file name

# seperates the User's input into IP, Port, and Filename and stores them into variables.
serverName = message[0:message.index(":")] # IP Address of the server
serverPort = int(message[message.index(":")+1:message.index("/")]) # Server port number
fileName = message[message.index("/"):len(message)] # File name requested

clientSocket = socket(AF_INET, SOCK_STREAM) # Create a TCP Socket
clientSocket.connect((serverName, serverPort)) # Establish a connection to serverName at serverPort
request = 'GET '+fileName+' HTTP/1.1\r\nHost: '+serverName+'\r\n\r\n' # Create GET request
clientSocket.send(request.encode()) # Send a GET request to server

while True:
	modifiedRequest = clientSocket.recv(4096) # Recieve OK message with html object.
	print(modifiedRequest.decode())


# print("From Server:", modifiedRequest.decode()) # Print html object.

clientSocket.close()