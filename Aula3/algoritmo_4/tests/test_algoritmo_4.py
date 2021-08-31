from algoritmo_4.algoritmo_4_arquivo import execucao
import pytest


def test_multiplicacao():
    a = 2
    b = 4
    resultado = execucao(a=a, b=b, operacao='*')
    assert resultado == 8

def test_soma_valida():
    a = 2
    b = 19
    resultado = execucao(a=a, b=b, operacao='+')
    assert resultado == 21

def test_subtracao():
    a = 2
    b = 10
    resultado = execucao(a=a, b=b, operacao='-')
    assert resultado == -8


def test_divisao():
    a = 100
    b = 10
    resultado = execucao(a=a, b=b, operacao='/')
    assert resultado == 10


def test_divisao_por_zero():
    a = 100
    b = 0
    with pytest.raises(Exception):
        execucao(a=a, b=b, operacao='/')

		
