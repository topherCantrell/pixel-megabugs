"""
This chain is mapped as a 64*2 x 32 grid.
"""
import time
import sys
import os
import json

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from rgbmatrix import graphics

options = RGBMatrixOptions()
        
options.hardware_mapping = 'regular'
options.rows = 32 # 32 rows per display
options.cols = 64 # 64 rows per display (64x32)
options.chain_length = 2 # 2 displays per chain (128x32)
options.parallel = 3 # 3 (128x96)
options.disable_hardware_pulsing = False
options.pwm_bits = 11
options.gpio_slowdown = 5
options.pwm_lsb_nanoseconds = 50

                
matrix = RGBMatrix(options = options)  

COLORS = [[0,0,0],[250,0,0],[0,0,250],[250,250,250]]

def get_frame_snapshot(screen):
    with open('frame.txt') as f:
        data = json.loads(f.read())
        
    for i in range(len(data)):
        if data[i]<0:
            data[i] += 256
            
    start = screen*0x0C00+0x0400
            
    # Get the COCO data
    frame = data[start:start+0x0C00]
    
    # Decode the 4-pixels-per-byte structure
    ret = []
    for d in frame:
        ret.append((d>>6)&3)
        ret.append((d>>4)&3)
        ret.append((d>>2)&3)
        ret.append(d&3)
        
    return ret

def draw_frame(pixels,colors,canvas):
    for y in range(96):
        for x in range(128):
            co = colors[pixels[y*128+x]]
            canvas.SetPixel(x,y,co[0],co[1],co[2])


canvas = matrix.CreateFrameCanvas()
pixels = get_frame_snapshot(2)
draw_frame(pixels,COLORS,canvas)    
matrix.SwapOnVSync(canvas)

while True:
    time.sleep(1)
