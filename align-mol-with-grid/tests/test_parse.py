# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 04:47:00 2021

@author: ran
"""

import unittest
import parse

class TestParse(unittest.TestCase):
    
    def setUp(self):
        self.xyz = 'tests/fixture/h2o1.xyz'
        self.mol = 'tests/fixture/ch4.mol'
    
    def test_read_xyz(self):
        symbols, coords = parse.read_xyz(self.xyz)
        self.assertEqual(symbols, ['O', 'H', 'H'])
        self.assertEqual(coords, [[ 0.0,     0.0652,  0.0],
                                  [ 0.7578, -0.54484, 0.0],
                                  [-0.7578, -0.54484, 0.0]])
        
    def test_read_mol(self):
        symbols, coords = parse.read_mol(self.mol)
        self.assertEqual(symbols, ['C', 'H', 'H', 'H', 'H'])
        self.assertEqual(coords, [[-0.0346,  0.0808,  0.0000],
                                  [ 0.3220, -0.9280,  0.0000],
                                  [ 0.3220,  0.5852,  0.8737],
                                  [ 0.3220,  0.5852, -0.8737],
                                  [-1.1046,  0.0808,  0.0000]])
        

        