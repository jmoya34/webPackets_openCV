#!/usr/bin/env python

# class version of the server
import asyncio
from websockets.server import serve

class Server:
    def __init__(self):
        self.server = None

    async def echo(self, websocket):
        async for message in websocket:
            await websocket.send(message)

    async def main(self):
        async with serve(self.echo, "localhost", 8765):
            await asyncio.Future()  # run forever

    def start(self):
        asyncio.run(self.main())

    # This function does not work but creating an implemntation of it is a good idea
    def stop(self):
        self.server.stop()