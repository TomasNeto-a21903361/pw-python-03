import os


def pede_pasta():
    while True:
        path = input("Introduza um caminho para uma pasta:")
        if os.path.exists(path):
            return path

def calcula_tamanho_pasta(pasta):
    aux = os.path.getsize(pasta)
    soma = 0
    if os.path.isfile(pasta):
        return aux
    for file in os.listdir(pasta):
        soma += calcula_tamanho_pasta(os.path.join(pasta, file))
    return soma

def main():
    return print(calcula_tamanho_pasta(pede_pasta()))

if __name__ == "__main__":
  main()