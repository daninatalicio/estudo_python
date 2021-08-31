def nao_se_repetem(lista1,lista2):
    lista_final = []
    tam = len(lista1)
    for item in lista1:
        i = 0
        repete = False
        while i < tam and repete == False:
            if item == lista2[i]:
               repete = True
            i = i + 1
        if repete == False:
            lista_final.append(item)
    for item in lista2:
        i = 0
        repete = False
        while i < tam and repete == False:
            if item == lista1[i]:
               repete = True
            i = i + 1
        if repete == False:
            lista_final.append(item)
    return lista_final

