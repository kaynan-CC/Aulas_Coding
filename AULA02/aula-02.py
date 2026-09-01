#Faça um programa que peça o nome e a idade da pessoa.
nome = input("Digite seu nome: ")
idade = int(input("Digite a sua idade: "))
print(f"Olá {nome}, você tem {idade} anos.")
#Faça um programa que some 2 números.
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
resultado = n1 + n2
print(f"A soma de {n1} + {n2} é igual a {resultado}.")
#Faça um programa onde exibe o antecessor e o sucessor de um número.
numero = int(input("Digite um número: "))
ant = numero - 1
suc = numero + 1
print(f"O sucessor de {numero} é {suc}.\n O antecessor de {numero} é {ant}.\n")
#Faça um programa que dobre um número.
nu = float(input("Digite um número: "))
resul = nu * 2
print(f"O dobro de {nu} é {resul}.")
#Faça um programa que calcule a média de duas notas.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print(f"A média de {nota1} e {nota2} é {media}.")
#Faça um programa que descobre se é maior de idade ou não.
name = input("Digite o seu nome: ")
age = int(input("Digite a sua idade: "))
if age >= 18:
    print(f"{name} Você é maior de idade.")
else:
    print(f"{name} Você é menor de idade.")
#Faça um programa que pede a media de um aluno e exiba se é aprovado ou reprovado.
average = float(input("Digite a média do aluno: "))
if average >= 7:
    print("Aluno aprovado.")
else:
    print("Aluno reprovado.")
#Faça um programa que informa se o número é negativo ou positivo.
number = float(input("Digite um número: "))
if number > 0:
    print("Número positivo.")
elif number < 0:
    print("Número negativo.")
elif number == 0:
    print("o seu número é nulo.")
#Faça um programa que informe qual deles é o maior.
number1 = float(input("Digite o 1°número: "))
number2 = float(input("Digite o 2°número: "))
if number1 > number2:
    print(f"O {number1} é maior que {number2}")
elif number2 > number1:
    print(f"O {number2} é maior que {number1}")
#Faça um programa que pergunta o nome e a idade da pessoa e se a idade for maior ou igual a 12, permite a entrada, se não, bloqueia.
nombre = input("Digite seu nome: ")
idade1 = int(input("Digite a sua idade: "))
if idade1 >= 12:
    print(f"Caro, {nombre}, sua entrada foi permitida.")
else:
    print(f"Caro, {nombre}, sua entrada foi bloqueada.")
#Faça um programa que conte de 1 até 10.
for i in range(1, 11):
    print(i)
#Faça um progarama que conte de 1 até um número personalizado.
n = int(input("Digite um número: "))
for i in range(1, n+ 1):
    print(i)
#Faça um programa que exibe uma tabuada de 1 até 10.
num = int(input("Digite um numero para a tabuada: "))
for i in range(1, 11):
    resultado = num * i
    print(f"{num} * {i} = {resultado}")
#Faça um programa que peça um número inteiro e que realize uma contagem regressiva
nn = int(input("Digite um numero: "))
for i in range(nn, -1, -1):
    print(i)
#Faça um programa que conte de 1 a 50 e exiba apenas os números pares.
for p in range(2, 51, 2):
    print(p)
#Faça um programa que descubra se é par ou ímpar.
nnn= int(input("Digite um número: "))
if nnn % 2 == 0:
    print("Seu numero é par.")
else:
    print("Seu numero é ímpar.")
#Faça um programa que percorra de 1 a 20 e que mostre apenas os números pares.]
for n in range(1, 21):
    if n % 2 == 0:
        print(n)
#Faça um programa que descobre se o número é divisivel por 5.
numer = int(input("Digite um número: "))
if numer % 5 == 0:
    print("Esse número é divisivel por 5.")
else:
    print("Esse número não é divisivel por 5.")
#Faça um programa que verifica a palavra python digitada
palavra = input("Digite a palavra Python: ").upper()
if palavra == "PYTHON":
    print("Você digitou Python.")
else:
    print("Você digitou outra palavra ou digitou Python errado.")
#Faça um programa que peça o nome do aluno, idade e nota. Depois verifique se ele é maior ou menor de idade e se foi aprovado ou reprovado.
#Nota >= 7 Aprovado.
#Nota < 7 Reprovado.
aluno = input("Digite o seu nome: ")
anos = int(input("Digite a sua idade: "))
exam = float(input("Digite a sua nota: "))
print(f"Aluno: {aluno}")
if anos >=18:
    print("Situação: Maior de idade")
else:
    print("Situação: Menor de idade")
if exam >= 7:
    print("Resultado: Aprovado.")
else:
    print("Resultado: Reprovado.")