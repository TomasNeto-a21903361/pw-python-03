import collections
import os
import glob
import csv
import re
from matplotlib import pyplot as plt


def pede_pasta():
    while True:
        path = input("Introduza um caminho para uma pasta:")
        #print(os.path.isdir(f"{os.getcwd()}\\{path}"))
        if os.path.exists(path):
            return path


def faz_calculos(dir):
    #res = {}
    #listaFicheiros = os.listdir(dir)
    #print(listaFicheiros)

    os.chdir(dir)
    count = collections.Counter()
    volume = collections.Counter()
    for filename in glob.glob("*"):
        name, ext = os.path.splitext(filename)
        if ext != '':
            count[ext] += 1
            volume[ext] += os.path.getsize(filename)
    count = {k: ("quantidade: " + str(v)) for k, v in count.items() if k in count}
    volume = {k: ("volume: " + str(v)) for k, v in volume.items() if k in volume}
# print(dict(count))
# print(dict(volume))
    res = {k: {count[k], v} for k, v in volume.items() if k in count}

# res = {str(volume.keys()) + "volume: " + str(dict(volume)) + " quantidade: " + str(dict(count)) + "}"}
    return res

def aux(res):
    xd = {key: [re.sub('quantidade:', '', ele) for ele in val]
    for key, val in res.items()}
    kek = {key: [re.sub('volume:', '', ele) for ele in val]
    for key, val in xd.items()}
    return kek


def guarda_resultados(res):
    nome = input("Introduza nome:")
    final = nome.split(".")
    name = final[0] + ".csv"
    print(name)
    with open(name, 'w', newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Extensao", "Quantidade", "Tamanho[kByte]"])
        for key, value in aux(res).items():
            writer.writerow([key,value])



def faz_grafico_queijos(titulo, lista_chaves, lista_valores):
    plt.pie(lista_valores, labels=lista_chaves, autopct='%1.0f%%')
    plt.title(titulo)
    plt.show()


def faz_grafico_barras(titulo, lista_chaves, lista_valores):
    plt.bar(lista_chaves, lista_valores)
    plt.title(titulo)
    plt.show()


if __name__ == '__main__':
    # print(pede_pasta())
    #print(faz_calculos(pede_pasta()))
    x = faz_calculos(pede_pasta())
    #print(aux(x))
    guarda_resultados(x)
