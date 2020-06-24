import hardware
from frame import Frame

from mega_maze import MegaMaze
import graphics as GR
import copy
from bug import Bug
import time
import random
from mouth import Mouth

def _translate_color(data,color):
    ret = copy.copy(data)
    for iy in range(len(ret)):
        for ix in range(len(ret[iy])):
            if ret[iy][ix]:
                ret[iy][ix] = color    
    return ret

def draw_text(pic,x,y,text,color=None):    
    mp = GR.CHARS.CHAR_MAP    
    for g in text:
        if color is None:            
            pic.draw_image(x,y,mp[g])
        else:
            pic.draw_image(x,y,_translate_color(mp[g],color))
        x+=6

def draw_bugs_on_magnifier(pic,x,y,s,bugs):
    sx = x-int(s/2) # This works out better if s is even
    sy = y-int(s/2)
    for bug in bugs:
        bx = (bug.x - x)*2+x -s//2
        by = (bug.y - y)*2+y -s//2
        gr = GR.LITTLE_BUG._images[bug.direction*2+bug.animation]
        for iy in range(6):
            for ix in range(6):
                bix = bx-2+ix
                biy = by-2+iy
                if bix>=sx and biy>=sy and bix<sx+s*2 and biy<sy+s*2:
                    bp = gr[iy][ix]
                    if bp:
                        pic.set_pixel(bix,biy,bp)

def draw_mouth_on_magnifier(pic,mouth):    
    gr = GR.MOUTH._images[mouth.direction*2+mouth.animation]    
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
            op = pic.get_pixel(ix+x,iy+y)
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

def draw_maze(maze,pic):    
    
    wc = GR.COLORS_MAZE_WALL
    dc = GR.COLOR_DOT
    
    # Walls
    for y in range(16):
        for x in range(20):
            pic.set_pixel(23+x*4,15+y*4,wc)
            top = maze[y*20+x]&2
            left = maze[y*20+x]&1
            for i in range(4):   
                if top:        
                    pic.set_pixel(23+x*4+i,15+y*4,wc)
                if left:
                    pic.set_pixel(23+x*4,15+y*4+i,wc)
            pic.set_pixel(25+x*4,17+y*4,dc)
                    
    # Top and (double) bottom
    for x in range(83):
        pic.set_pixel(x+22,14,wc)
        pic.set_pixel(x+22,67+12,wc)
        pic.set_pixel(x+22,67+13,wc)
    
    # Left and (double) right
    for y in range(64):
        pic.set_pixel(22,y+15,wc)
        pic.set_pixel(83+20,y+15,wc)
        pic.set_pixel(83+21,y+15,wc)
        
hardware.set_colors(GR.COLOR_PALETTE)

bugs = []

for i in range(16):
    while True:
        cx = random.randint(0,19)        
        cy = random.randint(0,15)
        if (cx>=6 and cx<14) and (cy>=6 and cy<14):
            continue
        break
    bugs.append(Bug(cx*4+25,cy*4+17,random.randint(0,3)))
       
bugimage = GR.BIG_BUG.get_images()
pic = Frame()
mega = MegaMaze(20,16,192)
draw_maze(mega._maze,pic)
pic.draw_image(3,32,bugimage[0])
pic.draw_image(108,32,bugimage[0])
        
draw_text(pic,19,4,'High Score 0000',2)

mouth = Mouth(25+10*4,17+8*4,0)

pic.set_pixel(mouth.x,mouth.y,0)

while True:
    
    # Start by drawing the bugs as dots
    nf = Frame(pic)    
    for bug in bugs:
        nf.set_pixel(bug.x,bug.y,GR.COLOR_BUG_AS_DOT)
    
    # Magnify the maze and bugs
    nf = draw_magnifier(nf,mouth.x-8,mouth.y-8,17)
    
    # Draw any bugs appearing on the magnifier (not just dots)
    draw_bugs_on_magnifier(nf,mouth.x-8,mouth.y-8,17,bugs)
    
    # Draw the mouth and check for bug collision
    hit_bug = draw_mouth_on_magnifier(nf,mouth)
    
    # Render the frame
    hardware.render_frame(nf)    
    
    if hit_bug:
        while True:
            time.sleep(1)            
    time.sleep(0.05)
    
    if pic.get_pixel(mouth.x,mouth.y)==GR.COLOR_DOT:
        pass
        # Register the score, make noise
        
    # Leave a crumb (also erases the dot)
    if mouth.animation==0:
        pic.set_pixel(mouth.x,mouth.y,GR.COLOR_CRUMB)
    
    # Erase crumbs taken by bugs
    for bug in bugs:
        if pic.get_pixel(bug.x,bug.y)==GR.COLOR_CRUMB:
            pic.set_pixel(bug.x,bug.y,0)
        bug.move(pic)
    
    # Move the mouth   
    mouth.move(pic)
    
    

        
        
    