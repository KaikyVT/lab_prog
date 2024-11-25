'''Crie dois vetores a=[1,2,3] e b=[4,5,6]. Calcule o produto escalar e o produto
externo (a⊗b)'''

import numpy as np

# Definindo os vetores
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Produto escalar
prod_esc = np.dot(a, b)
print(prod_esc)

# Produto externo
prod_ext = np.outer(a, b)
print(prod_ext)