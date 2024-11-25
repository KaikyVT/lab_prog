'''.Use numpy.linspace para criar um array com 50 valores igualmente
espaçados entre 0 e 10. Use numpy.arange para criar um array com
valores de 0 a 10, incrementando de 0.2.'''

import numpy as np

# De 0 a 10, de 0.2 em 0.2
arr1 = np.linspace(0, 10)

# Definindo condições de print e printando
np.set_printoptions(precision=1)
print(arr1)