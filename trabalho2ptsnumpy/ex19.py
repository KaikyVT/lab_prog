'''Crie uma matriz 3×33 times 33×3 com números de 1 a 9. Subtraia de cada
linha o valor da média dessa linha usando o conceito de broadcasting.
'''

import numpy as np

# Criando matrizes
matriz1 = np.random.randint(1, 10, (3, 33))
matriz2 = np.random.randint(1, 10, (33, 3))

# Calculando a média de cada linha da matriz1
media_linhas_matriz1 = np.mean(matriz1, axis=1, keepdims=True)

# Subtraindo a média com a matriz
resultado_matriz1 = matriz1 - media_linhas_matriz1

print("Matriz 3x33 original:")
print(matriz1)
print("\nMédia de cada linha da matriz 3x33:")
print(media_linhas_matriz1)
print("\nResultado (Matriz 3x33 com a média subtraída de cada linha):")
print(resultado_matriz1)

