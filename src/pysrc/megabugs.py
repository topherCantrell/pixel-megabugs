"""
3 chains of 2 panels. Each panel is 64x32:

 64 + 64 = 128
 64 + 64
 64 + 64
 -------
 96
 
"""
import time

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from rgbmatrix import graphics

from mega_maze import MegaMaze

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

MAZE = '''
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
| | | | | | | | | | | | | | | | | | | |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
| | | | | | | | | | | | | | | | | | | | 
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
| | | | | | | | | | | | | | | | | | | | 
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
| | | | | | | | | | | | | | | | | | | | 
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
| | | | | | | | | | | | | | | | | | | | 
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
| | | | | | | | | | | | | | | | | | | | 
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
| | | | | | | | | | | | | | | | | | | | 
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
| | | | | | | | | | | | | | | | | | | | 
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
| | | | | | | | | | | | | | | | | | | | 
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
| | | | | | | | | | | | | | | | | | | | 
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
| | | | | | | | | | | | | | | | | | | | 
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
| | | | | | | | | | | | | | | | | | | | 
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
| | | | | | | | | | | | | | | | | | | | 
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
| | | | | | | | | | | | | | | | | | | | 
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
| | | | | | | | | | | | | | | | | | | | 
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
| | | | | | | | | | | | | | | | | | | |  
'''

COLORS = [[0,0,0],[250,0,0],[0,0,250],[250,250,250]]

def draw_maze(maze,canvas):    
    
    # Walls
    for y in range(16):
        for x in range(20):
            canvas.SetPixel(23+x*4,15+y*4,*COLORS[1])
            top = maze[y*20+x]&2
            left = maze[y*20+x]&1
            for i in range(4):   
                if top:             
                    canvas.SetPixel(23+x*4+i,15+y*4,*COLORS[1])
                if left:
                    canvas.SetPixel(23+x*4,15+y*4+i,*COLORS[1])
                    
    # Top and (double) bottom
    for x in range(83):
        canvas.SetPixel(x+22,14,*COLORS[1])
        canvas.SetPixel(x+22,67+12,*COLORS[1])
        canvas.SetPixel(x+22,67+13,*COLORS[1])
    
    # Left and (double) right
    for y in range(64):
        canvas.SetPixel(22,y+15,*COLORS[1])
        canvas.SetPixel(83+20,y+15,*COLORS[1])
        canvas.SetPixel(83+21,y+15,*COLORS[1])
        
    """
    for y in range(16):
        for x in range(20):
            canvas.SetPixel(x*4+25,y*4+17,*COLORS[3])
    """
            
def draw_maze_test(pic,canvas):    
    for y in range(16):
        for x in range(20):            
            for i in range(4):
                canvas.SetPixel(23+x*4+i,15+y*4,*COLORS[1])
                canvas.SetPixel(23+x*4,15+y*4+i,*COLORS[1])
    for x in range(83):
        canvas.SetPixel(x+22,14,*COLORS[1])
        canvas.SetPixel(x+22,67+12,*COLORS[1])
        canvas.SetPixel(x+22,67+13,*COLORS[1])
    for y in range(64):
        canvas.SetPixel(22,y+15,*COLORS[1])
        canvas.SetPixel(83+20,y+15,*COLORS[1])
        canvas.SetPixel(83+21,y+15,*COLORS[1])
    for y in range(16):
        for x in range(20):
            canvas.SetPixel(x*4+25,y*4+17,*COLORS[3])

canvas = matrix.CreateFrameCanvas()

mega = MegaMaze(20,16,192)
draw_maze(mega._maze,canvas)

matrix.SwapOnVSync(canvas)

while True:
    time.sleep(1)
    