#!python
from datetime import datetime
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'Nome: {self.nome} - Idade: {self.idade}'

    def isAdulto(self):
        return True if self.idade >= 18 else False

class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__( nome, idade)
        self.compras = []


    def registrar_compra(self, compra):
        self.compras.append(compra)

    def get_data_ultima_compra(self):
        try:
            compra = self.compras[-1]
            return compra.data
        except IndexError as e:
            return f'Não existe uma compra na lista de compras \n error: {e}'
        
        

    def total_compra(self):
        return sum([compra.valor for compra in self.compras])

class Compra:
    def __init__(self, vendedor, data, valor):
        self.vendedor = vendedor
        self.data = data
        self.valor = valor

def main():
    vendedor = Vendedor('Adilson', 18, 983)
    compra1 = Compra(vendedor, datetime.now(), 51)
    compra2 = Compra(vendedor, datetime.now(), 49)

    cliente = Cliente('Sérgio', 23)
    print(cliente.get_data_ultima_compra())
    cliente.registrar_compra(compra1)
    cliente.registrar_compra(compra2)
    print(cliente.get_data_ultima_compra())
    print(cliente.total_compra())


if __name__ == "__main__":
    main()


                



    
    
