# Dia 1 - Exercícios

# 1. Crie variáveis para nome, idade e cidade e imprima: "Olá, eu sou NOME, tenho IDADE anos e vivo em CIDADE."

nome = "Alexandre"
idade = 70
cidade = "Maputo"

print(f"Olá, eu sou {nome}, tenho {idade} anos e vivo em {cidade}.")

# 2. Peca ao usuário para digitar o seu nome, idade e cidade e imprima a mesma frase do exercício 1.

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
cidade = input("Digite sua cidade: ")

print(f"Olá, eu sou {nome}, tenho {idade} anos e vivo em {cidade}.")

# 3. Peca ao usuário para digitar dois números e imprima a soma deles.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
print(f"A soma de {num1} e {num2} é {soma}.")

# 4. Crie uma string "Python é incrível!" e imprima apenas a palavra "incrível".

frase = "Python é incrível!"
palavra = frase.split()[2]

print(f"{palavra}")
