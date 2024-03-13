import numpy as np

print("Matriz vazia:")
empty_array = np.empty((3, 3)) # Matriz vazia.
print(empty_array)

# -------------------------------------------------------------------------------------

print("\n------------------------------------\n")
print("Matriz com número o 1: ")
ones_array = np.ones((2, 2)) # Matriz com o número 1.
print(ones_array)

# -------------------------------------------------------------------------------------

print("\n------------------------------------\n")
print("Matriz com números zeros")
zeros_array = np.zeros((4, 4)) # Matriz com números zeros.
print(zeros_array)

# -------------------------------------------------------------------------------------

print("\n------------------------------------\n")
print("Matriz que armazena números aleatórios:")
random_array = np.random.rand(3, 3)
print(random_array)

# -------------------------------------------------------------------------------------

print("\n------------------------------------\n")
print("Matriz declarada:")
my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # Declarando uma matriz com elementos com linhas ([], [], []) e Colunas ([1, 2, 3])
print(my_array)
print("\n Exibir um elementos específico da Matriz (Linha [1], Coluna [2]): ")
print(my_array[1, 2])  # Seleciona o elemento na segunda linha e terceira coluna (6)

# -------------------------------------------------------------------------------------

print("\n------------------------------------\n")
max_value = np.max(my_array) # Pega o valor máximo da Matriz
min_value = np.min(my_array) # Pega o valor mínimo da Matriz
print(f"Valor máximo: {max_value}, Valor mínimo: {min_value}")

# -------------------------------------------------------------------------------------
print("\n------------------------------------\n")
total_sum = np.sum(my_array) # Soma todos os elementos da matriz
print(f"Soma total: {total_sum}")

# -------------------------------------------------------------------------------------

print("\n------------------------------------\n")
# Remove os espaços unidimensionais da matriz. 
squeezed_array = np.squeeze(my_array)
print(squeezed_array)

# -------------------------------------------------------------------------------------

print("\n------------------------------------\n")
# Adição de Matrizes: usamos o operador +. Aqui está um exemplo:
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = matriz1 + matriz2
print("Resultado da adição de matrizes:")
print(resultado)

# -------------------------------------------------------------------------------------

print("\n------------------------------------\n")
# Subtração de Matrizes: usamos o operador -. Aqui está um exemplo:
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = matriz1 - matriz2
print("Resultado da subtração de matrizes:")
print(resultado)

# -------------------------------------------------------------------------------------

print("\n------------------------------------\n")
# Multiplicação de Matrizes: Para multiplicar matrizes em Python, podemos usar a função numpy.dot() ou o operador @. Aqui está um exemplo:
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = np.dot(matriz1, matriz2)
# Ou, alternativamente: resultado = matriz1 @ matriz2
print("Resultado da multiplicação de matrizes:")
print(resultado)

# -------------------------------------------------------------------------------------

print("\n------------------------------------\n")
