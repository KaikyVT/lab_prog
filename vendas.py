import numpy as np

file_name = "vendas.csv"

# 1 - Leitura e preparação dos Dados
my_data = np.genfromtxt(file_name, delimiter=',', dtype=str, skip_header=1)
qtd_vend = my_data[1:, 3] = my_data[1:, 3].astype(int)
pr_unit = my_data[1:, 4] = my_data[1:, 4].astype(float)
val_tot = my_data[1:, 5] = my_data[1:, 5].astype(float)
print(my_data)

# 2 - Análise Estatística

# Média
media = np.mean(val_tot)
print(f'Média: {media:.2f}')

# Mediana
mediana = np.median(val_tot)
print(f'Mediana: {mediana:.2f}')

# Desvio padrão
desvio = np.std(val_tot)
print(f'Desvio: {desvio:.2f}')

prod_a = my_data[1:, 2] == 'Produto A'
prod_b = my_data[1:, 2] == 'Produto B'
prod_c = my_data[1:, 2] == 'Produto C'

prod_qtd_a = qtd_vend[prod_a]
print(prod_qtd_a)

prod_qtd_b = qtd_vend[prod_b]
print(prod_b)

prod_qtd_c = qtd_vend[prod_c]
print(prod_qtd_c)