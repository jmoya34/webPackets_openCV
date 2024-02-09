#!/usr/bin/env python

# Single script version of the client
"""
import asyncio
import time
from websockets.sync.client import connect

def hello():
    try:
        with connect("ws://localhost:8765") as websocket:
            websocket.send("Hello world!")
            message = websocket.recv()
            print(f"Received: {message}")
    except ConnectionRefusedError:
        print("No connection made to server")
        time.sleep(3) 

while(1):
    hello()
"""

# class version of the client
import asyncio
import time
from websockets.sync.client import connect

class Client:
    def __init__(self):
        self.websocket = None
        self.connection_status = False

    def hello(self):
        try:
            self.websocket = connect("ws://localhost:8765")
            self.connection_status = True
            self.websocket.send("Status: Connection made to server (ping ponged)")
            message = self.websocket.recv()
            print(f"Received: {message}")
        except ConnectionRefusedError:
            self.connection_status = False
            print("No connection made to server")
            time.sleep(3) 
        # except ConnectionAbortedError:
        #     print("Connection distrupted by server")
        #     time.sleep(3)
        except TimeoutError:
            self.connection_status = False
            print("Timeout error")
            time.sleep(3)
        except ConnectionError:
            self.connection_status = False
            print("Connection error")
            time.sleep(3)

    def send_msg(self, message):
        self.websocket.send(message)

    def recieve_msg(self):
        message = self.websocket.recv()
        print(f"Received: {message}")

    def start(self):
        print("Client started")
        while(self.connection_status == False):
            self.hello()
    
    def stop(self):
        self.websocket.close()
        print("Connection closed")