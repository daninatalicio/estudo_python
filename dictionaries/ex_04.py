def numeros_nao_repetem(lista1,lista2):
    count_by_itens = {}
    lista_final = []

    for item in lista1:
        count_by_itens[item] = 1
           
    for item in lista2:
        count = count_by_itens.get(item, 0)
        count = count + 1
        count_by_itens[item] = count

    for chave, valor in count_by_itens.items():
        if valor == 1:
            lista_final.append(chave)
    
    # for chave in count_by_itens.keys():
    #     valor = count_by_itens[chave]
    #     if valor == 1:
    #         lista_final.append(chave)
    
    lista_final.sort()

    return lista_final


  
