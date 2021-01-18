# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 04:43:03 2021

@author: ran
"""

import os
import re
from mmoi_calc import ctab

XYZ_ATOM = re.compile(r'''
                      (?P<symbol>[A-Z][a-z]?)
                      \s+
                      (?P<x>[+-]?\d+.\d+)
                      \s+
                      (?P<y>[+-]?\d+.\d+)
                      \s+
                      (?P<z>[+-]?\d+.\d+)
                      (?P<mass_diff>)  # dummy regex for __init__ of ctab.Atom
                      ''', re.VERBOSE)


class Parser(ctab.Parser):

    def __init__(self, filename):
        self.filename = filename
        self.ext = os.path.splitext(filename)[1]
        if self.ext not in ('.mol', '.xyz'):
            raise ValueError('.mol 또는 .xyz 형식파일만 지원')

    def get_molecule(self):
        with open(self.filename) as lines:
            if self.ext == '.mol':
                molecule = super().molfile(lines)
            elif self.ext == '.xyz':
                molecule = self._xyzfile(lines)
        molecule.symbols = [a.symbol for a in molecule.atoms]
        molecule.coords = [list(a.coords) for a in molecule.atoms]
        return molecule

    def _xyzfile(self, lines):
        atoms = []
        for line in lines:
            atom = XYZ_ATOM.match(line)
            if not atom:
                break
            else:
                atoms.append(ctab.Atom(atom))
        molecule = ctab.Molecule(atoms)
        return molecule


if __name__ == '__main__':
    # Usage
    m = Parser('tests/fixture/ch4.mol').get_molecule()
    print('''
          __str__ : {}
          symbols : {}
          coords  : {}
          c.o.m   : {}
          inertia : {}
          inertia(moments_only=false): {}
          '''.format(m, m.symbols, m.coords, m.center_of_mass(),
                     m.inertia(),
                     m.inertia(moments_only=False)
                     ))
