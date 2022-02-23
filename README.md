# Client-and-Server
A project that contains a server and a client using socket programming.
WebServerFinal uses port 6789 by default.
Place HelloWorld.html and WebServerFinal.py in the same directory. Run WebServerFinal.py in Python3.
If the server is sucessfully running, you should see "Ready to serve CSCI340 Students ..." in your command prompt.
To connect to WebServerFinal, type http://"Server_Host":6789/HelloWorld.html. This will take your to your html page.
To give a 404 message, replace "HelloWorld.html" with a file not located in the project's directory.

For the ClientServer, run in python3.
You will be told to give an input to access the html file on the WebServer.
Input "server_host:server_port/file_name".
The server will print the html document in the command line.
Note that our html code will appear in the first lines of the returned code, which will loop infinitely. You may need to scroll up
to see the returned html file.
