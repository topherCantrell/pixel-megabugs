import pygame
import graphics as GR
import hardware

def handle(clock):    
    #print('Mode: Lose')
    
    last_maze_frame = hardware.last_rendered_frame

    SONG_END = pygame.USEREVENT+1
    pygame.mixer.music.set_endevent(SONG_END)
    pygame.mixer.music.load('gotcha.wav')
    pygame.mixer.music.play()
        
    bugimage = GR.BIG_BUG      
    animation = 0   
    
    playing = True
    while playing:
        for event in pygame.event.get():
            #print(event)
            if event.type==25:
                playing = False
                
        #print(bugimage['dancing'])
                                            
        last_maze_frame.draw_image(3,32,bugimage['dancing'][animation])
        last_maze_frame.draw_image(108,32,bugimage['dancing'][animation])
        
        hardware.render_frame(last_maze_frame)
        
        animation+=1
        animation&=1
            
        clock.tick(4)
        
    for _ in range(8):                                                    
        last_maze_frame.draw_image(3,32,bugimage['dancing'][animation])
        last_maze_frame.draw_image(108,32,bugimage['dancing'][animation])        
        hardware.render_frame(last_maze_frame)        
        animation+=1
        animation&=1            
        clock.tick(4)
    
    clock.tick(1)    
    return "Mode: Splash"