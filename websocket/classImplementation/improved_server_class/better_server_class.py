#!/usr/bin/env python

# class version of the server
import asyncio
from websockets.server import serve

class Server:
    def __init__(self):
        self.server = None
        self.flag = asyncio.Event()

    async def echo(self, websocket):
        async for message in websocket:
            await websocket.send(message)

    async def main(self, event):
        async with serve(self.echo, "localhost", 8765):
            print("Server running")
            await event.wait()  # run forever

    async def buffer(self):
        task = asyncio.create_task(self.main(self.flag))
        await task

    def start(self):
        asyncio.run(self.buffer())

    # This function does not work but creating an implemntation of it is a good idea
    def stop(self):
        self.flag.set()
        print("Server stopped")