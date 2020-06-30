from PIL import Image

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from rgbmatrix import graphics

import time

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

im = Image.open('adafruit.jpg')

canvas = matrix.CreateFrameCanvas()
canvas.SetImage(im)
matrix.SwapOnVSync(canvas)

while True:
    time.sleep(1)

"""
data = list(im.getdata())
pos = 0

for y in range(im.height):
    for x in range(im.width):
        pix = data[pos]
        pos += 1
        
        
print(help(dir(canvas)))
"""
    