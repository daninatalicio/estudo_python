from colecoes.ex_04 import conta_palavras

def test_valida_conta_palavras():
    frase = "Dani é uma excelente aluna"
    valida_conta_palavras = conta_palavras(frase=frase)
    assert valida_conta_palavras == 5

def test_valida_conta_palavras_2():
    frase = "O Rafa é fofo"
    valida_conta_palavras = conta_palavras(frase=frase)
    assert valida_conta_palavras == 4

def test_valida_conta_palavras_3():
    frase = "Oi"
    valida_conta_palavras = conta_palavras(frase=frase)
    assert valida_conta_palavras == 1