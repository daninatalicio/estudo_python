from Diversos1.ex_04 import string_to_calculo

def test_valida_string_to_calculo_soma():
    expressao = '10 + 9'
    
    valida_string_to_calculo = string_to_calculo(expressao = expressao)
    assert valida_string_to_calculo == 19

def test_valida_string_to_calculo_multiplicacao():
    expressao = '9 * 11'
    
    valida_string_to_calculo = string_to_calculo(expressao = expressao)
    assert valida_string_to_calculo == 99

def test_valida_string_to_calculo_subtracao():
    expressao = '11 - 2'
    
    valida_string_to_calculo = string_to_calculo(expressao = expressao)
    assert valida_string_to_calculo == 9


def test_valida_string_to_calculo_divisao():
    expressao = '100 / 10'
    
    valida_string_to_calculo = string_to_calculo(expressao = expressao)
    assert valida_string_to_calculo == 10

def test_valida_string_to_calculo_expo():
    expressao = '2 ** 3'
    
    valida_string_to_calculo = string_to_calculo(expressao = expressao)
    assert valida_string_to_calculo == 8