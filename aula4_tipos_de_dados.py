"""
tipos de dados
str - string - textos - 'Texto' "Texto"
int - inteiro - 12345 - 10 - 20 - 1500
float - real/ponto flutuante 10.50 - 2.5
bool - booleano/lógico - true/false 10 == 10 'true'
"""
# comando type
print("João", type("João"))
print("12345", type("12345"))  # entre aspas será considerado str
print(12345, type(12345))
print(10.50, type(10.50))
print(10 == 10, type(10 == 10))
print(10 == 5, type(10 == 5))
print(bool(""))
print(bool(0))
print("João", type("João"), bool("João"))
# type casting - str para int
print("10", type(int("10")))
print("10", "---", (float("10")))