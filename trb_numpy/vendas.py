import numpy as np
from datetime import datetime

file_name = "vendas.csv"

# 1 - Leitura e preparação dos Dados
my_data = np.genfromtxt(file_name, delimiter=',', dtype=str, skip_header=1)
qtd_vend = my_data[:, 3] = my_data[:, 3].astype(int)
pr_unit = my_data[:, 4] = my_data[:, 4].astype(float)
val_tot = my_data[:, 5] = my_data[:, 5].astype(float)
datas = my_data[:, 0]
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

# Produto c maior qtd vendida
prod_vend = pr_unit[np.argmax(qtd_vend)]
print(f'Produto mais vendido: {prod_vend}')

# Produto c maior valor de vendas
prod_mv = pr_unit[np.argmax(val_tot)]
print(f"Produto com maior valor total de vendas: {prod_mv}")

# 3 - Análise Temporal

datas_datetime = np.array([datetime.strptime(data, "%Y-%m-%d") for data in datas])

# Dia com mais vendas 

dias_da_semana = [data.strftime("%A") for data in datas_datetime]
unicos, contagens = np.unique(dias_da_semana, return_counts=True)
dia_mais_vendas = unicos[np.argmax(contagens)]
print(f"Dia com mais vendas: {dia_mais_vendas}")

ord = np.argsort(datas_datetime)
datas_ord = datas_datetime[ord]
valores_totais_ord = val_tot[ord]

# Calcular diferenças entre dias consecutivos
variacao_diaria = np.diff(valores_totais_ord)
print(f'Variação diária:\n{variacao_diaria}')




