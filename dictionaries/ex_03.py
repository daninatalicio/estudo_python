def frequencia_palavra(frase):

    palavras_separadas = frase.split(" ")
    conts = dict()
    for i in palavras_separadas: 
        conts[i] = conts.get(i,0) + 1
    return conts