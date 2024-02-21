#  1. Faça um programa que leia um vetor de 5 números inteiros e mostre-os:
print("Exercício 1:\n")

vetorInteiros = [1, 2, 3, 4, 5]
print(f"\nVetor de nº inteiros: {vetorInteiros}\n")

print ("----------------------------------------------------------------------------\n")

#  2. Faça um programa que leia um vetor de 10 números reais e mostre-os na ordem crescente:
print("Exercício 2:")

vetorDecimal = [1.6, 2.4, 3.5, 8.2, 1.7, 5.3, 9.1, 0.9, 1.05, 14.2] 
print(f"\nVetor de nº decimais e em ordem crescente: {sorted(vetorDecimal)}\n")

print ("----------------------------------------------------------------------------\n")

# 3. Faça um programa que leia 4 notas, mostre as notas e a média na tela.
print("Exercício 3:\n")

vetorNotas = [] # Vetor vazio
vetorMedias = [] # Vetor vazio
cont = 1

while cont <= 4:
    vetorNotas.append(float(input(f"Digite a {cont}ª nota do Aluno: ")))
    cont += 1
