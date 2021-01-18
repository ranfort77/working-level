# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 04:43:03 2021

@author: ran
"""

def read_xyz(xyzfile):
    """입력된 xyzfile 에서 원소기호와 각좌표를 추출
    return: list 리턴
    """
    with open(xyzfile) as f:
        symbols = []
        coords = []
        for line in f:
            line = line.strip().split()
            symbols.append(line[0])
            coords.append([float(e) for e in line[1:]])
    return symbols, coords

def read_mol(molfile):
    """입력된 molfile 에서 원소기호와 좌표를 추출
    retrun: list 리턴
    """    
    with open(molfile)as f:
        symbols = []
        coords = []
        for line in f:
            if 'V2000' in line:
                n = int(line[0:3])
                for nn in range(n):
                    line = next(f).strip().split()
                    symbols.append(line[3])
                    coords.append([float(e) for e in line[:3]])
        return symbols, coords            