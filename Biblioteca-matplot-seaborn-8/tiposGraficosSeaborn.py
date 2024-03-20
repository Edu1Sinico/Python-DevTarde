from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np


# Dados
dados = np.random.normal(loc=0, scale=1, size=1000)


# Plotar histograma com KDE
sns.histplot(dados, kde=True)
plt.title('Histograma com KDE')
plt.xlabel('Valores')
plt.ylabel('Densidade')
plt.show()


# Dados
categorias = ['A', 'B', 'C', 'D']
valores = [20, 35, 30, 25]


# Plotar gráfico de barras categóricas
sns.barplot(x=categorias, y=valores)
plt.title('Gráfico de Barras Categóricas')
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.show()




# Dados
dados = sns.load_dataset('iris')


# Plotar box plot
sns.boxplot(x='species', y='sepal_length', data=dados)
plt.title('Box Plot')
plt.xlabel('Espécies')
plt.ylabel('Comprimento da Sépala')
plt.show()


# Dados
dados = sns.load_dataset('iris')


# Plotar violin plot
sns.violinplot(x='species', y='sepal_length', data=dados)
plt.title('Violin Plot')
plt.xlabel('Espécies')
plt.ylabel('Comprimento da Sépala')
plt.show()
