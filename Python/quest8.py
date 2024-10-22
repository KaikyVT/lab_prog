def imc_cal(altura, peso):
    imc = peso / (altura*altura)
    print(f'Seu IMC é {imc:.2f}, isso significa que você está:')

    if imc < 17:
        print('Muito abaixo do peso.')
    elif imc < 18.5:
        print('Abaixo do peso.')
    elif imc < 25:
        print('Com o peso normal.')
    elif imc < 30:
        print('Com sobrepeso')
    elif imc < 35:
        print('Com obesidade grau I')
    elif imc < 40:
        print('Com obesidade grau II')
    else:
        print('Com obesidade grau III')


altura = float(input('Digite sua altura: '))
peso = int(input('Digite seu peso: '))

imc_cal(altura, peso)

'''
A função imc_cal() calcula o IMC inserido a partir da fórmula peso / altura². A partir do valor resultante, a função calcula se o IMC está em uma faixa de números e informa a classificação de acordo com a tabela da OMS.

Eu acertei a questão, mas fiz uma redundância na parte dos elifs, perdendo assim 0.3 pontos. Eu fiz, por exemplo:
if imc < 17:
    (condição)
elif imc >= 17 and imc < 18.5:
    (outra condição)
...

Essas duas condições no elif fazem o programa realizar um cálculo a mais. Nesse caso a diferença de tempo é imperceptível, mas em outros casos pode gerar lentidões por conta dessa má otimização.
'''