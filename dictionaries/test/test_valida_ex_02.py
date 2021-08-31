from dictionaries.ex_02 import dias_da_semana_italiano

def test_valida_dias_da_semana_italiano():
    dia = 'Domingo'

    valida_dias_da_semana_italiano = dias_da_semana_italiano(dia = dia)
    assert valida_dias_da_semana_italiano == 'Domenica'

def test_valida_dias_da_semana_italiano_2():
    dia = 'Sexta-Feira'

    valida_dias_da_semana_italiano = dias_da_semana_italiano(dia = dia)
    assert valida_dias_da_semana_italiano == 'Vernedi'

def test_valida_dias_da_semana_italiano_3():
    dia = 'Quarta Feira'

    valida_dias_da_semana_italiano = dias_da_semana_italiano(dia = dia)
    assert valida_dias_da_semana_italiano == 'Mercoledi'
