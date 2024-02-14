# Condicionais:

idade = int(input("Digite a sua idade: "))

if idade < 18:
    print("Você é menor de idade.")
elif 18 <= idade < 60:
    print("Você é adulto.")
else:
    print("Você é um(a) idoso(a).")

# Loops:

# Loop for para imprimir os números pares de 0 a 9
for numero in range(10): # range ---> método de tamanho de uma lista
    if numero % 2 == 0:
        print(numero)

# Loop while para contar até 5
contador = 0
while contador <= 5:
    print(contador)
    contador += 1
