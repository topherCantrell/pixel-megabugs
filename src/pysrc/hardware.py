from rgbmatrix import RGBMatrix, RGBMatrixOptions
from rgbmatrix import graphics

"""
3 chains of 2 panels. Each panel is 64x32:

 64 + 64 = 128
 64 + 64
 64 + 64
 -------
 96
 
"""

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

def set_colors(colors):
    global COLORS
    COLORS = colors
    
def render_frame(frame,colors=None):
    if colors is None:
        colors = COLORS
    canvas = matrix.CreateFrameCanvas()
    pixels = frame._pixels
    for y in range(96):
        for x in range(128):
            p = pixels[y*128+x]
            canvas.SetPixel(x,y,*colors[p])
    matrix.SwapOnVSync(canvas)
    