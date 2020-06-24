import graphics as GR
import random
from object_2d import Object2D

class Bug(Object2D):        
    
    def __init__(self,x,y,direction):
        super().__init__(x,y,direction)        
        self.animation = random.randint(0,1)
        self.every_other = random.randint(0,1)
        
    def move(self,frame):
        # Get surrounding directions
        
        # Always wiggle legs
        self.animation += 1
        self.animation &=1
        
        # Only move every other time
        self.every_other+=1
        self.every_other&=1
        
        if self.every_other:    
            rev = (self.direction+2)&3   
            possibles = [] 
            eyes = self.look_at_maze(frame)
            if GR.COLOR_CRUMB in eyes:
                if eyes[rev] == GR.COLOR_CRUMB:
                    # Sneaking up on me, eh?
                    possibles = [rev]
                else:
                    for i in range(4):
                        if eyes[i]==GR.COLOR_CRUMB:
                            possibles.append(i)   
            else:  
                for i in range(4):
                    if eyes[i]!='wall':
                        possibles.append(i)    
                # Avoid reversing if we can help it
                if len(possibles)>1:
                    rev = (self.direction+2)&3
                    if rev in possibles:
                        possibles.remove(rev)
                
            self.direction = random.choice(possibles)
            ofs = Object2D.DIR_OFFS[self.direction]
            self.x += ofs[0]
            self.y += ofs[1]
    
