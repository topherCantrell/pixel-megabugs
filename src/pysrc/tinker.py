"""
This chain is mapped as a 64*2 x 32 grid.
"""
import time
import sys
import os

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from rgbmatrix import graphics

options = RGBMatrixOptions()
        
options.hardware_mapping = 'regular'
options.rows = 32 # 32 rows per display
options.cols = 64 # 64 rows per display (64x32)
options.chain_length = 2 # 2 displays per chain (128x32)
options.parallel = 3 # 3 (128x96)
options.disable_hardware_pulsing = False
options.pwm_bits = 1
options.gpio_slowdown = 5
options.pwm_lsb_nanoseconds = 50

                
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
 
def test():           
    offscreen_canvas = matrix.CreateFrameCanvas()  
    for x in range(90):
        offscreen_canvas.SetPixel(x+2,x+2,255,255,255)        
    matrix.SwapOnVSync(offscreen_canvas)
    
    while True:
        time.sleep(5)
    
                
pos_x = 0
pos_y = 40
while True:       
    
    offscreen_canvas = matrix.CreateFrameCanvas()       
    draw_graphic(pos_x,pos_y,bug1,1,offscreen_canvas)    
    matrix.SwapOnVSync(offscreen_canvas)
    time.sleep(0.1)
    pos_x += 1    
    
    offscreen_canvas = matrix.CreateFrameCanvas()       
    draw_graphic(pos_x,pos_y,bug2,1,offscreen_canvas)    
    matrix.SwapOnVSync(offscreen_canvas)
    time.sleep(0.1) 
    pos_x += 1
    
    if pos_x > 115:
        pos_x = 0    
