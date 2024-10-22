from random import randint
import time
import sys

#Solução 1
def tem_duplicados(lista):
    start= time.time()
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                end = time.time()
                totim = end - start
                print(f'Tempo de processamento: {totim:.7f}')
                size = sys.getsizeof(lista)
                print(f'Como temos apenas uma lista padrão, a função pesa: {size} bytes')
                return True
    end = time.time()
    totim = end - start
    print(f'Tempo de processamento: {totim:.7f}')
    size = sys.getsizeof(lista)
    print(f'Como temos apenas uma lista padrão, a função pesa: {size} bytes')
    return False

#Solução 2
def tem_duplicados2(lista):
    start = time.time()
    lista_ordenada = sorted(lista)
    for i in range(len(lista_ordenada) - 1):
        if lista_ordenada[i] == lista_ordenada[i+1]:
            end = time.time()
            totim = end - start
            print(f'Tempo de processamento: {totim:.7f}')
            size = sys.getsizeof(lista) + sys.getsizeof(lista_ordenada)
            print(f'Como temos uma lista padrão e uma lista ordenada (2 variáveis), a função pesa: {size} bytes')
            return True
    end = time.time
    totim = end - start
    print(f'Tempo de processamento: {totim:.7f}')
    size = sys.getsizeof(lista) + sys.getsizeof(lista_ordenada)
    print(f'Como temos uma lista padrão e uma lista ordenada (2 variáveis), a função pesa: {size} bytes')
    return False

#Solução 3
def tem_duplicados3(lista):
    start = time.time()
    elementos_vistos = set()
    for elemento in lista:
        if elemento in elementos_vistos:
            end = time.time()
            totim = end - start
            print(f'Tempo de processamento: {totim:.7f}')
            size = sys.getsizeof(lista) + sys.getsizeof(elementos_vistos)
            print(f'Como temos apenas uma lista padrão e um set de elementos vistos, a função pesa: {size} bytes')
            return True
        elementos_vistos.add(elemento)
    end = time.time()
    totim = end - start
    print(f'Tempo de processamento: {totim:.7f}')
    size = sys.getsizeof(lista) + sys.getsizeof(elementos_vistos)
    print(f'Como temos apenas uma lista padrão e um set de elementos vistos, a função pesa: {size} bytes')
    return False

lista = []
for i in range(1000000):
    lista.append(randint(1,100000000))


print('Solução 1:')
print(tem_duplicados(lista))
print('-'*50)
print('Solução 2:')
print(tem_duplicados2(lista))
print('-'*50)
print('Solução 3:')
print(tem_duplicados3(lista))
print('-'*50)
print('Claramente a Solução 3 é mais rápida e claramente a Solução 1 pesa menos')

'''
A primeira função, como dá para ver pelos números, é uma função mais leve, porém que demora MUITO mais.
A segunda função, como também podemos ver pelos números, é a mais pesada, já que no seu pior caso ela duplica a lista. Não é a mais rápida, porém está longe de ser a mais lenta.
A terceira função como os números apontam, não é a mais pesada, mas também não é a mais leve. Porém é definitivamente a mais rápida. 
Marquei a letra D
As respostas poderiam ser C ou D, já que ambas ocorrem.
'''
