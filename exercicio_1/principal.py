from exercicio_1 import analisa_ficheiro
import json

if __name__ == '__main__':
    #analisa_ficheiro.calcula_linhas("dados.txt")
    #analisa_ficheiro.calcula_carateres("dados.txt")
    #analisa_ficheiro.calcula_palavra_comprida("dados.txt")
    #analisa_ficheiro.calcula_ocorrencia_de_letras("dados.txt")
    #analisa_ficheiro.pede_nome()
    #analisa_ficheiro.gera_nome("dados.txt")
    xd = analisa_ficheiro.gera_nome(analisa_ficheiro.pede_nome())

    with open(xd, 'w', encoding='utf8') as f:
        f.write("Nome do ficheiro: " + str(analisa_ficheiro.gera_nome("dados.txt")))
        f.write("\n")
        f.write("Número total de linhas: " + str(analisa_ficheiro.calcula_linhas("dados.txt")))
        f.write("\n")
        f.write("Número total de caracteres: " + str(analisa_ficheiro.calcula_carateres("dados.txt")))
        f.write("\n")
        f.write("Palavra mais comprida do ficheiro: " +str(analisa_ficheiro.calcula_palavra_comprida("dados.txt")))
        f.write("\n")
        f.write("Dicionário da ocorrência das letras: " + str(analisa_ficheiro.calcula_ocorrencia_de_letras("dados.txt")))
        f.write("\n")
        json.dump("---Stats---", f)
