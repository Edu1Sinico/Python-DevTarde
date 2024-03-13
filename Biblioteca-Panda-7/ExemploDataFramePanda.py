import matplotlib as plt
import pandas as pd

# Matriz
data = {'Nome': ['Alice', 'Bob', 'Charlie', 'James'],
        'Idade': [25, 30, 35, 38],
        'Cidade': ['A', 'B', 'C', 'D']}

# Criação do DataFrame
df = pd.DataFrame(data)

# =============================================================
# Seleção e Indexação:

# Acessando uma coluna por nome
coluna_idade = df['Idade']
print(f"{coluna_idade}\n")


# Selecionando linhas com base em uma condição
linha_filtro = df[df['Idade'] > 30]
print(f"{linha_filtro}\n")

# =============================================================
# Operações com DataFrames:

# Adicionando uma nova coluna
df['Profissao'] = ['Engenheiro', 'Analista', 'Designer', 'Programador']
print(f"{df}\n")


# Removendo uma coluna
df_sem_cidade = df.drop('Cidade', axis=1)
print(f"{df_sem_cidade}\n")

# =============================================================
# Visualização de Dados:

# Gráfico de barras da idade por nome
df.plot.bar(x='Nome', y='Idade')
plt.show()