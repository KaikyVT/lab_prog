def soma_diagonal_principal_1(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][i]
    return soma


def soma_diagonal_principal_2(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][-i]
    return soma

def soma_diagonal_principal_3(matriz):
    soma = 0
    for linha in matriz:
        for elemento in linha:
            soma += elemento
    return soma


def soma_diagonal_principal_4(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][len(matriz) - i - 1]
    return soma


def soma_diagonal_principal_5(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[len(matriz) - i - 1][i]
    return soma

matriz = [
    [1, 2, 7],
    [4, 5, 6],
    [0, 8, 4]
]
print('A soma da diagonal principal da matriz deve ser 10, vamos ver qual das soluções funciona:\n')
print(f'Soma solução 1: {soma_diagonal_principal_1(matriz)}')
print('-'*50)
print(f'Soma solução 2: {soma_diagonal_principal_2(matriz)}')
print('-'*50)
print(f'Soma solução 3: {soma_diagonal_principal_3(matriz)}')
print('-'*50)
print(f'Soma solução 4: {soma_diagonal_principal_4(matriz)}')
print('-'*50)
print(f'Soma solução 5: {soma_diagonal_principal_5(matriz)}')

'''
A primeira solução retorna a soma da diagonal principal porque só soma valores em que linha e coluna sejam iguais, ou seja, a diagonal principal.
A segunda solução retorna a soma da diagonal secundária da matriz, não da primária. O motivo é o uso do -i como índice, que faz essa inversão
A terceira solução não retorna a soma da diagonal principal porque ela soma todos os valores da lista, não só os da diagonal principal.
A quarta solução também retorna a soma da diagonal secundária, não da primária. Ela começa do último elemento da linha, não do primeiro
A quinta solução também retorna a soma da diagonal secundária, não da primária. Ela começa da última linha e vai até a primeira

Portanto, apesar de dependendo da matriz inserida, o valor da diagonal secundária ser o mesmo da diagonal primária, o único que realmente imprime o valor da diagonal principal é a solução 1.
Marquei a letra A
A resposta é a letra A
'''