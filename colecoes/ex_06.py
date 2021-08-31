def maior_palavra2(frase): #dani
    junta_palavras = frase.split()
    maior_palavra = max(junta_palavras, key=len)
    return maior_palavra


def maior_palavra(frase): #rafa
    palavras = frase.split()
    maior = 0
    maior_palavra = ""
    for palavra in palavras:
        tamanho = len(palavra)
        if tamanho > maior:
            maior = tamanho
            maior_palavra = palavra
    return maior_palavra



        
