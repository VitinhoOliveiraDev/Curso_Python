# Precedencia de operadores aritméticos

# 1. (n + n) # Primeiro a ser executado de dentro para fora.
# 2. ** # Segundo a ser executado
# 3. * / // % # Terceiro a ser executado da esquerda para direita
# 4. + - # Quarto a ser executado
conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)