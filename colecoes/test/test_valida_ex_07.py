from colecoes.ex_07 import junta_listas

def test_valida_junta_listas():
    lista1 = [2,4,6,8]
    lista2 = [1,3,5,7]

    valida_junta_listas = junta_listas(lista1=lista1, lista2=lista2)
    assert valida_junta_listas == [2,1,4,3,6,5,8,7]