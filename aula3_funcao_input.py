"""
A função input sempre vai chamar uma string
Para retornar um outro tipo de variável é
recomendado fazer um casting
"""
nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")
print("")
print(f"{nome} tem {idade} anos.")
# casting
data_de_nascimento = 2022 - int(idade)
print(f"{nome} nasceu em {data_de_nascimento}.")
print("")
# números
numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")
numero3 = int(input("Digite o segundo número: "))
print("Soma é: ", numero1 + numero2 + str(numero3))
print("Soma é: ", int(numero1) + int(numero2) + numero3)