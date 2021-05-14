from exercicio_2 import analise_pasta

if __name__ == '__main__':
    # print(analise_pasta.pede_pasta())
    # print(analise_pasta.faz_calculos(analise_pasta.pede_pasta()))
    x = analise_pasta.faz_calculos(analise_pasta.pede_pasta())
    analise_pasta.guarda_resultados(x)
    analise_pasta.faz_grafico_barras(x)
    analise_pasta.faz_grafico_queijos(x)
