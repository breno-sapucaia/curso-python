# -*- UTF-8 -*-

palavra = 'paralelepípedo'

for letra in palavra:
    print(letra, end=', ')

print('')

aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria']

for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1}) {nome}')

dias_semana=('domingo', 'Segunda', 'Terça',
             'Quarta' , 'Quinta', 'Sexta', 'Sábado')


for dia in dias_semana:
    print(f'Hoje é {dia}')


