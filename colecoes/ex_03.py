def lista_ao_quadrado2(lista_numeros): #dani
    lista = []
    i = 0
    while i <= len(lista_numeros) -1 :
        num = lista_numeros[i] ** 2
        lista.insert(i,num)
        i = i + 1
    return lista


def lista_ao_quadrado(lista_numeros): #rafa
    lista = []
    for i in lista_numeros:
        lista.append(i ** 2)
    return lista

