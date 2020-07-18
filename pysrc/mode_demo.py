import random

import graphics as GR
from frame import Frame
from maze import Maze
from bug import Bug
from mouth import Mouth
import magnifier as MAG
import hardware
import transitions

import text
import pygame

import mode_game
import time

DEMO_LOOPS = 200 # 000 

def handle(clock,event_handler):
    #print('Mode: Demo')
    
    # Make the bugs (not too close to center)
    bugs = []    
    for _ in range(16):
        while True:
            cx = random.randint(0,19)        
            cy = random.randint(0,15)
            if (cx>=6 and cx<14) and (cy>=6 and cy<14):
                continue
            break
        bugs.append(Bug(cx*4+25,cy*4+17,random.randint(0,3)))
    
    pic = Frame()
    
    # Draw the bugs
    mega = Maze(20,16,192)
    mode_game.draw_maze(mega._maze,pic)     
    
    # Draw the big bugs
    bugimage = GR.BIG_BUG
    pic.draw_image(3,32,bugimage['standing'])
    pic.draw_image(108,32,bugimage['standing'])
    
    # The mouth
    mouth = Mouth(25+10*4,17+8*4,random.randint(0,3))
    
    # Don't start on a dot
    pic.set_pixel(mouth.x,mouth.y,0)
    
    hs = str(mode_game.HIGH_SCORE).rjust(4,'0')  
    text.draw_text(pic,19,4,'High Score '+hs,GR.COLOR_SCORE)
    text.draw_text(pic,26,84,'Play Giga-Bug',GR.COLOR_SCORE)   
    
    transitions.wipe_in(pic)      
       
    """
    base_frame = Frame()
    
    base_frame.draw_image(10,15, GR.CHARS['A']) # The letter 'A'
    base_frame.draw_text(5,5,    GR.CHARS,'Demonstration')
    base_frame.draw_image(20,25, GR.BIG_BUG['standing']) # Bug standing
    base_frame.draw_image(50,25, GR.BIG_BUG['dancing'][0]) # Bug dancing ...
    base_frame.draw_image(70,25, GR.BIG_BUG['dancing'][1]) # ... two animations   
    
    direction = 1 # 0=UP, 1=RIGHT, 2=DOWN, 3=LEFT
    animation = 0 # 0 or 1 ... two animations
    
    while True:
        frame = Frame(base_frame)        
             
        frame.draw_image(10,60, GR.MOUTH[direction][animation])
            
        hardware.render_frame(frame)
        
        animation = (animation + 1) % 2
    
        time.sleep(0.25)  
    """
        
    clock.tick(0.75)
    nf = MAG.draw_magnifier(pic,mouth.x-8,mouth.y-8,17)
    MAG.draw_mouth_on_magnifier(nf,mouth)
    hardware.render_frame(nf)    
    clock.tick(0.75)                  
    
    # Play this setup
    return play_game(clock,pic,mouth,bugs,event_handler)    

def play_game(clock,mf,mouth,bugs,event_handler):      
               
    sound_eat = pygame.mixer.Sound('eat.wav')    
            
    for _ in range(DEMO_LOOPS):
        
        for event in pygame.event.get():           
            if event_handler:
                ret = event_handler(event)
                if ret:
                    return ret     
        
        # Object for this frame
        nf = Frame(mf) 
        
        # Draw the bugs as dots        
        for bug in bugs:
            nf.set_pixel(bug.x,bug.y,GR.COLOR_BUG_AS_DOT)    
        
        # Magnify the maze and bugs
        nf = MAG.draw_magnifier(nf,mouth.x-8,mouth.y-8,17)
        
        # Draw any bugs appearing on the magnifier (not just dots)
        MAG.draw_bugs_on_magnifier(nf,mouth.x-8,mouth.y-8,17,bugs)
        
        # Draw the mouth and check for bug collision
        hit_bug = MAG.draw_mouth_on_magnifier(nf,mouth)
        hit_bug = False
        
        # Render the frame
        hardware.render_frame(nf)
                
        if hit_bug:
            return "Mode: Splash"
               
        clock.tick(10)
        
        if mf.get_pixel(mouth.x,mouth.y)==GR.COLOR_DOT:            
            sound_eat.play()                                   
            
        # Leave a crumb (also erases the dot)
        if mouth.animation==0:
            mf.set_pixel(mouth.x,mouth.y,GR.COLOR_CRUMB)
        
        # Erase crumbs taken by bugs
        for bug in bugs:
            if mf.get_pixel(bug.x,bug.y)==GR.COLOR_CRUMB:
                mf.set_pixel(bug.x,bug.y,0)
            bug.move(mf)
        
        # Move the mouth
        mouth.move(mf,None,None)
        
    return "Mode: Splash"