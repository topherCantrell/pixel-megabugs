
import unittest
import image

class TestImage(unittest.TestCase):
    
    def test_one_image(self):
        test = '''
        1.
        .1'''
        
        res = image.from_string(test)
        exp = [[1, 0], [0, 1]]
        self.assertTrue(res==exp)
        
    def test_two_images(self):
        test = ['''
        1.
        .1
        ''',
        '''
        2.
        .2
        '''
        ]
        
        res = image.from_string(test)
        exp = [[[1, 0], [0, 1]],[[2,0],[0,2]]]
        self.assertTrue(res==exp)
        
    def test_one_as_array(self):
        test = ['''
        1.
        .1''']
        
        res = image.from_string(test)
        exp = [[[1, 0], [0, 1]]]
        self.assertTrue(res==exp)
        
    def test_multi(self):
        test = '''
        1.  2.
        .1  .2
        '''
        res = image.from_string(test)
        exp = [[[1, 0], [0, 1]],[[2,0],[0,2]]]
        self.assertTrue(res==exp)
        
    def test_complex_multi(self):
        test = ['''
        1.  2.
        .1  .2
        ''',
        '''
        3.
        .3
        ''']
        res = image.from_string(test)
        exp = [[[1, 0], [0, 1]], [[2, 0], [0, 2]], [[3, 0], [0, 3]]]
        self.assertTrue(res==exp)
        
    def test_simple_dict(self):
        test = {
        'A': 
        '''
        1.
        .1
        ''',
        'B':
        '''
        2.
        .2
        '''        
        }
        res = image.from_string(test)
        exp = {'A': [[1, 0],[0,1]], 'B': [[2, 0],[0,2]]}
        self.assertTrue(res==exp)

    def test_compound_dict(self):
        test = {
            'A' :
        '''
        1. 2.
        .1 .2
        '''
        }
        res = image.from_string(test)
        exp = {'A':[[[1, 0], [0, 1]],[[2,0],[0,2]]]}        
        self.assertTrue(res==exp)
    
"""

test4 = {
    'A': 
    '''
    1.
    .1
    ''',
    'B':
    '''
    2.
    .2
    '''
    
    }

test2 = from_string(test2)
print(test2)
"""