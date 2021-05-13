import math

class automovel():
    def __init__(self, cap_dep, quant_comb, consumo):
        self.capacidade = cap_dep
        self.quantidade = quant_comb
        self.consumo = consumo

    def combustivel(self):
        return self.quantidade

    def autonomia(self):
        return math.floor(self.quantidade / (self.consumo / 100))

    def abastece(self, n_litros):
        if n_litros + self.quantidade >= self.capacidade:
            print("Erro! Depósito já cheio")
            self.quantidade = self.capacidade
            return self.quantidade
        else:
            self.quantidade += n_litros
        return automovel.autonomia(self)

    def percorre(self, n_km):
        aux = automovel.autonomia(self)
        if aux >= n_km:
            aux -= n_km
            self.quantidade -= n_km * self.consumo / 100
            return aux
        else:
            print("Erro! A quantidade de combustível no depósito nao permite efetuar o trajeto")
            return -1


if __name__ == "__main__":
    #main
    a1 = automovel(60, 10, 15)
    print(a1.autonomia())
    print(a1.abastece(45))
    print(a1.percorre(150))
    print(a1.percorre(250))

