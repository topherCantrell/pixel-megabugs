
import socket
import time
import json

COLORS1 = [[0,0,0],[50,0,0],[0,0,50],[50,50,50]]
COLORS2 = [[0,0,0],[0,0,50],[50,0,0],[50,50,50]]

DISPLAYS = {
    'one'   : {'address' : '10.0.0.52', 'offset' : 0},
    'two'   : {'address' : '10.0.0.55', 'offset' : 4096},
    'three' : {'address' : '10.0.0.62', 'offset' : 4096*2}
    }

def get_frame_snapshot(screen):
    with open('../../frame.txt') as f:
        data = json.loads(f.read())
        
    for i in range(len(data)):
        if data[i]<0:
            data[i] += 256
            
    start = screen*0x0C00+0x0400
            
    # Get the COCO data
    frame = data[start:start+0x0C00]
    
    # Decode the 4-pixels-per-byte structure
    ret = []
    for d in frame:
        ret.append((d>>6)&3)
        ret.append((d>>4)&3)
        ret.append((d>>2)&3)
        ret.append(d&3)
        
    return ret

def send_frame(colors,pixels):
                
    data = b''
    for pix in colors:
        print(pix)
        data = data + bytes(pix)
    
    for dis in DISPLAYS:
        cs = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    
        cs.connect((DISPLAYS[dis]['address'],1234))        
        cs.send(bytes([len(colors)-1]))    
        cs.send(data)
        start = DISPLAYS[dis]['offset']        
        cs.send(bytes(pixels[start:start+4096]))

pixels = get_frame_snapshot(2)  
send_frame(COLORS1,pixels)  

"""
pixels = get_frame_snapshot(2)
SV = 0.1
while True:
    send_frame(COLORS1,pixels)
    time.sleep(SV)
    send_frame(COLORS2,pixels)
    time.sleep(SV)
"""
