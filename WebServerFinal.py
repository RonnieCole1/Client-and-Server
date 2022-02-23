#!/usr/bin/env python3
# Project 2 - TCP Web Server Lab
 
# import socket module
from socket import *
import sys # In order to terminate the program
import argparse # For command line parsing

# Create TCP socket                                                                         
serverSocket = socket(AF_INET, SOCK_STREAM)                                                 

# Prepare a server socket                                                                   
serverPort = 6789
serverSocket.bind(('', serverPort)) # bind the socket to the address and port
serverSocket.listen(1) # listen for one connection

while True:

    # Establish the connection
    print('Ready to serve CSCI340 Students...')

    # listen for requests that are coming in from the client connection
    connectionSocket, addr = serverSocket.accept()
    
    try:

        # receive requests that are coming in up to 4096 bytes of data
        message = connectionSocket.recv(4096)
        print(message.decode()) # print out the request
        filename = message.split()[1] # split our message into 2 parts. 1 consisting of our "\" and the other consisting of our object
        f = open(filename[1:]) # opens our object and stores it in f

        outputdata = f.read() # reads our object and stores it in outputdata

        # Send one HTTP header line into socket for a 200 OK message
        connectionSocket.send('\nHTTP/1.1 200 OK\nContent-Type: html\n\n'.encode())

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        # close the connection now that we're done, so we don't use all resources
        connectionSocket.close()

    except IOError:

        # Send HTTP response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())

        # Close the client connection socket
        connectionSocket.close()

serverSocket.close()
sys.exit() # Terminate the program after sending the corresponding data
