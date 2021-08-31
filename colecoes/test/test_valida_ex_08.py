from colecoes.ex_08 import nao_se_repetem

def test_valida_nao_se_repetem():
    lista1 = [1,3,5,7]
    lista2 = [1,2,3,9]

    valida_nao_se_repetem = nao_se_repetem(lista1 = lista1, lista2 = lista2)
    assert valida_nao_se_repetem == [5,7,2,9]
