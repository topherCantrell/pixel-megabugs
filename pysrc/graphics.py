import image
import copy

'''
Color Palette:
  00     Transparent  
  01-0F  Misc
     01     Dot
     02     Crumb
     03     Lens border
     04     Bug as dot
     05..08 Splash text colors
  10-1F  Maze wall
  20-2F  Mouth
  30-3F  Bug color
'''

# Constants to reference the palette
COLOR_DOT = 1
COLOR_CRUMB = 2
COLOR_LENS_BORDER = 3
COLOR_BUG_AS_DOT = 4
COLOR_SCORE = COLOR_LENS_BORDER
COLORS_SPLASH_TEXT = 5 # 5,6,7,8
#
COLORS_MAZE_WALL = 0x10 # Future expansion: different kinds of walls
COLORS_MOUTH = 0x20 # Future expansion: colorful magnified mouth
COLORS_BUG = 0x30 

# Start with a black palette
COLOR_PALETTE = [[0,0,0]]*256

# Add the individual colors
COLOR_PALETTE[COLOR_DOT]            = [0x00, 0xFF, 0x00] # Green
COLOR_PALETTE[COLOR_CRUMB]          = [0x96, 0x4B, 0x00] # Brown
COLOR_PALETTE[COLOR_LENS_BORDER]    = [0xFF, 0xFF, 0xFF] # White
COLOR_PALETTE[COLOR_BUG_AS_DOT]     = [0x00, 0x00, 0xFF] # Blue

COLOR_PALETTE[COLORS_SPLASH_TEXT+0] = [0xFF, 0x00, 0x00] # Red
COLOR_PALETTE[COLORS_SPLASH_TEXT+1] = [0x00, 0xFF, 0x00] # Green
COLOR_PALETTE[COLORS_SPLASH_TEXT+2] = [0x00, 0x00, 0xFF] # Blue
COLOR_PALETTE[COLORS_SPLASH_TEXT+3] = [0xFF, 0xFF, 0xFF] # White

COLOR_PALETTE[COLORS_MAZE_WALL + 0] = [0xFF, 0x00, 0x00] # Red
COLOR_PALETTE[COLORS_MOUTH + 0]     = [0xFF, 0xFF, 0xFF] # White
COLOR_PALETTE[COLORS_BUG + 0]       = [0x00, 0x00, 0xFF] # Blue
COLOR_PALETTE[COLORS_BUG + 1]       = [0x00, 0xFF, 0xFF] # Cyan
COLOR_PALETTE[COLORS_BUG + 2]       = [0x80, 0x00, 0xFF] # Purple

# Magnified colors start off the same as unmagnified
for i in range(128):
    COLOR_PALETTE[i+128] = COLOR_PALETTE[i]
    
# For demonstration of switching the color palette
COLOR_STYLES = [
    COLOR_PALETTE, # The default
]

# Invisible walls on magnifier
invs1 = copy.deepcopy(COLOR_PALETTE)
invs1[COLORS_MAZE_WALL + 0] = [0x00,0x00,0x00]
COLOR_STYLES.append(invs1)

# Invisible walls outside magnifier
invs2 = copy.deepcopy(COLOR_PALETTE)
invs2[COLORS_MAZE_WALL + 0 + 128] = [0x00,0x00,0x00]
COLOR_STYLES.append(invs2)

# Black and white unmagnified
bw = copy.deepcopy(COLOR_PALETTE)
bw[COLOR_DOT]            = [0xA0, 0xA0, 0xA0]
bw[COLOR_CRUMB]          = [0x20, 0x20, 0x20]
bw[COLOR_LENS_BORDER]    = [0xFF, 0xFF, 0xFF]
bw[COLOR_BUG_AS_DOT]     = [0xFF, 0xFF, 0xFF]
bw[COLORS_MAZE_WALL + 0] = [0xC0, 0xC0, 0xC0]
bw[COLORS_MOUTH + 0]     = [0xFF, 0xFF, 0xFF]
bw[COLORS_BUG + 0]       = [0x40, 0x40, 0x40]
bw[COLORS_BUG + 1]       = [0x60, 0x60, 0x60]
bw[COLORS_BUG + 2]       = [0x80, 0x80, 0x80]
COLOR_STYLES.append(bw)

# Graphics images

LITTLE_BUG = [    
    #UP
    [
        ''' 
            1.....  .....1
            .1..1.  .1..1.
            .222.1  1222..
            1222..  .222.1
            .1..1.  .1..1.
            .....1  1.....
        '''
    ],    
    #RIGHT
    [
        '''
            ..1..1  1..1..   
            .1..1.  .1..1.
            .222..  .222..
            .222..  .222..
            .1..1.  .1..1.
            1..1..  ..1..1    
        '''
    ],    
    #DOWN
    [
        '''
            1.....  .....1
            .1..1.  .1..1.
            .222.1  1222..
            1222..  .222.1
            .1..1.  .1..1.
            .....1  1.....
        '''
    ],    
    #LEFT
    [
        '''
            ..1..1  1..1..    
            .1..1.  .1..1. 
            .222..  .222..
            .222..  .222..
            .1..1.  .1..1.
            1..1..  ..1..1     
        '''
    ]    
]
LITTLE_BUG = image.from_string(LITTLE_BUG,COLORS_BUG)

BIG_BUG = {
    'standing' : 
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
'dancing' : 
'''
    ...2...........2.  .....2.......2...
    ....2.........2..  ....2.........2..
    .....2.......2...  .....2.......2...
    ......2.....2....  ......2.....2....
    .......2...2.....  .......2...2.....
    ......11.11......  ......11.11......
    .....1111111.....  .....1111111.....
    ....111311311.132  1323111311311....
    .....1111111.132.  .132.1111111.....
    .....111..11..2..  ...2.111..11.....
    ......11111...2..  ...2..11111......
    .......1.1....2..  ...2...1.1.......
    ...11.11111.11...  ...11.11111.11...
    ...2.111.111..132  132..111.111..2..
    ...2.1111111.132.  .132.1111111..2..
    ...2.111.111..2..  ...2.111.111..2..
    .132..11111...2..  ...2..11111..132.
    132....1.1....2..  ...2...1.1....132
    ...11.11111.11...  ...11.11111.11...
    ...2.1111111.....  .....1111111..2..
    ...2.111.111.....  .....111.111..2..
    ...2.1111111.....  .....1111111..2..
    .132.111.111.....  .....111.111.132.
    132..1111111.....  .....1111111..132
    .....22111.22....  .....22111.22....
    .....2......2....  .....2......2....
    .....2......2....  .....2......2....
    .....2......2....  .....2......2....
    ...111......2....  .....2.....111...
    .1111.......2....  .....2......1111.
    ...........111...  ...111...........
    ............1111.  .1111...........
'''
}
BIG_BUG = image.from_string(BIG_BUG,COLORS_BUG)

MOUTH = [
    [
        '''
            11..11   .1111.
            1....1   .1..1.
            11..11   .1111.
            1....1   11..11
            111111   111111
            ..11..   ..11..
        '''
    ],
    [
        '''
           .11111   .11...
           .1.1.1   .11111
           11....   11.1.1
           11....   11.1.1
           .1.1.1   .11111
           .11111   .11...
        '''
    ],
    [
        '''
            ..11..   ..11..
            111111   111111
            1....1   11..11
            11..11   .1111.
            1....1   .1..1.
            11..11   .1111.
        '''
    ],
    [
        '''
           11111.   ...11.
           1.1.1.   11111.
           ....11   1.1.11
           ....11   1.1.11
           1.1.1.   11111.
           11111.   ...11.
        '''
    ]
]
MOUTH = image.from_string(MOUTH,COLORS_MOUTH)


CHARS = {
    '0|1|2|3|4|5|6|7|8|9|A|B|C|D|E|F' : '''
        .111.. ..1... .111.. .111.. ...1.. 11111. .111.. 11111. .111.. .111.. ..1... 1111.. .111.. 1111.. 11111. 11111.
        1...1. .11... 1...1. 1...1. ..11.. 1..... 1...1. 1...1. 1...1. 1...1. .1.1.. .1..1. 1...1. .1..1. 1..... 1.....
        1..11. ..1... ....1. ....1. .1.1.. 1..... 1..... ...1.. 1...1. 1...1. 1...1. .1..1. 1..... .1..1. 1..... 1.....
        1.1.1. ..1... ..11.. ..11.. 11111. 1111.. 1111.. ...1.. .111.. .1111. 11111. .111.. 1..... .1..1. 1111.. 1111..
        11..1. ..1... .1.... ....1. ...1.. ....1. 1...1. ..1... 1...1. ....1. 1...1. .1..1. 1..... .1..1. 1..... 1.....
        1...1. ..1... 1..... 1...1. ...1.. ....1. 1...1. ..1... 1...1. 1...1. 1...1. .1..1. 1...1. .1..1. 1..... 1.....
        .111.. .111.. 11111. .111.. ...1.. 1111.. .111.. ..1... .111.. .111.. 1...1. 1111.. .111.. 1111.. 11111. 1.....
        ...... ...... ...... ...... ...... ...... ...... ...... ...... ...... ...... ...... ...... ...... ...... ......
        ...... ...... ...... ...... ...... ...... ...... ...... ...... ...... ...... ...... ...... ...... ...... ......''',
    'G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V':'''
        .111.. 1...1. 11111. ..111. 1...1. 1..... 1...1. 1...1. .111.. 1111.. .111.. 1111.. .111.. 11111. 1...1. 1...1.
        1...1. 1...1. ..1... ...1.. 1..1.. 1..... 11.11. 11..1. 1...1. 1...1. 1...1. 1...1. 1...1. 1.1.1. 1...1. 1...1.
        1..... 1...1. ..1... ...1.. 1.1... 1..... 1.1.1. 11..1. 1...1. 1...1. 1...1. 1...1. 1..... ..1... 1...1. 1...1.
        1.111. 11111. ..1... ...1.. 11.... 1..... 1.1.1. 1.1.1. 1...1. 1111.. 1...1. 1111.. .111.. ..1... 1...1. 1...1.
        1...1. 1...1. ..1... ...1.. 1.1... 1..... 1...1. 1..11. 1...1. 1..... 1.1.1. 1.1... ....1. ..1... 1...1. .1.1..
        1...1. 1...1. ..1... 1..1.. 1..1.. 1..... 1...1. 1..11. 1...1. 1..... 1..1.. 1..1.. 1...1. ..1... 1...1. .1.1..
        .111.. 1...1. 11111. .11... 1...1. 1111.. 1...1. 1...1. .111.. 1..... .11.1. 1...1. .111.. ..1... .111.. ..1...
        ...... ...... ...... ...... ...... ...... ...... ...... ...... ...... ...... ...... ...... ...... ...... ......
        ...... ...... ...... ...... ...... ...... ...... ...... ...... ...... ...... ...... ...... ...... ...... ......''',
    'W|X|Y|Z|a|b|c|d|e|f|g|h|i|j|k|l':'''
        1...1. 1...1. 1...1. 11111. ...... 1..... ...... ....1. ...... ..1... ...... 1..... ..1... ..1... 1..... .11...
        1...1. 1...1. 1...1. ....1. ...... 1..... ...... ....1. ...... .1.1.. ...... 1..... ...... ...... 1..... ..1...
        1...1. .1.1.. .1.1.. ...1.. .11... 1111.. .111.. .1111. .111.. .1.... .111.. 1.11.. .11... .11... 1..1.. ..1...
        1...1. ..1... ..1... ..1... ...1.. 1...1. 1...1. 1...1. 1...1. 111... 1...1. 11..1. ..1... ..1... 1.1... ..1...
        1.1.1. .1.1.. ..1... .1.... .111.. 1...1. 1..... 1...1. 11111. .1.... 1...1. 1...1. ..1... ..1... 11.... ..1...
        1.1.1. 1...1. ..1... 1..... 1..1.. 1...1. 1...1. 1...1. 1..... .1.... .1111. 1...1. ..1... ..1... 1.1... ..1...
        .1.1.. 1...1. ..1... 11111. .11.1. 1111.. .111.. .1111. .111.. .1.... ....1. 1...1. .111.. ..1... 1..1.. .111..
        ...... ...... ...... ...... ...... ...... ...... ...... ...... ...... 1...1. ...... ...... 1.1... ...... ......
        ...... ...... ...... ...... ...... ...... ...... ...... ...... ...... .111.. ...... ...... .1.... ...... ......''',
    'm|n|o|p|q|r|s|t|u|v|w|x|y|z| |!':'''
        ...... ...... ...... ...... ...... ...... ...... .1.... ...... ...... ...... ...... ...... ...... ...... ..1...
        ...... ...... ...... ...... ...... ...... ...... .1.... ...... ...... ...... ...... ...... ...... ...... ..1...
        11.1.. 1.11.. .111.. 1.11.. .11.1. 1.11.. .111.. 111... 1...1. 1...1. 1...1. 1...1. 1...1. 11111. ...... ..1...
        1.1.1. 11..1. 1...1. 11..1. 1..11. 11..1. 1..... .1.... 1...1. 1...1. 1.1.1. .1.1.. 1...1. ...1.. ...... ..1...
        1.1.1. 1...1. 1...1. 1...1. 1...1. 1..... .111.. .1.... 1...1. 1...1. 1.1.1. ..1... 1...1. ..1... ...... ..1...
        1.1.1. 1...1. 1...1. 1...1. 1..11. 1..... ....1. .1.1.. 1..11. .1.1.. 1.1.1. .1.1.. .1111. .1.... ...... ......
        1.1.1. 1...1. .111.. 1111.. .11.1. 1..... .111.. ..1... .11.1. ..1... .1.1.. 1...1. ....1. 11111. ...... ..1...
        ...... ...... ...... 1..... ....1. ...... ...... ...... ...... ...... ...... ...... ....1. ...... ...... ......
        ...... ...... ...... 1..... ....1. ...... ...... ...... ...... ...... ...... ...... .111.. ...... ...... ......''',
    "-|.|:|'":'''
        ...... ...... ...... ..1...
        ...... ...... ...... ..1...
        ...... ...... ..1... .1....
        11111. ...... ...... ......
        ...... ...... ...... ......
        ...... ..1... ..1... ......
        ...... ..1... ...... ......
        ...... ...... ...... ......
        ...... ...... ...... ......'''
}
CHARS = image.from_string(CHARS)
