import pandas as pd
import yaml
import matplotlib.pyplot as plt


# Carregar os dados dos funcionários a partir do arquivo YAML
with open("Biblioteca-Panda-7/dados/dados_funcionarios.yaml", "r") as file:
    dados_yaml = yaml.safe_load(file)


# Converter para DataFrame
df = pd.DataFrame(dados_yaml["funcionarios"])

# 1. Análise Exploratória
print("1. Análise Exploratória:")
print(df.head())  # Visualizar as primeiras linhas
print(df.info())  # Informações sobre os tipos de dados e valores nulos
print(df.describe())  # Estatísticas descritivas básicas

# 2. Seleção e Filtragem de Dados
print("\n2. Seleção e Filtragem de Dados:")
funcionarios_acima_30 = df[df['idade'] > 30]
print("Funcionários com mais de 30 anos:")
print(funcionarios_acima_30,"\n")


funcionarios_salario_acima_4000 = df[df['salario'] > 4000]
print("\nFuncionários com salário acima de 4000:")
print(funcionarios_salario_acima_4000,"\n")

# 3. Manipulação de Dados
print("\n3. Manipulação de Dados:")
df['salario_ajustado'] = df['salario']*1.1
print(df)

# 4. Agregação de Dados
print("\n4. Agregação de Dados:")
salario_medio = df['salario'].mean()
print("\nSalário médio dos funcionários antes do ajuste:", salario_medio)

salario_medio_ajustado = df['salario_ajustado'].mean()
print("\nSalário médio dos funcionários depois do ajuste:", salario_medio_ajustado)

idade_media = df["idade"].mean()
print("\nIdade média dos funcionários:", idade_media)

# cria um Arquivo CSV com o dataFrame
df.to_csv('Biblioteca-Panda-7/dados/dados_funcionarios.csv', index=False)

# 5. Visualização de Dados
print("\n5. Visualização de Dados:")
plt.hist(df['idade'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.title('Distribuição de Idades dos Funcionários')
plt.show()


plt.scatter(df['idade'], df['salario'], color='green')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.title('Idade vs Salário dos Funcionários')
plt.show()
