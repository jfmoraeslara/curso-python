nome = "João"
idade = 40
altura = 1.77
peso = 90
e_maior = idade > 18
print(nome)
print(nome, type(nome))
print("Nome:", nome)
print("Altura:", altura)
print("Peso:", peso)
print("Maior de idade:", e_maior)
imc = peso / (altura ** 2)  # (**) ao quadrado
print("IMC:", imc)
print(nome, "tem", idade, "anos, pesa", peso, "kg, altura de", altura, "e um IMC igual a", imc)
