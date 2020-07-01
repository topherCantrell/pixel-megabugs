import datetime
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

HIGH_SCORE = 0
MAN_WIN = False

LOOPINESS = 192

def manual_win():
    global MAN_WIN
    MAN_WIN = True
    
def more_loopiness():
    global LOOPINESS
    LOOPINESS = LOOPINESS//2
    
def reset_loopiness():
    global LOOPINESS
    LOOPINESS = 192

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

def handle(clock,joystick,event_handler):
    #print('Mode: Game')
    
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
    mega = Maze(20,16,LOOPINESS)
    draw_maze(mega._maze,pic)     
    
    # Draw the big bugs
    bugimage = GR.BIG_BUG.images
    pic.draw_image(3,32,bugimage[0])
    pic.draw_image(108,32,bugimage[0])
    
    # The mouth
    mouth = Mouth(25+10*4,17+8*4,random.randint(0,3))
    
    # Don't start on a dot
    pic.set_pixel(mouth.x,mouth.y,0)        
    
    text.draw_text(pic,33,4,'Time:',[GR.COLOR_SCORE])
    text.draw_text(pic,33,84,'Score:',[GR.COLOR_SCORE])
    text.draw_text(pic,69,4,'00:00',[GR.COLOR_SCORE])
    text.draw_text(pic,75,84,'0000',[GR.COLOR_SCORE]) 
    
    transitions.wipe_in(pic)        
        
    clock.tick(0.75)
    nf = MAG.draw_magnifier(pic,mouth.x-8,mouth.y-8,17)
    MAG.draw_mouth_on_magnifier(nf,mouth)
    hardware.render_frame(nf)    
    clock.tick(0.75)          
    
    # Play this setup
    return play_game(clock,joystick,pic,mouth,bugs,20*16-1,event_handler)    

def play_game(clock,joystick,mf,mouth,bugs,num_dots,event_handler):      
    
    global HIGH_SCORE
    global MAN_WIN
               
    sound_eat = pygame.mixer.Sound('eat.wav')
                
    text.draw_text(mf,33,4,'Time:',[GR.COLOR_SCORE])
    text.draw_text(mf,33,84,'Score:',[GR.COLOR_SCORE])     
                
    score = 0
    dots_eaten = 0
        
    start_time = datetime.datetime.now()
    
    last_time = None
    
    while True:
        
        for event in pygame.event.get():            
            if event_handler:
                ret = event_handler(event)
                if ret:
                    return ret         
        
        # Object for this frame
        nf = Frame(mf)
        
        # The score and timer
        now = datetime.datetime.now()
        secs = (now-start_time).seconds
        if not last_time:
            last_time = secs
            
        if last_time != secs and score>0:
            score = score - 1
            last_time = secs
        
        up_secs = secs//60
        low_secs = secs%60
        time_text = str(up_secs).rjust(2,'0') + ':'+str(low_secs).rjust(2,'0')    
        
        score_text = str(score).rjust(4,'0')
        text.draw_text(nf,69,4,time_text,[GR.COLOR_SCORE])
        text.draw_text(nf,75,84,score_text,[GR.COLOR_SCORE])    
                        
        # Draw the bugs as dots        
        for bug in bugs:
            nf.set_pixel(bug.x,bug.y,GR.COLOR_BUG_AS_DOT)    
        
        # Magnify the maze and bugs
        nf = MAG.draw_magnifier(nf,mouth.x-8,mouth.y-8,17)
        
        # Draw any bugs appearing on the magnifier (not just dots)
        MAG.draw_bugs_on_magnifier(nf,mouth.x-8,mouth.y-8,17,bugs)
        
        # Draw the mouth and check for bug collision
        hit_bug = MAG.draw_mouth_on_magnifier(nf,mouth)
        #hit_bug = False
        
        # Render the frame
        hardware.render_frame(nf)
                
        if hit_bug:
            
            SONG_END = pygame.USEREVENT+1
            pygame.mixer.music.set_endevent(SONG_END)
            pygame.mixer.music.load('touch.wav')
            pygame.mixer.music.play()            
            while True:
                for event in pygame.event.get():            
                    if event.type==25:
                        # "undraw" the magnifier
                        nf = Frame(mf)    
                        nf.set_pixel(mouth.x,mouth.y,0)            
                        text.draw_text(nf,69,4,time_text,[GR.COLOR_SCORE])
                        text.draw_text(nf,75,84,score_text,[GR.COLOR_SCORE]) 
                        for bug in bugs:
                            nf.set_pixel(bug.x,bug.y,GR.COLOR_BUG_AS_DOT)    
                        hardware.render_frame(nf)      
                        return "Mode: Lose"    
                clock.tick(10)
               
        clock.tick(10)
        
        if mf.get_pixel(mouth.x,mouth.y)==GR.COLOR_DOT:
            score+=10
            if score>HIGH_SCORE:
                HIGH_SCORE = score
            dots_eaten+=1
            sound_eat.play()
            
            if MAN_WIN or dots_eaten >= num_dots:
                
                MAN_WIN = False
                                
                # "undraw" the magnifier
                nf = Frame(mf)    
                nf.set_pixel(mouth.x,mouth.y,0)            
                text.draw_text(nf,69,4,time_text,[GR.COLOR_SCORE])
                text.draw_text(nf,75,84,score_text,[GR.COLOR_SCORE]) 
                for bug in bugs:
                    nf.set_pixel(bug.x,bug.y,GR.COLOR_BUG_AS_DOT)    
                hardware.render_frame(nf)                
                
                return 'Mode: Win'                       
            
        # Leave a crumb (also erases the dot)
        if mouth.animation==0:
            mf.set_pixel(mouth.x,mouth.y,GR.COLOR_CRUMB)
        
        # Erase crumbs taken by bugs
        for bug in bugs:
            if mf.get_pixel(bug.x,bug.y)==GR.COLOR_CRUMB:
                mf.set_pixel(bug.x,bug.y,0)
            bug.move(mf)
        
        # Move the mouth
        if joystick:   
            mouth.move(mf,joystick.get_axis(0),joystick.get_axis(1))
        else:
            mouth.move(mf,None,None)