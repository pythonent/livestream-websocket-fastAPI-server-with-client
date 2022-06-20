#!/usr/bin/env python
import asyncio
from tracemalloc import stop
#from tkinter import W
import cv2
from cv2 import AKAZE_DESCRIPTOR_KAZE
import numpy as np
#import sys
#import struct
import pickle
from fastapi import FastAPI, WebSocket
import threading
import websockets

app = FastAPI()
cap = cv2.VideoCapture(0)



#place_holder
def forward_():
    pass
def backward_():
    pass
def left_():
    pass
def right_():
    pass
def forward_left():
    pass
def forward_right():
    pass
def backward_left():
    pass
def backward_right():
    pass
def stop_():
    pass
def test_decision():
    pass



@app.websocket("/drive")
async def stream_handler(websocket:WebSocket):
    await websocket.accept()
    name = await websocket.receive_text()
    print("> {}".format(name))
    while True:
        #serializing the frame
        ret, frame= cap.read()
        data = pickle.dumps(frame)
        await websocket.send_bytes(data)
        command = await websocket.receive_text()
        #reading command
        if command == 'F':
            forward_()
        elif command == 'B':
            backward_()
        elif command == 'L':
            left_()
        elif command == 'R':
            right_()
        elif command == 'FL':
            forward_left()
        elif command == 'FR':
            forward_right()
        elif command == 'BL':
            backward_left()
        elif command == 'BR':
            backward_right()
        elif command == 'S':
            stop_()
        else:
            test_decision()
#for python 3.10 + use below syntax for shorter execution time

#match decision:
 #   case'F':
  #      return 'forward'
   # case _:
    #    return 'default'




    #name = await websocket.recv()
    #print("< {}".format(name))

    #greeting = "Hello {}!".format(name)
    #await websocket.send(greeting)
   #print("> {}".format(greeting))


#async def main():
 #   start_server = websockets.serve(handler, 'localhost', 8765)
  #  async with start_server:
   #     await asyncio.Future()

#asyncio.get_event_loop().run_until_complete(start_server)
#asyncio.get_event_loop().run_forever()
#asyncio.run(main())
