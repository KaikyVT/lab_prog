'''Crie uma matriz 4x4 preenchida com números de 1 a 16. Obtenha a
transposta dessa matriz e multiplique a matriz original pela transposta.'''

import numpy as np

# Criando a matriz e sua transposta
matriz = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
transposta = np.transpose(matriz)

# Printando para visualizar
print(f'Matriz: \n{matriz}')
print(f'\nTransposta: \n{transposta}')

# Multiplicando matrizes
mult = np.matmul(matriz, transposta)

# Printando  o resultado
print(f'\nMultiplicação:\n{mult}')