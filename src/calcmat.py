#!/bin/env python3

'''
  Calcul et affichage de la matrice des coefficients de la courbe de Bezier
'''

import math
import numpy as np

# generateur équivalent à range(n+1), pratique pour \sum_{i=0}^{n}
def mathRange(n: int) -> int:
  num: int = 0
  while num <= n:
    yield num
    num += 1

_nmax = 11 # nombre de points max (n+1)

for nP1 in range(2, _nmax+1):
  arr: np.ndarray = np.zeros((nP1, nP1), dtype=np.int32)
  n: int = nP1-1
  fn: int = math.factorial(n)
  for i in mathRange(n):
    fi: int = math.factorial(i)
    assert(fn % fi == 0) # normalement évident
    fn_i: int = fn//fi
    for k in mathRange(n):
      if k >= i:
        s: int = (-1)**(k-i)
        fki: int = math.factorial(k-i)
        fnk: int = math.factorial(n-k)
        fd: int = fki*fnk
        assert(fn_i % fd == 0) # moins évident
        arr[k, i]: int = s*(fn_i//fd) # k: ligne, i: colonne
  print(f'pour {nP1} points :')
  print(f'{arr}')
  print()