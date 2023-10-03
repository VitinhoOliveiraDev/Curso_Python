# Outra forma de formatação

a = 'A'
b = 'B'
c = 1.1
string = 'a={} b={} c={:.2f}'
formato = string.format(a, b, c) # format(a, b, c)Argumento
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format( nome1=a, nome2=b, nome3=c
)

print(formato)