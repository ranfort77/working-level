# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 04:47:00 2021

@author: ran
"""

import unittest
from mmoi_calc import ctab
from parse import Molecule, Parser, XYZ_ATOM


class TestMolecule(unittest.TestCase):
    """parse.Molecule class 테스트"""

    def setUp(self):
        with open('tests/fixture/ch4.mol') as lines:
            ctab_molecule = ctab.Parser().molfile(lines)
            self.molecule = Molecule(ctab_molecule.atoms)

    def test_implicit_init(self):
        self.assertAlmostEqual(self.molecule.mass, 16.04246)

    def test_added_attributes(self):
        self.assertAlmostEqual(self.molecule.masses,
                               [12.0107, 1.00794, 1.00794, 1.00794, 1.00794])
        self.assertAlmostEqual(self.molecule.atmrads,
                               [0.91, 0.79, 0.79, 0.79, 0.79])
        self.assertAlmostEqual(self.molecule.covrads,
                               [0.77, 0.32, 0.32, 0.32, 0.32])


class TestParser(unittest.TestCase):
    def test_invalid_fileext(self):
        with self.assertRaises(ValueError):
            Parser('ch4.txt')

    def test_molfile(self):
        molecule = Parser('tests/fixture/ch4.mol').get_molecule()
        self.assertEqual(molecule.symbols, ['C', 'H', 'H', 'H', 'H'])
        self.assertEqual(molecule.coords,
                         [[-0.0346,  0.0808,  0.0000],
                          [0.3220, -0.9280,  0.0000],
                          [0.3220,  0.5852,  0.8737],
                          [0.3220,  0.5852, -0.8737],
                          [-1.1046,  0.0808,  0.0000]])

    def test_xyzfile(self):
        molecule = Parser('tests/fixture/h2o.xyz').get_molecule()
        self.assertEqual(molecule.symbols, ['O', 'H', 'H'])
        self.assertEqual(molecule.coords, [[0.0,     0.0652,  0.0],
                                           [0.7578, -0.54484, 0.0],
                                           [-0.7578, -0.54484, 0.0]])

    def test_regex_xyz_atom(self):
        self.assertRegex('H  0.7578 -0.54484 0.0', XYZ_ATOM)
