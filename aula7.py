# Variáveis são usadas para salvar algo na memória do computador.
# PEP8: inicie variáveis com letras minúsculos, pode usar
# Números e underline _.
# O sinal de = é o operador de atribuição. Ele é usado para
# Atribuir um valor a um nome (variável)
# Uso: nome_variavel = expressão

nome_completo = 'Victor Carvalho Junior'
soma_dois_mais_dois =  2 + 2
int_um = int('1')
int_um = bool('1')
print(int_um, type(int_um))
print(int('1'), type(int('1')))
print(nome_completo, soma_dois_mais_dois) 

# Ficha basica para identicar maior de idade ou menor.

nome = 'Victor'
idade = 20
maior_de_idade = idade >= 18
print('Nome:', nome, 'Idade:', idade)
print('É maior?', maior_de_idade)