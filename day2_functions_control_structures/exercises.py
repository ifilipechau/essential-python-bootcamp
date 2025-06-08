### 10 - Exercícios de Fixação
# Usaremos dois tipos de abordagens para resolver os exercícios:
# 1. Abordagem directa, onde resolveremos o exercício de forma simples e rápida.
# 2. Abordagem com boas prácticas, onde criaremos funções para resolver o exercício de forma mais organizada e reutilizável.


# Abordagem directa

# 1. Peça a idade do usuário e diga se ele é maior de idade.

idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade.")


# Aborgem com boas prácticas

# 1. Peça a idade do usuário e diga se ele é maior de idade.
def verificar_mairidade():
    idade = int(input("Digite a sua idade: "))
    if idade >= 18:
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade")

verificar_mairidade()