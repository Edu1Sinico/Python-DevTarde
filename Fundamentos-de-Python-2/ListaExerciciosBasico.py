# Exercício 1 

# Soma (a + b).
# Subtração (a - b).
# Multiplicação (a * b).
# Divisão (a / b).
# Divisão Inteira (a // b).
# Resto da Divisão (a % b).
# Potenciação (a ** b).
# Declare uma variável para representar o raio de um círculo e calcule sua área usando a fórmula área = π * raio^2. Considere π como 3.14.

from ctypes.wintypes import PINT


pi = 3.14
a = int(input("Digite o 1º número: "))
b = int(input("Digite o 2º número: "))

print(f"\nA soma entre {a} e {b} é: {a + b}")
print(f"\nA subtração entre {a} e {b} é: {a - b}")
print(f"\nA multiplicação entre {a} e {b} é: {a * b}")

if b != 0:
    print(f"\nA divisão entre {a} e {b} é: {a / b}")
else:
    print("\nNão existe divisão por 0!")

if b != 0:
    print(f"\nA divisão inteira entre {a} e {b} é: {a // b}")
else:
    print("\nNão existe divisão por 0!")

if b != 0:
    print(f"\nA o resto da divisão entre {a} e {b} é: {a % b}")
else:
    print("\nNão existe divisão por 0!")

print(f"\nA potência entre {a} e {b} é: {a ** b}")
print(f"\nA área do circulo de raio {a} é: {pi * (a**2)} \nE a área do circulo de raio {b} é: {pi * (b**2)}")

#============================================================================================================
print("\n===================================================================================\n")

# Exercício 2

nome = input("Digite o seu primeiro nome: ")
sobrenome = input("Digite o seu segundo nome: ")

# Concatenar strings usando o operador '+'
nome_completo = nome + " " + sobrenome

print(f"\nOlá, o seu nome completo é: {nome_completo}")

frase = "Está é uma frase muito legal." 

frase_upper = frase.upper()
frase_lower = frase_upper.lower()
frase_replacement = frase.replace("legal","ruim")

print(f"\nFrase original: {frase}")
print(f"\nFrase com todas as letras maiúsculas: {frase_upper}")
print(f"\nFrase com todas as letras minúsculas: {frase_lower}")
print(f"\nFrase com palavra substituida: {frase_replacement}")

#============================================================================================================
print("\n===================================================================================\n")

# Exercício 3

# Lista

lista_cores = ["Amarelo", "Vermelho", "Azul"]
print(f"Lista de cores atual: {lista_cores}")

lista_cores.append("Verde")
lista_cores.append("Laranja")
print(f"\nLista de cores adicionadas: {lista_cores}")

# Tupla

tupla_coordenadas = (48.858370,2.294481)
print(f"\nCoordenadas da Torre Eiffel: {tupla_coordenadas}")

#============================================================================================================
print("\n===================================================================================\n")

# Exercício 4

# Variáveis booleanas
tem_chuva = False
faz_sol = False

x = int(input("Digite '0' para tempo com sol ou digite '1' para tem com chuva: "))

if (x == 0):
    faz_sol = True
    tem_chuva = False
elif(x == 1):
    tem_chuva = True
    faz_sol = False
else:
    print("\npor favor, digite um do números correspondentes!")

if (faz_sol == True and tem_chuva == False):
    print("\nO tempo está bom para uma caminhada :)")
elif(faz_sol == False and tem_chuva == True):
    print("\nO tempo está chuvoso :'(")

