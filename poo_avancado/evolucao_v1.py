#!python

class Humano:
    # atributos
    especie = 'Homo Sapiens'
    
    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Home {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]

class Neanderthal(Humano):
    especie = Humano.especies()[-2]

class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

if __name__ == "__main__":
    # jose = Humano('José')
    # grokn = Humano("Grokn")

    # grokn.das_cavernas()

    # print(f'Humano.especie: {Humano.especie}')
    # print(f'jose.especie: {jose.especie}')
    # print(f'grokn.especie {grokn.especie}')
    jose = HomoSapiens('José')
    grokn = Neanderthal('Grokn')
    print(f'Evolução (a partir da classe) 
           {', '.join(HomoSapiens.especies())}')
    print(f'Ev')