import pandas as pd

serie = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])

# =============================================================
# Indexação e Fatiamento:


# Acessando elementos por índice
value_at_b = serie['b']
print(f"{value_at_b}\n")

# Fatiando a série
slice_of_series = serie[1:3]
print(f"{slice_of_series}\n")

# =============================================================
# Operações Matemáticas: Realize operações matemáticas em uma Série.

# Operações matemáticas
dobro = serie * 2
print("Série multiplicada por 2:")
print(f"{dobro}\n")

# =============================================================
# Filtragem de Dados: Use condições para filtrar dados na Série.

# Filtrando dados
maior_que_30 = serie[serie > 30]
print("Elementos maiores que 30:")
print(f"{maior_que_30}\n")

# =============================================================
# Operações Estatísticas: Calcule estatísticas básicas sobre os dados.

# Operações estatísticas
media = serie.mean()
soma = serie.sum()
print("Média:", media)
print("Soma:", soma,"\n")




