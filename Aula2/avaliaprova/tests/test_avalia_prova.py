from avaliaprova.avalia_prova_arquivo import avalia_prova
import pytest

def test_avalia_prova_todas_questoes_erradas():
    r1 = 'a'
    r2 = 'a'
    r3 = 'a'
    g1 = 'b'
    g2 = 'c'
    g3 = 'd'

    resultado = avalia_prova(r1=r1, r2=r2, r3=r3, g1=g1, g2=g2, g3=g3)
    assert resultado == 0



def test_avalia_prova_com_1_acerto():
    r1, r2, r3, = 'a', 'b', 'c'
    g1, g2, g3 = 'c', 'b', 'a'

    resultado = avalia_prova(r1=r1, r2=r2, r3=r3, g1=g1, g2=g2, g3=g3)
    assert resultado == 1


def test_avalia_prova_com_2_acertos():
    r1, r2, r3, = 'a', 'b', 'c'
    g1, g2, g3 = 'a', 'b', 'a'

    resultado = avalia_prova(r1=r1, r2=r2, r3=r3, g1=g1, g2=g2, g3=g3)
    assert resultado == 2

def test_avalia_prova_com_3_acertos():
    r1, r2, r3, = 'a', 'b', 'c'
    g1, g2, g3 = 'a', 'b', 'c'

    resultado = avalia_prova(r1=r1, r2=r2, r3=r3, g1=g1, g2=g2, g3=g3)
    assert resultado == 3


def test_avalia_prova_com_tipo_invalido_r1():
    r1, r2, r3, = 1, 'b', 'c'
    g1, g2, g3 = '1', 'b', 'c'
    _valida_casos_erro(r1, r2, r3, g1, g2, g3)

def test_avalia_prova_com_tipo_invalido_r2():
    r1, r2, r3, = '1', 3, 'c'
    g1, g2, g3 = '1', '3', 'c'
    _valida_casos_erro(r1, r2, r3, g1, g2, g3)

def test_avalia_prova_com_tipo_invalido_r3():
    r1, r2, r3, = '1', '3', 4
    g1, g2, g3 = '1', '3', '4'
    _valida_casos_erro(r1, r2, r3, g1, g2, g3)

def test_avalia_prova_com_tipo_invalido_r1_r2():
    r1, r2, r3, = 1, 3, '4'
    g1, g2, g3 = '1', '3', '4'
    _valida_casos_erro(r1, r2, r3, g1, g2, g3)

def test_avalia_prova_com_tipo_invalido_r1_r3():
    r1, r2, r3, = 1, '3', 4
    g1, g2, g3 = '1', '3', '4'
    _valida_casos_erro(r1, r2, r3, g1, g2, g3)

def test_avalia_prova_com_tipo_invalido_r2_r3():
    r1, r2, r3, = '1', 3, 4
    g1, g2, g3 = '1', '3', '4'
    _valida_casos_erro(r1, r2, r3, g1, g2, g3)

def test_avalia_prova_com_tipo_invalido_r1_r2_r3():
    r1, r2, r3, = 1, 3, 4
    g1, g2, g3 = '1', '3', '4'
    _valida_casos_erro(r1, r2, r3, g1, g2, g3)

def _valida_casos_erro(r1, r2, r3, g1, g2, g3):
    with pytest.raises(Exception):
        avalia_prova(r1=r1, r2=r2, r3=r3, g1=g1, g2=g2, g3=g3)






#colocar validação gabaritos