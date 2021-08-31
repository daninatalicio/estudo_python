def ordena_nomes(nomes):
    nomes_ordenados = {}
    
    for nome in nomes:
        primeira_letra = nome[0].lower()
        lista_de_nomes_por_chave = nomes_ordenados.get(primeira_letra, None) #retorna se tem valor naquela chave
        nao_existe = lista_de_nomes_por_chave == None
        if nao_existe:
            nomes_ordenados[primeira_letra] = [nome] 
        else:
            lista_de_nomes_por_chave.append(nome)
    return nomes_ordenados

            
        



 


#para pegar a primeira letra da string item_lista[0]
#ex Lista = ['Dani','Rafa'] 
#for i in Lista 
#aux = i[0] - na primeira rodada D na segunda R
#depois de pegar a primeira letra olhar se a chave existe no dicionário
# D existe como chave?
#se não, insere e adiciona o item da lista ex > D : Dani
#se sim só adiciona o item na lista onde a chave existe correspondente a letra