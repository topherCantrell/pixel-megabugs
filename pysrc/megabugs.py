import pygame

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

import hardware

import graphics as GR
import mode_game
import mode_splash
import mode_win
import mode_lose
import mode_demo
import sys

clock = pygame.time.Clock()

hardware.set_colors(GR.COLOR_PALETTE)

# Just for demonstration/development
def demo_events(event):
    
    if event.joy!=0:
        return None
    
    if event.type!=10:
        return None       
    
    alt = joystick.get_axis(0)!=0 or joystick.get_axis(1)!=0
    
    if event.button==3 and alt:
        pygame.mixer.music.stop()
        from PIL import Image # Only needed for demo
        import time           # Only needed for demo
        im = Image.open('adafruit.jpg')
        canvas = hardware.get_raw_canvas()
        canvas.SetImage(im)
        hardware.render_raw_canvas(canvas)
        
        while True:
            time.sleep(1)
    
    if event.button==1 and alt:
        while True:
            pygame.mixer.music.pause()
            while True:
                for evt in pygame.event.get():
                    #print(evt)
                    if evt.type==10 and evt.button==1:
                        pygame.mixer.music.unpause()
                        return None   
                clock.tick(10) 
                
    if event.button==4 and alt:
        #print('MAN WIN')
        mode_game.manual_win()
        return None
    
    if event.button==4: # LEFT
        return "Mode: Win"
    if event.button==5: # RIGHT
        return "Mode: Lose"
    if event.button==8: # SELECT
        return "Mode: Splash"
    if event.button==9: # START
        if alt:            
            return "Mode: Demo"
        else:
            return "Mode: Game"    
    if event.button<4: # X,A,B,Y
        hardware.set_colors(GR.COLOR_STYLES[event.button])            
    return None

# For the real game-play
def app_events(event):
    if event.type==10 and event.joy==0 and event.button==9: # START
        return "Mode: Game"           

# Add any word to the command line to enter demo mode
        
if len(sys.argv)>1:
    # This is demonstration mode
    evts = demo_events        
    #mode = "Mode: Demo"
else:
    evts = app_events

mode = "Mode: Splash"

while True:
    if mode=='Mode: Splash':
        mode_game.reset_loopiness()
        mode = mode_splash.handle(clock,evts)
    elif mode=='Mode: Lose':
        mode_game.reset_loopiness()
        mode = mode_lose.handle(clock)
    elif mode=='Mode: Win':
        mode_game.more_loopiness()
        mode = mode_win.handle(clock)
    elif mode=='Mode: Demo':
        mode_game.reset_loopiness()
        mode = mode_demo.handle(clock,evts)
    elif mode=='Mode: Game':
        mode = mode_game.handle(clock,joystick,evts)
    else:
        raise Exception('Unknown mode '+mode)