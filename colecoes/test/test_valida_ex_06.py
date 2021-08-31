from colecoes.ex_06 import maior_palavra

def test_valida_maior_palavra():
    frase = "Dani é uma excelente aluna"
    valida_maior_palavra = maior_palavra(frase=frase)
    assert valida_maior_palavra == 'excelente'

def test_valida_maior_palavra_2():
    frase = "Rafaello é muito fofoooooooooooooooo"
    valida_maior_palavra = maior_palavra(frase=frase)
    assert valida_maior_palavra == 'fofoooooooooooooooo'