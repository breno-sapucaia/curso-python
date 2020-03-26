class Carro:
    def __init__(self, vel_maxima):
        self.vel_atual = 0
        self.vel_maxima = vel_maxima

    def acelerar(self, delta=5):
        if delta + self.vel_atual > self.vel_maxima:
            self.vel_atual = self.vel_maxima
        else:
            self.vel_atual += delta
        return self.vel_atual

    def frear(self, delta):
        if self.vel_atual - delta < 0:
            self.vel_atual = 0
        else:
            self.vel_atual -= delta
        return self.vel_atual



if __name__ == "__main__":
    c1 = Carro(180)

    for _ in range(25):
        print(c1.acelerar(8))
        
    for _ in range(10):
        print(c1.frear(delta=20))