# ---=<Operações com Variáveis>=---

# Variáveis do tipo inteiro
salario = 3000
bonus = 500
salario_total = salario + bonus
print(salario_total)


# Maniulação de Strings:
nome = "Maria"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome
print(nome_completo)


# Atualização de Variáveis:
contador = 0
contador += 1
print(contador)


# Variáveis e Estrutura de Controle:
idade = 18
if idade >= 18:
    pode_votar = True
else:
    pode_votar = False
print(pode_votar)


# Tipagem em Python
numero = 42
texto = "Python"
# resultado = numero + texto
# print (resultado)

# OU

# print(f"{numero} "+texto )

#  OU

numero = 42
texto = str(numero)  # Converte o número para string

# Ou ao contrário:

texto = "42"
numero = int(texto)  # Converte a string para inteiro


