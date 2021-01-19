# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 04:43:03 2021

@author: ran
"""

import os
import re
from mmoi_calc import ctab, elements

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


class Molecule(ctab.Molecule):
    """ctab.Molecule 에서 attributes 추가

    ctab.Molecule attributes:
        atoms: 분자 내 모든 elements의 ctab.Atom 클래스 인스턴스들
        mass: (float) molecular mass
        center_of_mass()
        inertia(principal=True, moments_only=True)

    추가 attributes:
        symbols: (list)
        coords: (list of lists)
        masses: (list) 분자 내 모든 elements의 mass
        atmrads: (list) Atomic radius in Angstrom
        covrad: (list) Covalent radius in Angstrom
    """
    @property
    def symbols(self):
        return [a.symbol for a in self.atoms]

    @property
    def coords(self):
        return [list(a.coords) for a in self.atoms]

    @property
    def masses(self):
        return [elements.ELEMENTS[a.symbol].mass for a in self.atoms]

    @property
    def atmrads(self):
        return [elements.ELEMENTS[a.symbol].atmrad for a in self.atoms]

    @property
    def covrads(self):
        return [elements.ELEMENTS[a.symbol].covrad for a in self.atoms]


class Parser(ctab.Parser):
    """.mol, .xyz 정보를 읽고 Molecule 객체 리턴

    Usage:
        >>> molecule = Parser('ch4.mol').get_molecule()
        >>> print(molecule.mass)
        >>> print(molecule.symbols)
        >>> print(molecule.coords)
    """

    def __init__(self, filename):
        self.filename = filename
        self.ext = os.path.splitext(filename)[1]
        if self.ext not in ('.mol', '.xyz'):
            raise ValueError('.mol 또는 .xyz 형식파일만 지원')

    def get_molecule(self):
        with open(self.filename) as lines:
            if self.ext == '.mol':
                return Molecule(super().molfile(lines).atoms)
            elif self.ext == '.xyz':
                return self.xyzfile(lines)

    def xyzfile(self, lines):
        atoms = []
        for line in lines:
            atom = XYZ_ATOM.match(line)
            if not atom:
                break
            else:
                atoms.append(ctab.Atom(atom))
        return Molecule(atoms)


if __name__ == '__main__':
    # Usage
    m = Parser('tests/fixture/ch4.mol').get_molecule()

    # ctab.Molecule에 있던 attributes
    print('''
          __str__ : {}
          atoms   : {}
          mass    : {}
          c.o.m   : {}
          inertia : {}
          inertia(moments_only=false): {}
          '''.format(m, m.atoms, m.mass,
                     m.center_of_mass(),
                     m.inertia(),
                     m.inertia(moments_only=False)))

    # 추가한 attributes
    print('''
          symbols : {}
          coords  : {}
          masses  : {}
          atmrads : {}
          covrads : {}
          '''.format(m.symbols, m.coords, m.masses,
                     m.atmrads,
                     m.covrads))
