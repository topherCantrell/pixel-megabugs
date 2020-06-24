"""
  - Add this line to /etc/rc.local (before the exit 0):
  -   /home/pi/ONBOOT.sh 2> /home/pi/ONBOOT.errors > /home/pi/ONBOOT.stdout &
  - Add the following ONBOOT.sh script to /home/pi and make it executable:
  
#!/bin/bash
cd /home/pi/megabugs
python3 app_frame_viewer.py  
"""

import time
import sys
import os

import socket

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from rgbmatrix import graphics

options = RGBMatrixOptions()
    
# This chain is mapped as a 64*2 x 32 grid.
    
options.rows = 32 # 32 rows per display
options.cols = 64 # 64 rows per display (64x32)
options.chain_length = 2 # 2 displays per chain (128x32)
options.parallel = 1 # 3 (128x96)
                
matrix = RGBMatrix(options = options)  


def draw_graphic(x,y,data,color,canvas):
    data = data.replace(' ','').replace('\n','')    
    pos = 0 
    for j in range(12):
        for i in range(12):
            if data[pos]=='*':
                canvas.SetPixel(x+i,y+j,100,255,255) 
            pos+=1
            
def draw_frame(colors,pixels):
    canvas = matrix.CreateFrameCanvas()   
    for y in range(32):
        for x in range(128):
            val = pixels[128*y+x]
            #print('##',val)
            pix = colors[val]
            canvas.SetPixel(x,y,pix[0],pix[1],pix[2])
    matrix.SwapOnVSync(canvas)

def main():
    ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    ss.bind(('',1234))
    ss.listen(1)
    
    print('Listening on',ss)
    
    while True:
        cs,_ = ss.accept()
        print('Got a connection from',cs)
        #try:            
        sz = cs.recv(1)        
        sz = sz[0] + 1
        print('Loading',sz,'colors')
        colors = []
        for _ in range(sz):
            pix = [cs.recv(1)[0],cs.recv(1)[0],cs.recv(1)[0]]
            colors.append(pix)
        print(colors)
        pixels = []
        for _ in range(32):
            for _ in range(128):
                pixels.append(cs.recv(1)[0])
                #print(len(pixels))
        draw_frame(colors,pixels)
        cs.close()
        print('done')
        #except:
            # Eating exceptions on purpose
        #    print('eating')
            

main()
        
colors = [[0,0,0],[100,100,100]]
pixels = [0]*128*32

for x in range(32):
    pixels[128*x+x] = 1
    
draw_frame(colors,pixels)       
    
while True:
    time.sleep(1)
    
                
while True:       
    
    offscreen_canvas = matrix.CreateFrameCanvas()       
    draw_graphic(56,10,bug1,1,offscreen_canvas)    
    matrix.SwapOnVSync(offscreen_canvas)
    time.sleep(0.25) 
    
    offscreen_canvas = matrix.CreateFrameCanvas()       
    draw_graphic(56,10,bug2,1,offscreen_canvas)    
    matrix.SwapOnVSync(offscreen_canvas)
    time.sleep(0.25) 
    
