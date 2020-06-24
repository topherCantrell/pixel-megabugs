
class Frame:
    
    def __init__(self,pix=None):
        if pix is None:
            self._pixels = [0]*128*96
        else:
            self._pixels = pix._pixels[:]
        
    def set_pixel(self,x,y,color):
        self._pixels[y*128+x] = color        
        
    def get_pixel(self,x,y):
        return self._pixels[y*128+x]
    
    def draw_image(self,x,y,data):
        p = self._pixels
        for iy in range(len(data)):
            for ix in range(len(data[iy])):
                p[(iy+y)*128+ix+x] = data[iy][ix]