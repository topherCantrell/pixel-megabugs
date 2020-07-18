import hardware
from frame import Frame
import time

"""

xxx,yyy ... xxx,yyy    xxx,yyy ... xxx,yyy
|                 |    |                 |
xxx,yyy ... xxx,yyy    xxx,yyy ... xxx,yyy

255,031 ... xxx,yyy    192,031 ... xxx,yyy
|                 |    |                 |
xxx,yyy ..< 192,000    191,000 ..< 128,000

000,000 >.. 063,000    064,000 >.. 128,000
|                 |    |                 |
000,031 ... 063,031    064,031 ... 128,031

"""

def draw_shape(fr,x,y):
    for i in range(8):
        fr.set_pixel(x+i,y,4)
        fr.set_pixel(x,y+i,4)
        fr.set_pixel(x+1,y+1,1)
        fr.set_pixel(x+2,y+2,2)
        fr.set_pixel(x+3,y+3,3)

fr = Frame()

draw_shape(fr,0,0)

hardware.render_frame(fr)

print('sleeping')
time.sleep(10)
