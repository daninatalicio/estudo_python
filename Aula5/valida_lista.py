# def sao_diferentes(nomes_1,nomes_2):
#     for i in range(len(nomes_1)):
#         if nomes_1[i] != nomes_2[i]:
#             return True
#     return False


def sao_diferentes(nomes_1,nomes_2):
    posicao = 0
    while posicao < (len(nomes_1)):
        if nomes_1[posicao] != nomes_2[posicao]:
            return True
        else:
            posicao = posicao + 1
    return False


def sao_iguais(lista_1,lista_2):
    posicao = 0
    while posicao <= (len(lista_1) -1):
        if lista_1[posicao] == lista_2[posicao]:
           posicao = posicao + 1
        else:
            return False
    return True
 

    ##for > quando preciso percorrer a lista toda
    ##while > quando não precisa percorrer a lista toda

    #fazer com while
    #fazerumalgoritmoparaverseestãoiguais