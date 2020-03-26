#!python
from math import pi


def circulo(raio):
    return raio ** 2 * pi


if __name__ == '__main__':
    area = circulo(input())
    print(f'Área do circulo: {area}')
