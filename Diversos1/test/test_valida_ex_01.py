from Diversos1.ex_01  import romeuejulieta

def test_valida_romeuejulieta():
    carta = 'Dani é legal!'
    n = 3

    validar_romeuejulieta = romeuejulieta(n = n, carta = carta)
    assert validar_romeuejulieta == 'gdql é ohjdo!'
