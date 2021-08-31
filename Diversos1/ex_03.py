# def nome_qtd_letras(nomes):

#     dic_final = {}
   
#     for index in nomes:
#         tamanho = len(index)
#         nao_existe = dic_final.get(tamanho,None)  #existe = tamanho in dic_final
#         if nao_existe is None:
#             lista_nome = []
#             lista_nome.append(index)
#             dic_final[tamanho] = lista_nome
#         else:
#             dic_final.setdefault(tamanho, []).append(index)                     

#     return dic_final
       

def nome_qtd_letras_2(nomes):

    tamanho_to_nomes = {}
   
    for nome in nomes:
        tamanho = len(nome)
        lista_nomes = tamanho_to_nomes.get(tamanho,None)
        if lista_nomes is None:
            lista_nova = []
            lista_nova.append(nome)
            tamanho_to_nomes[tamanho] = lista_nova
        else:
            lista_nomes.append(nome)                

    return tamanho_to_nomes


        
def qtd_nomes_por_tam(nomes,tamanho):

    dic = nome_qtd_letras_2(nomes)
    list_nomes = dic[tamanho]
    qtd = len(list_nomes)

    return qtd


def nomes_por_letra(nomes,letra):

    lista_nomes = []
        
    for nome in nomes:
        primeira_letra = nome[0].lower()
        if letra == primeira_letra:
            lista_nomes.append(nome)
    return lista_nomes







    
   

