import graphics as GR
import random
from object_2d import Object2D

class Mouth(Object2D):        
    
    def __init__(self,x,y,direction):
        super().__init__(x,y,direction)        
        self.animation = random.randint(0,1)
        self.every_other = random.randint(0,1)
        self.direction = direction
        self.animation = 0
    
    def move(self,frame):
        self.animation +=1
        self.animation &=1
        eyes = self.look_at_maze(frame)
        
        # Build the list of possible directions        
        possibles = []
        for i in range(4):
            if eyes[i]!='wall':
                possibles.append(i)    
        # Avoid reversing if we can help it
        if len(possibles)>1:
            rev = (self.direction+2)&3
            if rev in possibles:
                possibles.remove(rev)
            
        self.direction = random.choice(possibles)
        
        if eyes[self.direction] != 'wall':
            ofs = Object2D.DIR_OFFS[self.direction]
            self.x += ofs[0]
            self.y += ofs[1]    
    