'''Crie uma matriz quadrada 3x3 aleatória e calcule seus autovalores e
autovetores.
'''

import numpy as np
from numpy import linalg as la

# Criando a matriz 
matriz = np.array([[3, 0, 0], [0, 3, 2], [0, -1, 0]])

# Printando para visualizar
print(matriz)


# Setando autovalor e autovetor
autovalor, autovetor = la.eig(matriz)

# Printando resultados
print(f'Autovalor:\n {autovalor}')
print(f'\nAutovetor:\n {autovetor}')