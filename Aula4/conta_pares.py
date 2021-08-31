def conta_pares(lista):
    pares = 0
    for item in lista:
        if item % 2 == 0:
            pares = pares + 1
    return pares

