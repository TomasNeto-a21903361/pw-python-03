import os


def pede_nome():
    diretorio = os.getcwd()
    while True:
        nome = input("Introduza nome:")
        localizacao = os.path.join(diretorio, nome)
        # print(nome + ".txt")
        # print(localizacao)
        if os.path.isfile(localizacao):
            return nome

def gera_nome(nome):
    final = nome.split(".")
    res = final[0] + ".json"
    return res




#if __name__ == '__main__':
    #print(gera_nome(pede_nome()))
