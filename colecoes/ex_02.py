def lista_invertida2(lista_numeros): #dani
    tam = len(lista_numeros) - 1
    invertida = []
    i = 0
    while tam >= 0:
        invertida.insert(i,lista_numeros[tam])
        tam = tam - 1
        i = i + 1
    return invertida


def lista_invertida(lista_numeros): #rafa
    invertida = []
    for item in lista_numeros: #item qnd coloca range ai é a posição
        invertida.insert(0,item)
    return invertida

 

