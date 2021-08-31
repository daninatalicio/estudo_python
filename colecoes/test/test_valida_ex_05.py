from colecoes.ex_05 import conta_letras

def test_valida_quantidade_letras():
    frase = "Dani é uma excelente aluna"
    valida_conta_letras = conta_letras(frase=frase)
    assert valida_conta_letras == 22

def test_valida_quantidade_letras_2():
    frase = "Rafa fofo"
    valida_conta_letras = conta_letras(frase=frase)
    assert valida_conta_letras == 8