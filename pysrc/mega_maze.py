import random

class MegaMaze:
    
    DIR_OFFS = [
        [0,-1], # 0 = Up
        [1,0],  # 1 = Right
        [0,1],  # 2 = Down
        [-1,0]  # 3 = Left
    ]
    
    def __init__(self,width,height,loopiness):
        
        # Maze structure
        self._width = width
        self._height = height
        self._loopiness = loopiness
        
        # Fill all walls in the maze 2=visited, 1=top, 0=left
        self._maze = [3]*width*height
        
        # List of cells that need visiting
        self._visit_next = []
        
        # Starting in the center cell
        cx = int(width/2)
        cy = int(height/2)
        cd = -1 # Current direction (we'll pick one at random shortly)
        
        # We start here
        self.mark_visited(cx,cy)
        
        # Open all neighboring cells and add them to the
        # needs-visiting list
        for d in range(4):
            self.open_cell_wall(cx,cy,d)
            nx,ny = self.get_neighbor_coord(cx,cy, d)
            self.push_needs_visiting(nx,ny)
            self.mark_visited(nx,ny)        
            
        while self._visit_next:
            cx,cy = self.pop_needs_visiting()
            self.mark_visited(cx,cy)
            opened_wall = False
            
            while True:
                # Build list of unvisited neighbors
                possible_dirs = []
                for d in range(4):
                    nx,ny = self.get_neighbor_coord(cx,cy,d)
                    if (nx is not None) and (not self.is_visited(nx,ny)):
                        possible_dirs.append(d)                                     
                
                if not possible_dirs:
                    # There no a direction we can go. End with a dead end or a loop.
                    if opened_wall:
                        nx,ny = self.get_neighbor_coord(cx,cy,cd)
                        if nx is not None:
                            r = random.randint(0,255)
                            if r<loopiness:
                                self.open_cell_wall(cx,cy,cd)
                    break # Done with this run. Back to pop off next to visit
                
                # If there are multiple free neighbors then we need to revisit this
                if len(possible_dirs)>1:                    
                    self.push_needs_visiting(cx,cy)
                    
                # Pick a random valid direction and move to it
                cd = random.choice(possible_dirs)
                self.open_cell_wall(cx,cy,cd)
                opened_wall = True               
                cx,cy = self.get_neighbor_coord(cx,cy,cd)
                self.mark_visited(cx,cy)
   
        
    def get_neighbor_coord(self,cx,cy,direction):
        nx = cx + MegaMaze.DIR_OFFS[direction][0]
        ny = cy + MegaMaze.DIR_OFFS[direction][1]
        if nx<0 or ny<0 or nx>=self._width or ny>=self._height:
            return None,None
        return nx,ny
    
    def open_cell_wall(self,cx,cy,direction):
        if direction==0: # Up
            p = cy*self._width + cx            
            self._maze[p] &= 5
        elif direction==3: # Left
            p = cy*self._width + cx
            self._maze[p] &= 6
        elif direction==1: # Right
            nx,ny = self.get_neighbor_coord(cx,cy,direction)
            p = ny*self._width + nx
            self._maze[p] &= 6
        elif direction==2: # Down
            nx,ny = self.get_neighbor_coord(cx,cy,direction)
            p = ny*self._width + nx
            self._maze[p] &= 5
        else:
            raise Exception('Invalid direction '+str(direction))
    
    def is_visited(self,cx,cy):
        p = cy*self._width + cx
        if (self._maze[p] & 4) == 4:
            return True
        return False
    
    def mark_visited(self,cx,cy):
        #if self.is_visited(coord):
        #    raise Exception('Visiting twice '+str(coord))
        p = cy*self._width + cx
        self._maze[p] |= 4
    
    def pop_needs_visiting(self):
        return self._visit_next.pop(0)
    
    def push_needs_visiting(self,cx,cy):
        return self._visit_next.append((cx,cy))
    
if __name__ == '__main__':
    maze = MegaMaze(20,16,192)