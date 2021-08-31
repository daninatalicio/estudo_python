from colecoes.ex_09 import gera_combinacoes

def test_valida_gerar_combinacoes():
    lista1 = ['A','B']
    lista2 = ['C','D','E']

    valida_gerar_combinacoes = gera_combinacoes(lista1 = lista1, lista2 = lista2)
    assert valida_gerar_combinacoes == ['AC', 'AD', 'AE', 'BC', 'BD', 'BE']

def test_valida_gerar_combinacoes_2():
    lista1 = ['A','B','X']
    lista2 = ['C','D','E']

    valida_gerar_combinacoes_2 = gera_combinacoes(lista1 = lista1, lista2 = lista2)
    assert valida_gerar_combinacoes_2 == ['AC', 'AD', 'AE', 'BC', 'BD', 'BE','XC','XD','XE']

def test_valida_gerar_combinacoes_3():
    lista1 = ['A','B','X']
    lista2 = ['C','D']

    valida_gerar_combinacoes_3 = gera_combinacoes(lista1 = lista1, lista2 = lista2)
    assert valida_gerar_combinacoes_3 == ['AC', 'AD', 'BC', 'BD','XC','XD']