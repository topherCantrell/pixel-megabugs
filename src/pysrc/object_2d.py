import graphics as GR

class Object2D:
    
    DIR_OFFS = [
        [0,-1], # 0 = Up
        [1,0],  # 1 = Right
        [0,1],  # 2 = Down
        [-1,0]  # 3 = Left
    ]
    
    def __init__(self,x,y,direction):
        self.x = x
        self.y = y
        self.direction = direction
    
    def look_at_maze(self,frame):
        ret = [0x00,0x00,0x00,0x00]                
        x = self.x
        y = self.y
        for i in range(3):
            # UP
            p = frame.get_pixel(x-1+i,y-2)
            if p==GR.COLORS_MAZE_WALL:
                ret[0] = 'wall'
            if not ret[0]:                
                ret[0] = p                
            
            # DOWN
            p = frame.get_pixel(x-1+i,y+2)
            if p==GR.COLORS_MAZE_WALL:
                ret[2] = 'wall'
            if not ret[2]:
                ret[2] = p
                
            # RIGHT
            p = frame.get_pixel(x+2,y-1+i)
            if p==GR.COLORS_MAZE_WALL:
                ret[1] = 'wall'
            if not ret[1]:
                ret[1] = p
                
            # LEFT
            p = frame.get_pixel(x-2,y-1+i)
            if p==GR.COLORS_MAZE_WALL:
                ret[3] = 'wall'
            if not ret[3]:
                ret[3] = p
                
        return ret    