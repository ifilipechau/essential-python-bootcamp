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

print(f".. e a palavra mágica é {palavra}")

# 5. Dada a string "     dados limpos      ", limpe os espaços e transforme em maiúsculas.

dados = "    dados limpos    "
dados_limpos = dados.strip().upper()
print(f"Este é o dado antes de limpar: '{dados}'")
print(f"E este é o dado limpo: {dados_limpos}")


# 6. Crie uma lista com 5 frutas. Imprima a segunda e a última.

frutas = ["maçã", "banana", "laranja", "uva", "papaia"]
print(f"A segunda fruta é: {frutas[1]}, e a última é: {frutas[-1]}")



# 7. Crie um dicionário com informações de uma pessoa (nome, idade, profissão) e imprima uma frase com os dados

pessoa = {
    "nome": "Quitéria",
    "idade": 61,
    "profissao": "Engenheira"
}
print(f"{pessoa['nome']} tem {pessoa['idade']} anos e é {pessoa['profissao']}")


# 8. Peca ao usuário um número e diga se ele é par ou ímpar.

numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")



# 9. Peca uma palavra e diga quantas vogais ela tem.
palavra = input("Digite uma palavra: ")
vogais = "aeiouAEIOU"
contador_vogais = sum(1 for letra in palavra if letra in vogais) # Contagem de vogais usando compreensão de lista
print(f"A palavra '{palavra}' tem {contador_vogais} vogais.")


# 10. Converta a idade em anos para  meses e dias (suponha 365 dias por ano).
idade = int(input("Digite sua idade em anos: "))
meses = idade * 12
dias = idade * 365
print(f"Sua idade em meses é {meses} e em dias é {dias}")


# 11. Desafio: Crie um script que pergunta o nome completo do usuário e imprime:
# - Quantas letras tem (sem espacos)
# - Primeira letra
# - Última letra

nome_completo = input("Digite seu nome completo:  ").strip()
num_letras = len(nome_completo)
print(f"O teu nome tem {num_letras} letras, a primeira letra é: {nome_completo[0]}, e a última letra é: {nome_completo[-1]} ")
