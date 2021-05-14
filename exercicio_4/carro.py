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

def main():
    option = None
    cap_dep = int(input("Insira a capacidade do depósito: "))
    quant_comb = int(input("Insira a quantidade de combustível no depósito: "))
    consumo = int(input("Insira o consumo do automóvel em litros aos 100km: "))
    a1 = automovel(cap_dep, quant_comb, consumo)

    while option != 0:
        n_km = 0
        n_litros = 0

        print("-- ESCOLHA UMA OPÇÃO --")
        print("1 -> Ver a quantidade de combustível")
        print("2 -> Ver a autonomia")
        print("3 -> Abastecer o depósito")
        print("4 -> Percorrer distância")
        print("0 -> Sair")

        option = eval(input(">>>"))

        if option == 3:
            n_litros = int(input("Introduza o nº de litros: "))
        elif option == 4:
            n_km = int(input("Introduza o nº de km: "))
        elif option == 0:
            return

        actions = {
            1: a1.combustivel(),
            2: a1.autonomia(),
            3: a1.abastece(n_litros),
            4: a1.percorre(n_km),
        }

        print(actions[option])

if __name__ == "__main__":
    #main
    #a1 = automovel(60, 10, 15)
    #print(a1.autonomia())
    #print(a1.abastece(45))
    #print(a1.percorre(150))
    #print(a1.percorre(250))
    main()

