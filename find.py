def find(lista, valor) -> int:
    tamanho_lista = len(lista)
    for i in range(tamanho_lista):
        # Caso o valor já esteja na lista
        if valor == lista[i]:
            return i
        # Caso o valor esteja entre 2 valores na lista
        elif valor > lista[i] and valor < lista[i+1]:
            return i+1
        # Caso seja maior que o último da lista
        elif valor > lista[-1]:
            return tamanho_lista
        # Caso seja menor que o primeiro da lista
        elif valor < lista[0]:
            return 0

lista = [1, 2, 3, 4, 6, 7]
print(f'O valor escolhido está ou estaria na posição {find(lista, 8)}')