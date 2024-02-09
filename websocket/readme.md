# Connecting from client
As default from documentation when the server isn't up the application will just crash and choose not to continue checking if a connection can be re-established. Therefore modify the code to always check within a time interval if there is server attempting to connect

# Issue I ran into
Due to my lack of knowledge of how sockets worked, I was constantly adding clients to connect to the server and ultimately connecting a bunch of pages. This would crash the server and would leave me unsure where went wrong. The while loop I had implemented inside the client_class.py file was the source of the issues and for future use it should be refrained from using .start() in a while loop to prevent the server from crashing.