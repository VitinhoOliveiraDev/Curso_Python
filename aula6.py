# Conversão de tipos, coerção
# Type convertion, typecasting, coercion
# É o ato de converter um tipo em outro
# Tipos imutáveis e primitivos
# Str, int, float, bool
print(1 + 1)

# print('1' + 1) # TypeError
print(str(11) + "b")  # Correção

print("a" + "b")

print("1", type("1"))  # 1 seria um valor,o type vai mostrar o tipo desse valor.

print(int("1"), type(int("1")))  # Convertendo o '1' em inteiro

print(float("1") + 1)  # convertendo para float
print(float("1.2") + 1)

print(bool(" "))  # Convertendo para bool