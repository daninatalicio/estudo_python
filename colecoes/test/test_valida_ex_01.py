from colecoes.ex_01 import progressao_aritmetica

def test_valida_progressao_aritmetica():
    n = 4
    r = 3
    valida_progressao = progressao_aritmetica(n=n, r=r)
    assert valida_progressao == [3,6,9,12]

def test_valida_progressao_aritmetica_2():
    n = 7
    r = 9
    valida_progressao = progressao_aritmetica(n=n, r=r)
    assert valida_progressao == [9,18,27,36,45,54,63]

def test_valida_progressao_aritmetica_3():
    n = 7
    r = 9
    valida_progressao = progressao_aritmetica(n=n, r=r)
    assert type(valida_progressao) == list #inferir o tipo que tá vindo
    assert valida_progressao == [9,18,27,36,45,54,63]