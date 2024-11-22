'''Crie um array com os números inteiros de 0 a 20. Converta esse array para o
tipo de dado float e exiba o resultado'''

import numpy as np

# Setando uma matriz padrão
matriz = np.arange(0, 21)
print(matriz)

# Transformando a matriz em float
matrizflt = matriz.astype(float)
print(matrizflt)