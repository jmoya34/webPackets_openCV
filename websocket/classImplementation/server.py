from server_class import Server

# Start Server
try: 
    server = Server()
    server.start()
except KeyboardInterrupt:
    server.stop()