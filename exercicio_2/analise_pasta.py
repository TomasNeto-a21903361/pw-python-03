import collections
import os
import glob
import csv


def pede_pasta():
    while True:
        path = input("Introduza um caminho para uma pasta:")
        if os.path.exists(path):
            return path


def faz_calculos(dir):
    # res = {}
    listaFicheiros = os.listdir(dir)
    # print(listaFicheiros)

    os.chdir(dir)
    count = collections.Counter()
    volume = collections.Counter()
    for filename in glob.glob("*"):
        name, ext = os.path.splitext(filename)
        count[ext] += 1
        volume[ext] += os.path.getsize(filename)
    count = {k: ("quantidade: " + str(v)) for k, v in count.items() if k in count}
    volume = {k: ("volume: " + str(v)) for k, v in volume.items() if k in volume}
    # print(dict(count))
    # print(dict(volume))
    res = {k: {count[k], v} for k, v in volume.items() if k in count}

    # res = {str(volume.keys()) + "volume: " + str(dict(volume)) + " quantidade: " + str(dict(count)) + "}"}
    return res


def guarda_resultados(res):
    nome = input("Introduza nome:")
    final = nome.split(".")
    name = final[0] + ".csv"
    print(name)
    with open(name, 'w', newline="") as csv_file:
        writer = csv.writer(csv_file)
        for key, value in res.items():
            writer.writerow([key, value])



if __name__ == '__main__':
    # print(pede_pasta())
    #print(faz_calculos(pede_pasta()))
    x = faz_calculos(pede_pasta())
    guarda_resultados(x)
