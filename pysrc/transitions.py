from frame import Frame
import hardware
import graphics as GR

def wipe_in(fin):
    #print('wipe in')
    nf = Frame(hardware.last_rendered_frame)
            
    for x in range(1,64,2):
        for y in range(96):
            nf.set_pixel(x,y,fin.get_pixel(x,y))
            nf.set_pixel(x-1,y,fin.get_pixel(x-1,y))
            nf.set_pixel(127-x,y,fin.get_pixel(127-x,y))
            nf.set_pixel(127-x+1,y,fin.get_pixel(127-x+1,y))
            if x!=63:
                nf.set_pixel(x+1,y,GR.COLOR_LENS_BORDER)
                nf.set_pixel(127-x-1,y,GR.COLOR_LENS_BORDER)             
        hardware.render_frame(nf)
        #clock.tick(100)
        #time.sleep(0.5)

def wipe_out(fin):
    nf = Frame(hardware.last_rendered_frame)
    
    #src = fin._pixels
    #dst = nf._pixels
    for x in range(1,64,2):
        #a = 63-x
        #b = 64+x
        for y in range(96):            
            #dst[y*128+a] = src[y*128+a]
            #dst[y*128+b] = src[y*128+b]            
            nf.set_pixel(63-x,y,fin.get_pixel(63-x,y))
            nf.set_pixel(63-x+1,y,fin.get_pixel(63-x+1,y))
            nf.set_pixel(64+x,y,fin.get_pixel(64+x,y))
            nf.set_pixel(64+x-1,y,fin.get_pixel(64+x-1,y))
            if x!=63:
                #dst[y*128+a-1] = GR.COLOR_LENS_BORDER
                #dst[y*128+b+1] = GR.COLOR_LENS_BORDER
                nf.set_pixel(63-x-1,y,GR.COLOR_LENS_BORDER)
                nf.set_pixel(64+x+1,y,GR.COLOR_LENS_BORDER)             
        hardware.render_frame(nf)
        #clock.tick(100)
        #time.sleep(0.5)