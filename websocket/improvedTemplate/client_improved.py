#!/usr/bin/env python

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