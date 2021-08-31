def check_doors_2(n):
    lista_portas = []
    i = 0
    posicao = 1
    while i < n:
        lista_portas.insert(i,1)
        i = i + 1
    for item in lista_portas:
        if posicao % 2 == 0:
            item = 0
            posicao = posicao + 1
        else:
            posicao = posicao + 1
    return lista_portas

    
def check_doors_2(n):
    lista_portas = []
    for i in range(n):
        pos = i + 1
        lista_portas.append(1)
        if pos % 2 == 0:
           lista_portas[i] = inverte_porta(porta=lista_portas[i])
        if pos % 3 == 0:
           lista_portas[i] = inverte_porta(porta=lista_portas[i])
    return lista_portas


# def check_doors(n):
#    doors = [False] * n
#     for i in range(n):
#         for j in range(i, n, i+1):
#             doors[j] = not doors[j]
#     return doors


def check_doors(n):
    doors = [False] * (n + 1)  
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            print(f'{i}: {not doors[j]}')
            doors[j] = not doors[j]  
    return doors


def inverte_porta(porta):
   return abs(porta-1)
  
