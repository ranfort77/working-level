# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 04:47:00 2021

@author: ran
"""

import re
import io
import unittest
from parse import Parser
from parse import XYZ_ATOM


CH4_MOL = """

Created by GaussView 5.0.9
  5  4  0  0  0  0  0  0  0   999 V2000 
   -0.0346    0.0808    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.3220   -0.9280    0.0000 H   0  0  0  0  0  0  0  0  0  0  0  0
    0.3220    0.5852    0.8737 H   0  0  0  0  0  0  0  0  0  0  0  0
    0.3220    0.5852   -0.8737 H   0  0  0  0  0  0  0  0  0  0  0  0
   -1.1046    0.0808    0.0000 H   0  0  0  0  0  0  0  0  0  0  0  0
  1  2  1  0  0  0  0
  1  3  1  0  0  0  0
  1  4  1  0  0  0  0
  1  5  1  0  0  0  0

"""

H2O_XYZ = """O  0.0     0.0652  0.0
H  0.7578 -0.54484 0.0
H -0.7578 -0.54484 0.0

"""

class TestParser(unittest.TestCase):            
    def test_read_molfile(self):
        molecule = Parser().molfile(io.StringIO(CH4_MOL))
        self.assertEqual(molecule.symbols, ['C', 'H', 'H', 'H', 'H'])
        self.assertEqual(molecule.coords, 
                         [[-0.0346,  0.0808,  0.0000],
                          [ 0.3220, -0.9280,  0.0000],
                          [ 0.3220,  0.5852,  0.8737],
                          [ 0.3220,  0.5852, -0.8737],
                          [-1.1046,  0.0808,  0.0000]])
        
    def test_read_xyzfile(self):
        molecule = Parser().xyzfile(io.StringIO(H2O_XYZ))
        self.assertEqual(molecule.symbols, ['O', 'H', 'H'])
        self.assertEqual(molecule.coords, [[ 0.0,     0.0652,  0.0],
                                           [ 0.7578, -0.54484, 0.0],
                                           [-0.7578, -0.54484, 0.0]])             

    def test_regex_xyz_atom(self):
        self.assertRegex('H  0.7578 -0.54484 0.0', XYZ_ATOM)

        