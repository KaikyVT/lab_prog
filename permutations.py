def permutations(lista):
    tamanho = len(lista)
    ponteiro = 0
    matriz = []
    while ponteiro != tamanho:
        for i in range(ponteiro, tamanho - 1):
            copy = lista.copy()
            copy[ponteiro], copy[i+1] = copy[i+1], copy[ponteiro]
            matriz.append(copy)
            for j in range(ponteiro + 1, tamanho - 1):
                copy2 = copy.copy()
                copy2[ponteiro], copy2[j+1] = copy2[j+1], copy2[ponteiro]
                matriz.append(copy2)
            
        ponteiro += 1
    return matriz
        

lista = [1, 2, 3]
print(permutations(lista))
