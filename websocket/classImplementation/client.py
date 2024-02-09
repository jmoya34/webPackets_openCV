from client_class import Client

client = Client()
client.start()

print("Connection made to server and terminating client")
client.stop()   # without this line, the client will keep running and trying to connect to the server
