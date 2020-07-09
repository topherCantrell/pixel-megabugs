import hardware
import graphics as GR
from frame import Frame
import text
import pygame

def handle(clock):
    #print('Mode: Win')
    
    mf = hardware.last_rendered_frame
    
    sound_step = pygame.mixer.Sound('step.wav')
        
    colors = [GR.COLORS_SPLASH_TEXT,GR.COLORS_SPLASH_TEXT+1,GR.COLORS_SPLASH_TEXT+2,GR.COLORS_SPLASH_TEXT+3]
    
    sc = 0
    og = GR.COLOR_PALETTE[GR.COLORS_MAZE_WALL]
    for i in range(8):
        GR.COLOR_PALETTE[GR.COLORS_MAZE_WALL] = GR.COLOR_PALETTE[colors[sc]]
        sc += 1
        if sc>=len(colors):
            sc = 0
        hardware.render_frame(mf)
        clock.tick(4)
    GR.COLOR_PALETTE[GR.COLORS_MAZE_WALL] = og   
        
    pic = Frame()
    
    text.draw_text(pic,0x1E,0x1B,"We'll Getcha",[GR.COLORS_SPLASH_TEXT+1])
    text.draw_text(pic,0x27,0x28,"Next Time",[GR.COLORS_SPLASH_TEXT+2])
        
    acc = Frame()
        
    seg = 0
    y = 0
    animation = 0
    
    while True:
        
        for _ in pygame.event.get():            
            pass
            
        if seg==0:
            
            if y>0:
                for x in range(128):
                    acc.set_pixel(x,y-2,pic.get_pixel(x,y-2))
                    acc.set_pixel(x,y-1,pic.get_pixel(x,y-1))
            nf = Frame(acc)
            
            sound_step.play(0)
            for i in range(32):
                nf.draw_image(0+i*8,y,GR.LITTLE_BUG[2][animation])
            animation += 1
            animation &= 1 
            y = y + 2
            if y>96:
                seg = 1
                text.draw_text(pic,0x5D,0x28,"!",[GR.COLORS_SPLASH_TEXT+3])
                y = 0
                hardware.render_frame(acc)
                clock.tick(1)
                
            hardware.render_frame(nf)
            
            clock.tick(10)
            
        elif seg==1:
            
            if y>0:
                for x in range(128):
                    acc.set_pixel(x,y-4,pic.get_pixel(x,y-4))
                    acc.set_pixel(x,y-3,pic.get_pixel(x,y-3))
                    acc.set_pixel(x,y-2,pic.get_pixel(x,y-2))
                    acc.set_pixel(x,y-1,pic.get_pixel(x,y-1))
            nf = Frame(acc)
            
            sound_step.play(0)
            nf.draw_image(92,y,GR.LITTLE_BUG[2][animation])
            animation += 1
            animation &= 1 
            y = y + 4
            if y>96:
                seg = 3                
                
            hardware.render_frame(nf)    
            
            clock.tick(15)
            
        else:
            clock.tick(1)
            return "Mode: Game"