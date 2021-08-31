from dictionaries.ex_05 import ordena_nomes

def test_valida_ordena_nomes():

    # nomes = ['Dani','Rafa','Denise']
    nomes = ['Ana','Bruno','Alberto','Caio','Bia','Dani','Denilson']

    valida_ordena_nomes = ordena_nomes(nomes = nomes)
    # assert valida_ordena_nomes == {'D':['Dani','Denise'],'R':['Rafa']}
    assert valida_ordena_nomes == {'a': ['Ana', 'Alberto'], 'b':['Bruno', 'Bia'], 'c':['Caio'], 'd': ['Dani','Denilson']}