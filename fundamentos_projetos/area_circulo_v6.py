#!python
from math import pi
import sys

def circulo(raio):
    return float(raio) ** 2 * pi

def help(arg):
    print('É necessário informar o raio da circuferência')
    print(f'Sintaxe: {arg} <raio>') 

if __name__ == '__main__':
    if sys.argv.__len__() < 2:
        help(sys.argv[0][2:])
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print(f'Área do circulo: {area}')
