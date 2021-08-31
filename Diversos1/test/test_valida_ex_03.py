from Diversos1.ex_03 import nome_qtd_letras_2, qtd_nomes_por_tam, nomes_por_letra


def test_valida_qtd_letras():
    nomes = ['Ana', 'Luiz', 'Paulo', 'Cesar', 'Marco', 'Pedro', 'Jodelvan', 'Hélio', 'Lia']
    validar_qtd_letras = nome_qtd_letras_2(nomes = nomes)
    assert validar_qtd_letras == {3: ['Ana', 'Lia'], 4: ['Luiz'], 5: ['Paulo', 'Cesar', 'Marco', 'Pedro', 'Hélio'], 8: ['Jodelvan']}


def test_valida_qtd_nomes():
    tamanho = 5
    nomes = ['Ana', 'Luiz', 'Paulo', 'Cesar', 'Marco', 'Pedro', 'Jodelvan', 'Hélio', 'Lia']
    valida_qtd_nomes = qtd_nomes_por_tam(tamanho = tamanho, nomes = nomes)
    assert valida_qtd_nomes == 5

def test_valida_qtd_nomes_2():
    tamanho = 8
    nomes = ['Ana', 'Luiz', 'Paulo', 'Cesar', 'Marco', 'Pedro', 'Jodelvan', 'Hélio', 'Lia']
    valida_qtd_nomes = qtd_nomes_por_tam(tamanho = tamanho, nomes = nomes)
    assert valida_qtd_nomes == 1

def test_valida_nomes_por_letra():
    letra = 'l'
    nomes = ['Ana', 'Luiz', 'Paulo', 'Cesar', 'Marco', 'Pedro', 'Jodelvan', 'Hélio', 'Lia']
    valida_nomes_por_letra = nomes_por_letra(letra = letra, nomes = nomes)
    assert valida_nomes_por_letra == ['Luiz','Lia']

def test_valida_nomes_por_letra_2():
    letra = 'p'
    nomes = ['Ana', 'Luiz', 'Paulo', 'Cesar', 'Marco', 'Pedro', 'Jodelvan', 'Hélio', 'Lia']
    valida_nomes_por_letra = nomes_por_letra(letra = letra, nomes = nomes)
    assert valida_nomes_por_letra == ['Paulo','Pedro']