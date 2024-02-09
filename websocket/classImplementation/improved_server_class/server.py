from better_server_class import Server
import asyncio
# Start Server
server = Server()
try: 
    server.start()
except KeyboardInterrupt:
    server.stop()
