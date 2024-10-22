def func(n):
    if n == 0:
        return 1
    else:
        return n * func(n - 1)

print(func(3))

'''
Essa função retorna o fatorial de um número, já que ela utiliza a recursividade para fazer um número N se multiplicar por N - 1, e pega esse N - 1 e passa pela função novamente até que o número seja 0, retornando 1 e não utilizando da recursividade.
Com o exemplo do 3, ele faz 3 * 2 * 1 * 1, sendo esse último número 1 o momento em que a função recebe "((3 - 1) - 1) - 1
Marquei a letra B
A resposta é a letra B
'''