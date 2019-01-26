"""
This chain is mapped as a 64*2 x 32 grid.
"""
import time
import sys
import os

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from rgbmatrix import graphics

options = RGBMatrixOptions()
        
options.rows = 32
options.cols = 64
options.chain_length = 2
options.parallel = 1
options.row_address_type = 0
options.multiplexing = 0
options.pwm_bits = 11
options.brightness = 100
options.pwm_lsb_nanoseconds = 130
options.led_rgb_sequence = 'RGB'
options.pixel_mapper_config = ''
                
matrix = RGBMatrix(options = options)
  
                
while True:       
    
    X0 = 128-10-2
    Y0 = 10
    
    offscreen_canvas = matrix.CreateFrameCanvas()    
    
    for y in range(10):
        for x in range(10):    
            offscreen_canvas.SetPixel(X0+x,Y0+y,100,255,255)
    
    matrix.SwapOnVSync(offscreen_canvas)
    time.sleep(1) 
    
