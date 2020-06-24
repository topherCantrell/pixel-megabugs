
from image import BitImage

'''
  00     Transparent  
  01-0F  Misc
     01    Dot
     02    Crumb
     03    Lens border
     04    Bug as dot
  10-1F  Maze wall
  20-2F  Mouth
  30-3F  Bug color
'''

COLOR_DOT = 1
COLOR_CRUMB = 2
COLOR_LENS_BORDER = 3
COLOR_BUG_AS_DOT = 4
COLORS_MAZE_WALL = 0x10
COLORS_MOUTH = 0x20
COLORS_BUG = 0x30

COLOR_PALETTE = []
for i in range(256):
    COLOR_PALETTE.append([0,0,0])

COLOR_PALETTE[COLOR_DOT]            = [0x00, 0xFF, 0x00]
COLOR_PALETTE[COLOR_CRUMB]          = [150, 75, 0]
COLOR_PALETTE[COLOR_LENS_BORDER]    = [0xFF, 0xFF, 0xFF]
COLOR_PALETTE[COLOR_BUG_AS_DOT]     = [0x00, 0x00, 0xFF]

COLOR_PALETTE[COLORS_MAZE_WALL + 0] = [0xFF, 0x00, 0x00]
COLOR_PALETTE[COLORS_MOUTH + 0]     = [0xFF, 0xFF, 0xFF]
COLOR_PALETTE[COLORS_BUG + 0]       = [0x00, 0x00, 0xFF]
COLOR_PALETTE[COLORS_BUG + 1]       = [0x00, 0xFF, 0xFF]
COLOR_PALETTE[COLORS_BUG + 2]       = [0x80, 0x00, 0xFF]

# Magnified colors are the same as non -- for now
for i in range(128):
    COLOR_PALETTE[i+128] = COLOR_PALETTE[i]

LITTLE_BUG = BitImage([
    
#UP
''' 
    1.....
    .1..1.
    .222.1
    1222..
    .1..1.
    .....1
''',
'''
    .....1
    .1..1.
    1222..
    .222.1
    .1..1.
    1.....
''',

#RIGHT
'''
    ..1..1    
    .1..1. 
    .222.. 
    .222.. 
    .1..1. 
    1..1..     
''',
'''
    1..1..
    .1..1.
    .222..
    .222..
    .1..1.
    ..1..1
''',

#DOWN
'''
    1.....
    .1..1.
    .222.1
    1222..
    .1..1.
    .....1
''',
'''
    .....1
    .1..1.
    1222..
    .222.1
    .1..1.
    1.....
''',

#LEFT
'''
    ..1..1    
    .1..1. 
    .222.. 
    .222.. 
    .1..1. 
    1..1..     
''',
'''
    1..1..
    .1..1.
    .222..
    .222..
    .1..1.
    ..1..1
''',    

],COLORS_BUG)

BIG_BUG = BitImage([
'''
    ...2...........2.
    ....2.........2..
    .....2.......2...
    ......2.....2....
    .......2...2.....
    ......11.11......
    .....1111111.....
    ....111311311....
    .....1111111.....
    .....111..11.....
    ......11111......
    .......1.1.......
    ...11.11111.11...
    ...2.111.111..2..
    ...2.1111111..2..
    ...2.111.111..2..
    .132..11111..132.
    132....1.1....132
    ...11.11111.11...
    ...2.1111111..2..
    ...2.111.111..2..
    ...2.1111111..2..
    .132.111.111.132.
    132..1111111..132
    .....22111.22....
    .....2......2....
    .....2......2....
    .....2......2....
    .....2......2....
    .....2......2....
    ...111.....111...
    .1111.......1111.
''',
'''
    ...2...........2.
    ....2.........2..
    .....2.......2...
    ......2.....2....
    .......2...2.....
    ......11.11......
    .....1111111.....
    ....111311311.132
    .....1111111.132.
    .....111..11..2..
    ......11111...2..
    .......1.1....2..
    ...11.11111.11...
    ...2.111.111..132
    ...2.1111111.132.
    ...2.111.111..2..
    .132..11111...2..
    132....1.1....2..
    ...11.11111.11...
    ...2.1111111.....
    ...2.111.111.....
    ...2.1111111.....
    .132.111.111.....
    132..1111111.....
    .....22111.22....
    .....2......2....
    .....2......2....
    .....2......2....
    ...111......2....
    .1111.......2....
    ...........111...
    ............1111.
''',    
'''
    .....2.......2...
    ....2.........2..
    .....2.......2...
    ......2.....2....
    .......2...2.....
    ......11.11......
    .....1111111.....
    1323111311311....
    .132.1111111.....
    ...2.111..11.....
    ...2..11111......
    ...2...1.1.......
    ...11.11111.11...
    132..111.111..2..
    .132.1111111..2..
    ...2.111.111..2..
    ...2..11111..132.
    ...2...1.1....132
    ...11.11111.11...
    .....1111111..2..
    .....111.111..2..
    .....1111111..2..
    .....111.111.132.
    .....1111111..132
    .....22111.22....
    .....2......2....
    .....2......2....
    .....2......2....
    .....2.....111...
    .....2......1111.
    ...111...........
    .1111............
'''
],COLORS_BUG)

MOUTH = BitImage([
    '''
    11..11
    1....1
    11..11
    1....1
    111111
    ..11..
''',
'''
    .1111.
    .1..1.
    .1111.
    11..11
    111111
    ..11..
''',
'''
   .11111 
   .1.1.1
   11....
   11....
   .1.1.1
   .11111
''',       
'''
   .11...
   .11111
   11.1.1
   11.1.1
   .11111
   .11...
''',
'''
    ..11..
    111111
    1....1
    11..11
    1....1
    11..11
''',
''' 
    ..11..
    111111
    11..11
    .1111.
    .1..1.
    .1111.
''',
'''
   11111. 
   1.1.1.
   ....11
   ....11
   1.1.1.
   11111.
''',       
'''
   ...11.
   11111.
   1.1.11
   1.1.11
   11111.
   ...11.
'''



],COLORS_MOUTH)

CHARS = BitImage([
'''
    .111....
    1...1...
    1..11...
    1.1.1...
    11..1...
    1...1...
    .111....
    ........
    ........
''','''
    ..1.....
    .11.....
    ..1.....
    ..1.....
    ..1.....
    ..1.....
    .111....
    ........
    ........
''','''
    .111....
    1...1...
    ....1...
    ..11....
    .1......
    1.......
    11111...
    ........
    ........
''','''
    .111....
    1...1...
    ....1...
    ..11....
    ....1...
    1...1...
    .111....
    ........
    ........
''','''
    ...1....
    ..11....
    .1.1....
    11111...
    ...1....
    ...1....
    ...1....
    ........
    ........
''','''
    11111...
    1.......
    1.......
    1111....
    ....1...
    ....1...
    1111....
    ........
    ........
''','''
    .111....
    1...1...
    1.......
    1111....
    1...1...
    1...1...
    .111....
    ........
    ........
''','''
    11111...
    1...1...
    ...1....
    ...1....
    ..1.....
    ..1.....
    ..1.....
    ........
    ........
''','''
    .111....
    1...1...
    1...1...
    .111....
    1...1...
    1...1...
    .111....
    ........
    ........
''','''
    .111....
    1...1...
    1...1...
    .1111...
    ....1...
    1...1...
    .111....
    ........
    ........
''','''
    ..1.....
    .1.1....
    1...1...
    11111...
    1...1...
    1...1...
    1...1...
    ........
    ........
''','''
    1111....
    .1..1...
    .1..1...
    .111....
    .1..1...
    .1..1...
    1111....
    ........
    ........
''','''
    .111....
    1...1...
    1.......
    1.......
    1.......
    1...1...
    .111....
    ........
    ........
''','''
    1111....
    .1..1...
    .1..1...
    .1..1...
    .1..1...
    .1..1...
    1111....
    ........
    ........
''','''
    11111...
    1.......
    1.......
    1111....
    1.......
    1.......
    11111...
    ........
    ........
''','''
    11111...
    1.......
    1.......
    1111....
    1.......
    1.......
    1.......
    ........
    ........
''','''
    .111....
    1...1...
    1.......
    1.111...
    1...1...
    1...1...
    .111....
    ........
    ........
''','''
    1...1...
    1...1...
    1...1...
    11111...
    1...1...
    1...1...
    1...1...
    ........
    ........
''','''
    11111...
    ..1.....
    ..1.....
    ..1.....
    ..1.....
    ..1.....
    11111...
    ........
    ........
''','''
    ..111...
    ...1....
    ...1....
    ...1....
    ...1....
    1..1....
    .11.....
    ........
    ........
''','''
    1...1...
    1..1....
    1.1.....
    11......
    1.1.....
    1..1....
    1...1...
    ........
    ........
''','''
    1.......
    1.......
    1.......
    1.......
    1.......
    1.......
    1111....
    ........
    ........
''','''
    1...1...
    11.11...
    1.1.1...
    1.1.1...
    1...1...
    1...1...
    1...1...
    ........
    ........
''','''
    1...1...
    11..1...
    11..1...
    1.1.1...
    1..11...
    1..11...
    1...1...
    ........
    ........
''','''
    .111....
    1...1...
    1...1...
    1...1...
    1...1...
    1...1...
    .111....
    ........
    ........
''','''
    1111....
    1...1...
    1...1...
    1111....
    1.......
    1.......
    1.......
    ........
    ........
''','''
    .111....
    1...1...
    1...1...
    1...1...
    1.1.1...
    1..1....
    .11.1...
    ........
    ........
''','''
    1111....
    1...1...
    1...1...
    1111....
    1.1.....
    1..1....
    1...1...
    ........
    ........
''','''
    .111....
    1...1...
    1.......
    .111....
    ....1...
    1...1...
    .111....
    ........
    ........
''','''
    11111...
    1.1.1...
    ..1.....
    ..1.....
    ..1.....
    ..1.....
    ..1.....
    ........
    ........
''','''
    1...1...
    1...1...
    1...1...
    1...1...
    1...1...
    1...1...
    .111....
    ........
    ........
''','''
    1...1...
    1...1...
    1...1...
    1...1...
    .1.1....
    .1.1....
    ..1.....
    ........
    ........
''','''
    1...1...
    1...1...
    1...1...
    1...1...
    1.1.1...
    1.1.1...
    .1.1....
    ........
    ........
''','''
    1...1...
    1...1...
    .1.1....
    ..1.....
    .1.1....
    1...1...
    1...1...
    ........
    ........
''','''
    1...1...
    1...1...
    .1.1....
    ..1.....
    ..1.....
    ..1.....
    ..1.....
    ........
    ........
''','''
    11111...
    ....1...
    ...1....
    ..1.....
    .1......
    1.......
    11111...
    ........
    ........
''','''
    ........
    ........
    .11.....
    ...1....
    .111....
    1..1....
    .11.1...
    ........
    ........
''','''
    1.......
    1.......
    1111....
    1...1...
    1...1...
    1...1...
    1111....
    ........
    ........
''','''
    ........
    ........
    .111....
    1...1...
    1.......
    1...1...
    .111....
    ........
    ........
''','''
    ....1...
    ....1...
    .1111...
    1...1...
    1...1...
    1...1...
    .1111...
    ........
    ........
''','''
    ........
    ........
    .111....
    1...1...
    11111...
    1.......
    .111....
    ........
    ........
''','''
    ..1.....
    .1.1....
    .1......
    111.....
    .1......
    .1......
    .1......
    ........
    ........
''','''
    ........
    ........
    .111....
    1...1...
    1...1...
    .1111...
    ....1...
    1...1...
    .111....
''','''
    1.......
    1.......
    1.11....
    11..1...
    1...1...
    1...1...
    1...1...
    ........
    ........
''','''
    ..1.....
    ........
    .11.....
    ..1.....
    ..1.....
    ..1.....
    .111....
    ........
    ........
''','''
    ..1.....
    ........
    .11.....
    ..1.....
    ..1.....
    ..1.....
    ..1.....
    1.1.....
    .1......
''','''
    1.......
    1.......
    1..1....
    1.1.....
    11......
    1.1.....
    1..1....
    ........
    ........
''','''
    .11.....
    ..1.....
    ..1.....
    ..1.....
    ..1.....
    ..1.....
    .111....
    ........
    ........
''','''
    ........
    ........
    11.1....
    1.1.1...
    1.1.1...
    1.1.1...
    1.1.1...
    ........
    ........
''','''
    ........
    ........
    1.11....
    11..1...
    1...1...
    1...1...
    1...1...
    ........
    ........
''','''
    ........
    ........
    .111....
    1...1...
    1...1...
    1...1...
    .111....
    ........
    ........
''','''
    ........
    ........
    1.11....
    11..1...
    1...1...
    1...1...
    1111....
    1.......
    1.......
''','''
    ........
    ........
    .11.1...
    1..11...
    1...1...
    1..11...
    .11.1...
    ....1...
    ....1...
''','''
    ........
    ........
    1.11....
    11..1...
    1.......
    1.......
    1.......
    ........
    ........
''','''
    ........
    ........
    .111....
    1.......
    .111....
    ....1...
    .111....
    ........
    ........
''','''
    .1......
    .1......
    111.....
    .1......
    .1......
    .1.1....
    ..1.....
    ........
    ........
''','''
    ........
    ........
    1...1...
    1...1...
    1...1...
    1..11...
    .11.1...
    ........
    ........
''','''
    ........
    ........
    1...1...
    1...1...
    1...1...
    .1.1....
    ..1.....
    ........
    ........
''','''
    ........
    ........
    1...1...
    1.1.1...
    1.1.1...
    1.1.1...
    .1.1....
    ........
    ........
''','''
    ........
    ........
    1...1...
    .1.1....
    ..1.....
    .1.1....
    1...1...
    ........
    ........
''','''
    ........
    ........
    1...1...
    1...1...
    1...1...
    .1111...
    ....1...
    ....1...
    .111....
''','''
    ........
    ........
    11111...
    ...1....
    ..1.....
    .1......
    11111...
    ........
    ........
''','''
    ........
    ........
    ........
    ........
    ........
    ........
    ........
    ........
    ........
''','''
    ..1.....
    ..1.....
    ..1.....
    ..1.....
    ..1.....
    ........
    ..1.....
    ........
    ........
''','''
    ........
    ........
    ........
    11111...
    ........
    ........
    ........
    ........
    ........
''','''
    ........
    ........
    ........
    ........
    ........
    ..1.....
    ..1.....
    ........
    ........
''','''
    ........
    ........
    ..1.....
    ........
    ........
    ..1.....
    ........
    ........
    ........
''','''
    ..1.....
    ..1.....
    .1......
    ........
    ........
    ........
    ........
    ........
    ........
'''
])

order = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz !-.:'"
CHARS.CHAR_MAP = {}
for i in range(len(order)):
    CHARS.CHAR_MAP[order[i]] = CHARS._images[i]
    
