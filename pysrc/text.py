import graphics as GR
import copy

def _translate_color(data,color):
    ret = copy.deepcopy(data)
    for iy in range(len(ret)):
        for ix in range(len(ret[iy])):
            if ret[iy][ix]:
                ret[iy][ix] = color    
    return ret

def draw_text(pic,x,y,text,colors,start=0):      
    if not isinstance(colors,list):
        colors = [colors]          
    for g in text:
        ch = _translate_color(GR.CHARS[g],colors[start])
        pic.draw_image(x,y,ch)
        x+=len(ch[0])
        start +=1
        if start>=len(colors):
            start = 0
