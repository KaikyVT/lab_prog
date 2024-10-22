def lista_0_a_4_A():
    lista = [x for x in range(5)]
    print(lista)

def lista_0_a_4_B():
    lista = list(range(5))
    print(lista)

def lista_0_a_4_C():
    lista = []
    i = 0
    while i < 5:
        lista.append(i)
        i+=1
    print(lista)


print('Os três programas em teoria devem printar uma lista de 0 a 4, vamos ver:')
lista_0_a_4_A()
print('-'*30)
lista_0_a_4_B()
print('-'*30)
lista_0_a_4_C()

'''
As três funções printam uma lista de 0 a 4, porém de formas diferentes:
A primeira utiliza list comprehension para printar números do 0 ao 4 a partir de um loop for.
A segunda utiliza a listagem do range(5), que pega os números de 0 a 4 e os coloca em uma lista.
A terceira, por fim, cria uma lista vazia e um índice 0 que, enquanto for menor que 5, adiciona esse índice na lista.

Portanto, a resposta correta é a letra D
Marquei a letra C

Eu não consegui, na hora da prova, entender o funcionamento desse list(range(5)), então pensei que fosse algo que não funcionaria. Agora entendi que posso usar o list() para armazenar números dentro de um range também.
'''