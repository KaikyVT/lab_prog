import numpy as np

arr = np.array(range(0, 51))

lista1 = arr[arr%2 == 0]
print(lista1)

posic = arr[37]
print(posic)
print(arr)