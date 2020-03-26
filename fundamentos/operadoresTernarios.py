esta_chuvendo = True

print('Hoje estou com as roupas ' + ('secas.', 'molhadas.')[esta_chuvendo])
print('Hoje estou com as roupas ' + ('molhadas.' if esta_chuvendo else 'secas.') )


lista = [1,2,3,'ana']
print(1 in lista)
print('ana' in lista)
print('ana' not in lista)
x = 2
y = 4

p = print

p(x is y)
p( x is not  y)

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]

p(lista_b is lista_c )