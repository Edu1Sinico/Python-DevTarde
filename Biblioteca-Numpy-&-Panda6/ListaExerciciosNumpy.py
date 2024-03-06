import numpy as np

# Criação de Arrays:
# Exercício 1
print("Exercício 1\n")

print("Matriz vazia:")
empty_array = np.empty((3, 3)) # Matriz vazia.
print(empty_array)

print("\nMatriz com os números uns:")
ones_array = np.ones((3,3))
print(ones_array)

# -------------------------------------------------------------------------------------
# Exercício 2

print("\n------------------------------------\nExercício 2\n")

print("Matriz com os números zeros:")
zeros_array = np.zeros((3,3))
print(zeros_array)

# -------------------------------------------------------------------------------------
# Exercício 3

print("\n------------------------------------\nExercício 3\n")

print("Matriz que armazena números aleatórios:")
random_array = np.random.rand(3, 3)
print(random_array)

# -------------------------------------------------------------------------------------
# Exercício 4

print("\n------------------------------------\nExercício 4\n")

print("Criação de uma Matriz Unidimensional:")
my_array = np.array([1,2,3,4,5])
print(my_array)

# -------------------------------------------------------------------------------------
# Exercício 5

print("\n------------------------------------\nExercício 5\n")

print("Criação de uma Matriz Bidimensional:")
my_array2 = np.array([[1,2,3], [4,5,6]])
print(my_array2)

# -------------------------------------------------------------------------------------
# Indexação e Seleção:
# Exercício 6

print("\n------------------------------------\nExercício 6\n")

print("Seleção de elementos específicos de uma matriz (Coluna 1, Linha 3):")
print(my_array2[0,2])

# -------------------------------------------------------------------------------------
# Exercício 7

print("\n------------------------------------\nExercício 7\n")

print("Exibir o valor mínimo e máximo de uma Matriz:\n")
max_value = np.max(my_array2)
min_value = np.min(my_array2)
print(f"Valor máximo da matriz: {max_value}\n"
      +f"Valor mínimo da Matriz: {min_value}")

# -------------------------------------------------------------------------------------
# Exercício 8

print("\n------------------------------------\nExercício 8\n")

print("Calcular a soma dos valores de uma Matriz:\n")
result_array = np.sum(my_array2)
print(f"Resultado da soma dos elementos: {result_array}")

# -------------------------------------------------------------------------------------
# Manipulação de Arrays:
# Exercício 9

print("\n------------------------------------\nExercício 9\n")

print("Remover entradas unidimensionais de uma Matriz:")
remove_array = np.squeeze(my_array2)
print(remove_array)

# -------------------------------------------------------------------------------------
# Exercício 10

print("\n------------------------------------\nExercício 10\n")

print("Somar e subtrair duas Matrizes:\n")
array1 = np.array([[5,6],[2,8]])
array2 = np.array([[5,4],[8,2]])
array_sum = array1 + array2
array_sub = array1 - array2

print("Resultado da Soma:")
print(array_sum)

print("\nResultado da Subtração:")
print(array_sub)

# -------------------------------------------------------------------------------------
# Exercício 11

print("\n------------------------------------\nExercício 11\n")

print("Multiplicação de matrizes:\n")
array_mut = np.dot(array1,array2)
print("Resultado da Multiplicação:")
print(array_mut)

# -------------------------------------------------------------------------------------
# Operações Estatísticas:
# Exercício 12

print("\n------------------------------------\nExercício 12\n")

print("Calcular a média, mediana e desvio padrão de uma Matriz plana:\n")

my_array3 = np.array([[1,3,5],[7,9,11],[13,15,17]])

print("Média:")
array_mean = np.mean(my_array3)
print(array_mean)

print("\nMediana:")
array_median = np.median(my_array3)
print(array_median)

print("\nDesvio Padrão:")
array_std = np.std(my_array3)
print(array_std)

# -------------------------------------------------------------------------------------
# Exercício 13

print("\n------------------------------------\nExercício 13\n")

