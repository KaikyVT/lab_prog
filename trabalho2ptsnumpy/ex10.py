'''Gere um conjunto de dados simulando as alturas (em cm) de 100 pessoas,
usando uma distribuição normal com média 170 e desvio padrão 10. Depois
calcule:

a. O percentil 25, 50 (mediana) e 75.
b. A quantidade de pessoas com altura acima de 180 cm.
c. Plote um histograma dos dados usando Matplotlib (não precisa
detalhar o código da plotagem).
'''

import numpy as np
import matplotlib.pyplot as plt

# Setando variáveis
media = 170
pessoas = 100
desvio = 10

# Criando a altura
alturas = np.random.normal(media, desvio, pessoas)
print(alturas)

# Letra A
perc25 = np.percentile(alturas, 25)
print(f'25% -> {perc25}')
perc50 = np.percentile(alturas, 50)
print(f'50% -> {perc50}')
perc75 = np.percentile(alturas, 75)
print(f'75% -> {perc75}')

# Letra B
maior180 = alturas[alturas > 180]
print(maior180)

# Letra C
plt.hist(alturas, bins=np.arange(alturas.min(), alturas.max() + 1))
hist = np.histogram(alturas)
plt.show()