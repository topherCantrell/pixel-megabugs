
class BitImage:
        
    def __init__(self,text,color_ofs=1):
        self.images = []
        for ti in text:
            image = []            
            ti = ti.strip().split('\n')
            for i in range(len(ti)):
                ti[i] = ti[i].strip()
                row = []
                for c in ti[i]:
                    if c=='.':
                        c=0
                    else:
                        c = int(c,16)-1+color_ofs
                    row.append(c)
                image.append(row)
            self.images.append(image)        
