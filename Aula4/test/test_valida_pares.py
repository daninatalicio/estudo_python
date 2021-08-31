from Aula4.conta_pares import conta_pares


def test_conta_pares_lista_so_impar():
    lista = [3, 7, 9]
    resultado = conta_pares(lista)
    assert resultado == 0

def test_conta_pares_lista_mista():
    lista = [3, 7, 9, 10, 11]
    resultado = conta_pares(lista)
    assert resultado == 1

def test_conta_pares_lista_so_pares():
    lista = [2, 4, 6, 8, 10, 12]
    resultado = conta_pares(lista)
    assert resultado == 6