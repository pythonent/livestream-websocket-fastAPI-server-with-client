#!/usr/bin/env python
import asyncio
#from tkinter import Frame
import websockets
import pickle
#import struct
import cv2
import numpy as np
#import sys
import threading




async def handler():
    async with websockets.connect('ws://localhost:8000/drive') as websocket:
        name = input("What's your name? ")
        await websocket.send(name)
        print("> {}".format(name))
        while True:
            frame_data = await websocket.recv()
            frame = pickle.loads(frame_data)
            t1=threading.Thread(cv2.imshow('vision', frame))
            #cv2.waitKey(1)
            #insert automised image recognition for decision making here
            command=input("what is your next command")
            await websocket.send(command)
            

        #name = input("What's your name? ")
        #await websocket.send(name)
        #print("> {}".format(name))

        #greeting = await websocket.recv()
        #print("< {}".format(greeting))

#asyncio.get_event_loop().run_until_complete(handler())

asyncio.run(handler())