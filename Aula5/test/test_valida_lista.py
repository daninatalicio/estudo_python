from Aula5.valida_lista import sao_diferentes, sao_iguais

def test_sao_diferentes_com_listas_iguais():
    nomes_1 = ['Maria', 'Luiza', 'Juliette']
    nomes_2 = ['Maria', 'Luiza', 'Juliette']

    listas_diferentes = sao_diferentes(nomes_1=nomes_1, nomes_2=nomes_2)
    assert listas_diferentes == False
    

def test_sao_diferentes_com_listas_diferentes():
    nomes_1 = ['Maria', 'Pedro', 'Juliette']
    nomes_2 = ['Maria', 'Mylena', 'Juliette']

    listas_diferentes = sao_diferentes(nomes_1=nomes_1, nomes_2=nomes_2)
    assert listas_diferentes == True

def test_sao_iguais_com_listas_iguais():
    lista_1 = ['Maria', 'Luiza', 'Juliette']
    lista_2 = ['Maria', 'Luiza', 'Juliette']

    listas_iguais = sao_iguais(lista_1=lista_1, lista_2=lista_2)
    assert listas_iguais == True
    

def test_sao_iguais_com_listas_diferentes():
    lista_1 = ['Maria', 'Pedro', 'Juliette']
    lista_2 = ['Maria', 'Mylena', 'Juliette']

    listas_iguais = sao_iguais(lista_1=lista_1, lista_2=lista_2)
    assert listas_iguais == False
