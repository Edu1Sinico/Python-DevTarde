# Criação de Listas

# Listas de números
numeros = [1,2,3,4,5]

# Lista de strings
frutas = ["maçã","banana","laranja"]

# Lista mista
mistura = [1, "python", True, 3.14]

# ====================================

#Acesso a Elementos:

# Acesso por índice
primeiro_elemento = numeros[0]  # Resultado: 1

# Índices negativos contam a partir do final
ultimo_elemento = frutas[-1]  # Resultado: "laranja"

# ====================================

#Modificação de Elementos:

# Modificar um elemento
frutas[1] = "kiwi"  # Agora a lista é ["maçã", "kiwi", "laranja"]

#Adição e Remoção de Elementos:

# Adicionar elemento ao final da lista
frutas.append("uva")  # Resultado: ["maçã", "kiwi", "laranja", "uva"]

# Remover elemento por valor
frutas.remove("kiwi")  # Resultado: ["maçã", "laranja", "uva"]

# ====================================

# Operações e Métodos Úteis:
# len(): Retorna o número de elementos na lista.
# append(): Adiciona um elemento ao final da lista.
# pop(): Remove e retorna o último elemento da lista.
# insert(): Insere um elemento em uma posição específica.
# remove(): Remove o primeiro elemento com um valor específico.
# Slicing: Permite criar sublistas usando a notação de slicing.

# Exemplo de Slicing
sublista = numeros[1:4]  # Resultado: [2, 3, 4]

print(numeros)
print(frutas)
print(mistura)
print(sublista)