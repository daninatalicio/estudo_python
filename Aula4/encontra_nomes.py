#def encontra_nome(lista_nomes,nome):
#   posicao = 0
#   for item in lista_nomes:
#       if item == nome:
#             return posicao
#      else:
#           posicao = posicao + 1
#   if posicao > (len(lista_nomes) -1) :
#       return -1
#   return posicao        



def encontra_nome(lista_nomes,nome):
    posicao = 0
    while posicao <= (len(lista_nomes) -1):
        if nome == lista_nomes[posicao]:
            return posicao
        else:
           posicao = posicao + 1
   return -1

    
def encontra_nome(lista_nomes,nome):
    for i in range(0, len(lista_nomes)):
        if nome == lista_nomes[i]:
            return i
    return -1




#while, #for i in range(0, len(lista_nomes)):

#arrumarnomesparanãocomentar