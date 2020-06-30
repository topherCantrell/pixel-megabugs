import graphics as GR
from frame import Frame

def draw_bugs_on_magnifier(pic,x,y,s,bugs):
    sx = x-int(s/2) # This works out better if s is even
    sy = y-int(s/2)
    for bug in bugs:
        bx = (bug.x - x)*2+x -s//2
        by = (bug.y - y)*2+y -s//2
        gr = GR.LITTLE_BUG.images[bug.direction*2+bug.animation]
        for iy in range(6):
            for ix in range(6):
                bix = bx-2+ix
                biy = by-2+iy
                if bix>=sx and biy>=sy and bix<sx+s*2 and biy<sy+s*2:
                    bp = gr[iy][ix]
                    if bp:
                        pic.set_pixel(bix,biy,bp)

def draw_mouth_on_magnifier(pic,mouth):    
    gr = GR.MOUTH.images[mouth.direction*2+mouth.animation]    
    hit_bug = False
    for iy in range(6):
        for ix in range(6):
            bp = gr[iy][ix]
            if bp:
                o = pic.get_pixel(mouth.x-2+ix,mouth.y-2+iy)
                if o>=GR.COLORS_BUG and o<=GR.COLORS_BUG+16:
                    hit_bug = True
                pic.set_pixel(mouth.x-2+ix,mouth.y-2+iy,bp)
    return hit_bug

def draw_magnifier(pic,x,y,s):    
    ret = Frame(pic)
    sx = x-int(s/2) # This works out better if s is even
    sy = y-int(s/2)
    lc = GR.COLOR_LENS_BORDER
    for iy in range(s):
        for ix in range(s):
            op = pic.get_pixel(ix+x,iy+y) + 128 # Set upper bit
            ret.set_pixel(sx+ix*2,sy+iy*2,op)
            ret.set_pixel(sx+ix*2+1,sy+iy*2,op)
            ret.set_pixel(sx+ix*2,sy+iy*2+1,op)
            ret.set_pixel(sx+ix*2+1,sy+iy*2+1,op)
    for i in range(s*2+2):
        ret.set_pixel(sx-1+i,sy-1,lc)
        ret.set_pixel(sx-1+i,sy+s*2,lc)
        ret.set_pixel(sx-1,sy-1+i,lc)
        ret.set_pixel(sx+s*2,sy-1+i,lc)  
            
    return ret