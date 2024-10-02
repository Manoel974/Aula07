n = int(input('Número 1: '))
a = int(input('Número 2: '))
s = int(input('Número 3: '))
b = int(input('Número 4: '))
e = int(input('Número 5: '))

tupla_notas = (n, a, s, b, e)

print(f'Menor número: {min(tupla_notas)}')
print(f'Maior número: {max(tupla_notas)}')
print(f'Valor total: {sum(tupla_notas)}')
print(sorted(tupla_notas))

