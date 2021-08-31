from Aula4.encontra_nomes import encontra_nome

def test_encontra_nome_em_lista():
    lista_nomes = ['Rafaelo', 'Mari', 'Dani', 'De']
    nome = 'Dani'
    posicao_na_lista = encontra_nome(lista_nomes = lista_nomes, nome=nome)

    assert posicao_na_lista == 2

def test_nao_encontra_nome_em_lista():
    lista_nomes = ['Rafael', 'Mariane', 'Danielle', 'Denilson']
    nome = 'Danielson'
    posicao_na_lista = encontra_nome(lista_nomes = lista_nomes, nome=nome)

    assert posicao_na_lista == -1


    # def test_nao_encontra_nome_em_lista():
    # lista_nomes = ['Rafael', 'Mariane', 'Danielle', 'Denilson']
    # nome = 'Danielson'
    # posicao_na_lista1 = encontra_nome1(lista_nomes = lista_nomes, nome=nome)
    # posicao_na_lista2 = encontra_nome2(lista_nomes = lista_nomes, nome=nome)

    # assert posicao_na_lista1 == posicao_na_lista2


    #fazermaistestes