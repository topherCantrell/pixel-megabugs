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

import copy

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

BIG_BUG = [
    [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0], 
    [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0], 
    [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 1, 1, 1, 3, 1, 1, 3, 1, 1, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0], 
    [0, 0, 0, 2, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 2, 0, 0], 
    [0, 0, 0, 2, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2, 0, 0], 
    [0, 0, 0, 2, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 2, 0, 0], 
    [0, 1, 3, 2, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 3, 2, 0], 
    [1, 3, 2, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 3, 2], 
    [0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0], 
    [0, 0, 0, 2, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2, 0, 0], 
    [0, 0, 0, 2, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 2, 0, 0], 
    [0, 0, 0, 2, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2, 0, 0], 
    [0, 1, 3, 2, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 3, 2, 0], 
    [1, 3, 2, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 3, 2], 
    [0, 0, 0, 0, 0, 2, 2, 1, 1, 1, 0, 2, 2, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0], 
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], 
    [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0]
]


class Screen:
    
    def __init__(self):
        
        self._pixels = [0]*128*96
        
    def draw_image(self,x,y,pic):
        for iy in range(len(pic)):
            for ix in range(len(pic[iy])):
                self._pixels[(iy+y)*128+(ix+x)] = pic[iy][ix]
                
    def set_pixel(self,x,y,color):
        self._pixels[y*128+x] = color        
        
    def get_pixel(self,x,y):
        return self._pixels[y*128+x]
    
    def to_canvas(self,canvas):
        for y in range(96):
            for x in range(128):
                p = self._pixels[y*128+x]
                canvas.SetPixel(x,y,*COLORS[p])

def draw_magnifier(pic,x,y,s=17):    
    org = copy.deepcopy(pic)
    sx = x-int(s/2) # This works out better if s is even
    sy = y-int(s/2)
    for iy in range(s):
        for ix in range(s):
            op = org.get_pixel(ix+x,iy+y)
            #op = COLORS[2]
            pic.set_pixel(sx+ix*2,sy+iy*2,op)
            pic.set_pixel(sx+ix*2+1,sy+iy*2,op)
            pic.set_pixel(sx+ix*2,sy+iy*2+1,op)
            pic.set_pixel(sx+ix*2+1,sy+iy*2+1,op)
    for i in range(s*2+2):
        pic.set_pixel(sx-1+i,sy-1,3)
        pic.set_pixel(sx-1+i,sy+s*2,3)
        pic.set_pixel(sx-1,sy-1+i,3)
        pic.set_pixel(sx+s*2,sy-1+i,3)

def draw_maze(maze,pic):    
    
    # Walls
    for y in range(16):
        for x in range(20):
            pic.set_pixel(23+x*4,15+y*4,1)
            top = maze[y*20+x]&2
            left = maze[y*20+x]&1
            for i in range(4):   
                if top:        
                    pic.set_pixel(23+x*4+i,15+y*4,1)
                if left:
                    pic.set_pixel(23+x*4,15+y*4+i,1)
            pic.set_pixel(25+x*4,17+y*4,2)
                    
    # Top and (double) bottom
    for x in range(83):
        pic.set_pixel(x+22,14,1)
        pic.set_pixel(x+22,67+12,1)
        pic.set_pixel(x+22,67+13,1)
    
    # Left and (double) right
    for y in range(64):
        pic.set_pixel(22,y+15,1)
        pic.set_pixel(83+20,y+15,1)
        pic.set_pixel(83+21,y+15,1)
    
    
mx = 10
ox = 1
my = 10
oy = 1

while True:
        
    mega = MegaMaze(20,16,192)
    
    for i in range(50):       
    
        pic = Screen()
        draw_maze(mega._maze,pic)
        pic.draw_image(2,32,BIG_BUG)
        pic.draw_image(110,32,BIG_BUG)
        
        draw_magnifier(pic,mx,my,18)
        mx+=ox
        my+=oy
        
        if mx>100:
            mx = 100
            ox = -1
        if mx<10:
            mx = 10
            ox = 1
        if my>67:
            my = 67
            oy = -1
        if my<10:
            my = 10
            oy = 1
        
        canvas = matrix.CreateFrameCanvas()
        pic.to_canvas(canvas)
        matrix.SwapOnVSync(canvas)
        
        
    