# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 04:43:03 2021

@author: ran
"""

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
    def molfile(self, lines):
        molecule = super().molfile(lines)
        molecule.symbols = [a.symbol for a in molecule.atoms]
        molecule.coords = [list(a.coords) for a in molecule.atoms]
        return molecule
    
    def xyzfile(self, lines):
        atoms = []
        for line in lines:
            atom = XYZ_ATOM.match(line)
            if not atom:
                break
            else:
                atoms.append(ctab.Atom(atom))
        molecule = ctab.Molecule(atoms)
        molecule.symbols = [a.symbol for a in molecule.atoms]
        molecule.coords = [list(a.coords) for a in molecule.atoms]        
        return molecule
    

        