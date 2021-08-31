from colecoes.ex_02 import lista_invertida

def test_valida_lista_ivertida():
    lista_numeros = [1,2,3,4]
    valida_lista = lista_invertida(lista_numeros=lista_numeros)
    assert valida_lista == [4,3,2,1]

