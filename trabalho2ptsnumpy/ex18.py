'''Crie um array representando os coeficientes do polinômio p(x) = x^3 - 4x^2 +
6x - 24. Use funções do NumPy para calcular:
a. As raízes do polinômio.
b. O valor de p(x) para x=2.
'''

import numpy as np

# Criando os coeficiente
coef = np.array([1, -4, 6, -24])

# Tirando as raízes
raizes = np.roots(coef)
print(raizes)

# Assumindo x = 2 para solucionar
x = 2
sol = np.polyval(coef, x)
print(sol)