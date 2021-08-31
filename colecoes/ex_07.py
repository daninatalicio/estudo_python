def junta_listas_2(lista1,lista2):  #dani
    listas_juntas = lista1 + lista2
    lista_ordenada = sorted(listas_juntas)
    return lista_ordenada

def junta_listas(lista1,lista2):  #rafa
    lista_nova = []
    for i in range(len(lista1)):
        lista_nova.append(lista1[i])
        lista_nova.append(lista2[i])
    return lista_nova

