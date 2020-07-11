import hardware
import text
from frame import Frame
import graphics as GR
import pygame
import transitions

def handle(clock,event_handler):
    
    #print('Mode: Splash')
    hardware.set_colors(GR.COLOR_PALETTE)
    
    pic = Frame()
    
    color_start1 = 0
    color_start2 = 1
    color_start3 = 2
    
    colors = [GR.COLORS_SPLASH_TEXT,GR.COLORS_SPLASH_TEXT+1,GR.COLORS_SPLASH_TEXT+2,GR.COLORS_SPLASH_TEXT+3]
    
    text.draw_text(pic,22,14,'Bob Bishop',GR.COLOR_CRUMB)
    text.draw_text(pic,22,34,'Steve Bjork',GR.COLOR_CRUMB)
    text.draw_text(pic,22,44,'Datasoft 1982',GR.COLOR_CRUMB)
    text.draw_text(pic,22,74,'Chris Cantrell',colors[1])
    
    text.draw_text(pic,10,4,'DUNG BEETLES',colors,color_start1)        
    text.draw_text(pic,10,24,'Mega-Bug',colors,color_start2)        
    text.draw_text(pic,10,64,'PooBugs',colors,color_start3)
    
    transitions.wipe_out(pic)        
    
    SONG_END = pygame.USEREVENT+1
    pygame.mixer.music.set_endevent(SONG_END)
    pygame.mixer.music.load('splash.wav')
    pygame.mixer.music.play()
    
    while True:                
                
        for event in pygame.event.get():            
            if event.type==25:
                return "Mode: Demo"
            if event_handler:
                ret = event_handler(event)
                if ret:
                    pygame.mixer.music.stop()
                    return ret
        
        nf = Frame(pic)
        
        text.draw_text(nf,10,4,'DUNG BEETLES',colors,color_start1)        
        text.draw_text(nf,10,24,'Mega-Bug',colors,color_start2)        
        text.draw_text(nf,10,64,'PooBugs',colors,color_start3)
        
        color_start1+=1
        if color_start1>=4:
            color_start1 = 0
        color_start2+=1
        if color_start2>=4:
            color_start2 = 0
        color_start3+=1
        if color_start3>=4:
            color_start3 = 0
        
        hardware.render_frame(nf)
            
        clock.tick(10)