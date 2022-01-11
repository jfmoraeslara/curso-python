nome = "João"
idade = 40
altura = 1.77
peso = 90
e_maior = idade > 18
imc = peso / (altura ** 2)  # (**) ao quadrado
print("IMC:", imc)
print(nome, "tem", idade, "anos, pesa", peso,"kg, altura de", altura, "e um IMC igual a", imc)
# uso do f'{}' em uma string
print(f"{nome} tem {idade} anos, pesa {peso}kg, altura de {altura} e um IMC igual a {imc:.2f}")
# método com uso do format
print("{} tem {} anos, pesa {}kg, altura de {} e um imc igual a {:.2f}".format(nome, idade, peso, altura, imc))
print("{0} tem {1} anos, pesa {2}kg".format(nome, idade, peso))
print("{n} tem {i} anos, pesa {p}kg".format(n=nome, i=idade, p=peso))
