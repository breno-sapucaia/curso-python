#!python
import csv
from urllib import request

def read(url):
    with request.urlopen(url) as entrada:
        print('Baixando o CSV...')
        dados = entrada.read().decode('latin1')
        print('Download completo')
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}: {cidade[3]}')

# with open('./desafio-ibge.csv') as registros:
#     for registro in csv.reader(registros):
#         print('nono campo: {} e quarto campo: {}'.format(registro[8], registro[3]))
if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
