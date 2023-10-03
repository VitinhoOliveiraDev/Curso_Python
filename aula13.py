# Como formatar uma string

nome = 'Victor Oliveira'
altura = 1.70
peso = 80
imc =  peso / (altura * altura)

"f-strings"
linha_1 = f'{nome} tem {altura:,.2f} de altura' # Formatação de 1.7 para 1.70
linha_2 = f'{peso}, quilos, e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)