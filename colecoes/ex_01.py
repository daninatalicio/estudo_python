#progressaoaritmetica a,r - a1, a2 = a1 + r, a3 = a3 + r .. an = a1 + (n-1) * r

def progressao_aritmetica2(n,r): #dani
    ultimo_valor = 0
    x = 1
    lista = []
    for i in range(n):
        ultimo_valor = r + (x-1) * r
        x = x + 1
        lista.insert(i,ultimo_valor) #vc coloca na posição que você quer
    return lista
    

def progressao_aritmetica(n,r): #rafa
    lista = []
    anterior = 0
    for i in range(n):
        atual = anterior + r
        lista.append(atual) #vc coloca no fim da lista
        anterior = atual
    return lista

