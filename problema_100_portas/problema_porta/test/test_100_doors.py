from problema_porta.doors import check_doors

def test_100_doors():
    n = 6
    lista_portas = check_doors(n)
    assert lista_portas == [False,True,True,True,False,False]



