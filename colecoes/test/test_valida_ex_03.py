from colecoes.ex_03 import lista_ao_quadrado

def test_valida_lista_ao_quadrado():
    lista_numeros = [2,5,6,10]
    valida_lista_quadrado = lista_ao_quadrado(lista_numeros=lista_numeros)
    assert valida_lista_quadrado == [4,25,36,100]