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

'''
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
'''

def faz_calculos(foldername):
    res = {}
    dirs = os.listdir(foldername)

    for file in dirs:
        path = f"teste\\{file}"
        if os.path.isfile(path):
            size = os.path.getsize(path)
            ext = file.split(".")[-1]
            if not ext in res:
                res[ext] = {}
                res[ext]['quantidade'] = 1
                res[ext]['size'] = size
            else:
                res[ext]['quantidade'] = res[ext]['quantidade'] + 1
                res[ext]['size'] = res[ext]['size'] + size

    return res

'''
def aux(res):
    xd = {key: [re.sub('quantidade:', '', ele) for ele in val]
    for key, val in res.items()}
    kek = {key: [re.sub('volume:', '', ele) for ele in val]
    for key, val in xd.items()}
    return kek
'''


def guarda_resultados(res):
    nome = input("Introduza nome:")
    final = nome.split(".")
    name = final[0] + ".csv"
    print(name)
    with open(name, "w", newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(["Extensao", "Quantidade", "Tamanho\[kByte]"])
        for key in res:
            writer.writerow([key, res[key]['quantidade'], res[key]['size']])



def faz_grafico_queijos(dict_info):
    lista_chaves = [key for key in dict_info.keys()]
    lista_valores_Quantidades = [dict_info[key]['quantidade'] for key in dict_info.keys()]
    plt.pie(lista_valores_Quantidades, labels=lista_chaves, autopct='%1.0f%%')
    plt.title("Quantidades")
    plt.show()

    lista_valores_Tamanhos = [dict_info[key]['size'] for key in dict_info.keys()]
    plt.pie(lista_valores_Tamanhos, labels=lista_chaves, autopct='%1.0f%%')
    plt.title("Tamanhos")
    plt.show()


def faz_grafico_barras(dict_info):
    lista_chaves = [key for key in dict_info.keys()]
    lista_valores_Quantidades = [dict_info[key]['quantidade'] for key in dict_info.keys()]
    plt.bar(lista_chaves, lista_valores_Quantidades)
    plt.title("Quantidades")
    plt.show()

    lista_valores_Tamanhos = [dict_info[key]['size'] for key in dict_info.keys()]
    plt.bar(lista_chaves, lista_valores_Tamanhos)
    plt.title("Tamanhos")
    plt.show()


if __name__ == '__main__':
    # print(pede_pasta())
    #print(faz_calculos(pede_pasta()))
    y = pede_pasta()
    x = faz_calculos(y)
    #print(aux(x))
    guarda_resultados(x)
    faz_grafico_barras(faz_calculos(y))
