from dictionaries.ex_03 import frequencia_palavra

def test_valida_frequencia_palavra():

    frase = 'aprender a aprender é difícil de se aprender mas quando aprender não mais desaprenderá'

    valida_frequencia_palavra = frequencia_palavra(frase=frase)
    assert valida_frequencia_palavra == {'aprender': 4, 'a': 1, 'é': 1,'difícil': 1, 'de': 1, 'se':1, 'mas': 1, 'não': 1, 'mais': 1, "quando": 1, 'desaprenderá': 1}