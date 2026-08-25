#Escreva um programa que peça o nome e a idade de uma pessoa e diga se ela pode votar.
nome = input("Digite seu nome: ")
idade = int(input("Digite a sua idade: "))

if idade >= 16:
    print(f"{nome}, Você pode votar!")
else:
    print(f"{nome}, Vocẽ não pode votar!")
#Tabuada feita em for de 1 a 10.
numero = int(input("Digite um numero para a tabuada: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")
#programa que conte de 1 a 100 e exiba apenas os números pares.
for i in range(0, 101, 2):
    print(i)
#Peça ao usuário uma palavra e verifique se ela é um palíndromo (ex: “arara”).
palavra = input("Digite uma palavra: ")
if palavra == palavra[::-1]:
    print("Essa palavra é um PALÍNDROMO")
else:
    print("Essa palavra NÃO é um PALÍNDROMO")
