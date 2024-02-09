from client_class import Client

client = Client()
client.start()

try:
    while(1):
        client.send_msg("Hello world!")
        client.recieve_msg()
except KeyboardInterrupt:
    print("Connection made to server and terminating client")
    client.stop()

# print("Connection made to server and terminating client")
# client.stop()   # without this line, the client will keep running and trying to connect to the server
