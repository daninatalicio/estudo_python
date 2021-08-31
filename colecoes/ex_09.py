def gera_combinacoes_old(lista1,lista2):
    lista_final = []
    tam = len(lista2)
    for item in lista1:
        i = 0
        while i < tam:
            lista_final.append(item + lista2[i])
            i = i + 1
    return lista_final


def gera_combinacoes(lista1, lista2):
    lista_final = []
    for item in lista1:
        for i in lista2:
            lista_final.append(item + i)
    return lista_final
     