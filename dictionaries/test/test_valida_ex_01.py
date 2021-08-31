from dictionaries.ex_01 import quantidade_dias

def test_valida_quantidade_dias():
    mes = 'Janeiro'

    valida_quantidade_dias = quantidade_dias(mes = mes)
    assert valida_quantidade_dias == 31

def test_valida_quantidade_dias_2():
    mes = 'Fevereiro'

    valida_quantidade_dias = quantidade_dias(mes = mes)
    assert valida_quantidade_dias == 28
    