import graphics as GR
import copy

def _translate_color(data,color):
    ret = copy.copy(data)
    for iy in range(len(ret)):
        for ix in range(len(ret[iy])):
            if ret[iy][ix]:
                ret[iy][ix] = color    
    return ret

def draw_text(pic,x,y,text,colors,start=0):    
    mp = GR.CHARS.CHAR_MAP    
    for g in text:
        pic.draw_image(x,y,_translate_color(mp[g],colors[start]))
        x+=6
        start +=1
        if start>=len(colors):
            start = 0
