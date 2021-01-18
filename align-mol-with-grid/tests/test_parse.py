# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 04:47:00 2021

@author: ran
"""

import unittest
from parse import Parser, XYZ_ATOM


class TestParser(unittest.TestCase):    
    def test_init(self):
        with self.assertRaises(ValueError):
            Parser('ch4.txt')
        
    def test_molfile(self):
        molecule = Parser('tests/fixture/ch4.mol').get_molecule()
        self.assertEqual(molecule.symbols, ['C', 'H', 'H', 'H', 'H'])
        self.assertEqual(molecule.coords, 
                         [[-0.0346,  0.0808,  0.0000],
                          [ 0.3220, -0.9280,  0.0000],
                          [ 0.3220,  0.5852,  0.8737],
                          [ 0.3220,  0.5852, -0.8737],
                          [-1.1046,  0.0808,  0.0000]])
        
    def test_xyzfile(self):
        molecule = Parser('tests/fixture/h2o.xyz').get_molecule()
        self.assertEqual(molecule.symbols, ['O', 'H', 'H'])
        self.assertEqual(molecule.coords, [[ 0.0,     0.0652,  0.0],
                                           [ 0.7578, -0.54484, 0.0],
                                           [-0.7578, -0.54484, 0.0]])             

    def test_regex_xyz_atom(self):
        self.assertRegex('H  0.7578 -0.54484 0.0', XYZ_ATOM)

        