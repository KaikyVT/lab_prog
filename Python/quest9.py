alpha = float(input('Informe alpha: '))
x = float(input('Informe X: '))

if alpha > 0.1:
    print('Valor inválido para alpha')
else:
    if x < 0:
        print(alpha * x)
    else:
        print(x)
print('\n')

print('| Situação do programa| Resultado do programa |')
print('|      Alpha > 0.1    | Print de valor inválido |')
print('| Alpha < 0.1 e X < 0 |   Print de alpha * x  |')
print('| Alpha < 0.1 e X >= 0 |       Print de x     |')
print('O programa funciona como o intendido em todas as hipóteses!')

'''
O programa pede que o usuário informe um valor para alpha e um valor para x. Com isso, algumas condições ocorrem:
Caso alpha seja maior que 0.1, o programa printa uma mensagem de valor inválido. 
Caso alpha seja menor que 0.1, outras duas condições ocorrem:
    Caso x seja menor que 0, o programa printa alpha * x
    Caso x seja maior ou igual a 0, o programa printa apenas x

Eu acertei a questão, mas perdi 0.1 porque não fiz em forma de tabela, daí ficou ruim de ler. Não sabia que tinha que ser em forma de tabela, então vacilei.
Agora fiz a tabela no próprio programa. Não é das mais bonitas, mas dá pra entender :)
'''