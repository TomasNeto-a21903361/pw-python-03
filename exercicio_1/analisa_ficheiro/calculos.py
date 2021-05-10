import string


def calcula_linhas(nome):
    file = open(nome, "r")
    count = 0

    start = file.read()
    content = start.split("\n")

    for i in content:
        if i:
            count += 1
    return count

def calcula_carateres(nome):
    file = open(nome, "r")
    count = 0

    start = file.read()

    for line in start:
        count += len(line)
    return count

def calcula_palavra_comprida(nome):
    with open(nome, 'r+') as file:
        words = file.read().split()
        max_len_word = max(words, key=len)
        return max_len_word

def calcula_ocorrencia_de_letras(nome):
    res = {}
    with open(nome, 'r') as f:
        for line in f:
            for letter in line.lower():
                if letter in res:
                    res[letter] += 1
                else:
                    res[letter] = 1
    return res



#if __name__ == '__main__':
    #print(calcula_linhas("dados.txt"))
    #print(calcula_carateres("dados.txt"))
    #print(calcula_palavra_comprida("dados.txt"))
    #print(calcula_ocorrencia_de_letras("dados.txt"))
