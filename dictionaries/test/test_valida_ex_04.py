from dictionaries.ex_04 import numeros_nao_repetem

def test_valida_numeros_nao_repetem():

    lista1 = [1,3,5,7]
    lista2 = [1,2,3,9]

    valida_numeros_nao_repetem = numeros_nao_repetem(lista1 = lista1, lista2 = lista2)
    assert valida_numeros_nao_repetem == [2,5,7,9]