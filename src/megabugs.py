"""
This chain is mapped as a 64*2 x 32 grid.
"""
import time
import sys
import os

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from rgbmatrix import graphics

options = RGBMatrixOptions()
        
options.rows = 32 # 32 rows per display
options.cols = 64 # 64 rows per display (64x32)
options.chain_length = 2 # 2 displays per chain (128x32)
options.parallel = 1 # 3 (128x96)
                
matrix = RGBMatrix(options = options)  

bug1 = '''
       ..**********
       ..**********
       ..**..**..**
       ..**..**..**
       ****........
       ****........
       ****........
       ****........
       ..**..**..**
       ..**..**..**
       ..**********
       ..**********
       '''
       
bug2 = '''
       ..****......
       ..****......
       ..**********
       ..**********
       ****..**..**
       ****..**..**
       ****..**..**
       ****..**..**
       ..**********
       ..**********
       ..****......
       ..****......
       '''

def draw_graphic(x,y,data,color,canvas):
    data = data.replace(' ','').replace('\n','')    
    pos = 0 
    for j in range(12):
        for i in range(12):
            if data[pos]=='*':
                canvas.SetPixel(x+i,y+j,100,255,255) 
            pos+=1
    
                
while True:       
    
    offscreen_canvas = matrix.CreateFrameCanvas()       
    draw_graphic(56,10,bug1,1,offscreen_canvas)    
    matrix.SwapOnVSync(offscreen_canvas)
    time.sleep(0.25) 
    
    offscreen_canvas = matrix.CreateFrameCanvas()       
    draw_graphic(56,10,bug2,1,offscreen_canvas)    
    matrix.SwapOnVSync(offscreen_canvas)
    time.sleep(0.25) 
    
