from rgbmatrix import RGBMatrix, RGBMatrixOptions
from rgbmatrix import graphics
from PIL import Image

from frame import Frame

"""
3 chains of 2 panels. Each panel is 64x32:

 64 + 64 = 128
 64 + 64
 64 + 64
 -------
 96
 
"""

options = RGBMatrixOptions()
        
options.hardware_mapping = 'adafruit-hat'
options.rows = 32 # 32 rows per display
options.cols = 64 # 64 rows per display (64x32)

# Heller Zenner board
#options.chain_length = 2 # 2 displays per chain (128x32)
#options.parallel = 3 # 3 (128x96)

options.chain_length = 6
options.parallel = 1

options.disable_hardware_pulsing = False
options.pwm_bits = 11
options.gpio_slowdown = 2
options.pwm_lsb_nanoseconds = 50
                
matrix = RGBMatrix(options = options)

# Some default colors
COLORS = [[0,0,0],[250,0,0],[0,255,0],[0,0,250],[250,250,250]]

def set_colors(colors):
    global COLORS
    COLORS = colors

last_rendered_frame = Frame()


def _one_panel(src, dst, sx, sy, dx, forward, colors):
    pixels = src._pixels

    if forward:
        for y in range(32):
            for x in range(64):
                p = pixels[(sy+y)*128+sx+x]
                dst.SetPixel(dx+x, y, *colors[p])
    else:
        for y in range(32):
            for x in range(64):
                p = pixels[(sy+y)*128+sx+x]
                dst.SetPixel(dx+63-x, 31-y, *colors[p])


def render_frame(frame,colors=None):
    
        
    """    
    000,000 >.. 063,000    064,000 >.. 128,000
    |                 |    |                 |
    000,031 ... 063,031    064,031 ... 128,031    
    
    255,031 ... xxx,yyy    192,031 ... xxx,yyy
    |                 |    |                 |
    xxx,yyy ..< 192,000    191,000 ..< 128,000
    
    256,000 ... xxx,yyy    320,000 ... xxx,yyy
    |                 |    |                 |
    xxx,yyy ... 391,031    xxx,yyy ... 383,031
    """    

    global last_rendered_frame 
    last_rendered_frame = frame
    if colors is None:
        colors = COLORS
    canvas = matrix.CreateFrameCanvas()

    _one_panel(frame, canvas, 0, 0, 0, True, colors)
    _one_panel(frame, canvas, 64, 0, 64, True, colors)
    
    _one_panel(frame, canvas, 0,32, 192, False, colors)
    _one_panel(frame, canvas, 64,32, 128, False, colors)
    
    _one_panel(frame, canvas, 0, 64, 256, True, colors)
    _one_panel(frame, canvas, 64, 64, 320, True, colors)
    
    matrix.SwapOnVSync(canvas)

    
def render_frame_zeller(frame,colors=None):
    global last_rendered_frame
    last_rendered_frame = frame
    if colors is None:
        colors = COLORS
    canvas = matrix.CreateFrameCanvas()
    pixels = frame._pixels
    
    pos = 0
    for y in range(32):
        for x in range(64*6):
            p = pixels[pos]
            pos+=1
            canvas.SetPixel(x,y,*colors[p])
            
    """
    for y in range(96):
        for x in range(128):
            p = pixels[y*128+x]
            canvas.SetPixel(x,y,*colors[p])
    """
    matrix.SwapOnVSync(canvas)
    
def get_raw_canvas():
    return matrix.CreateFrameCanvas()

def render_raw_canvas(canvas):
    matrix.SwapOnVSync(canvas)
