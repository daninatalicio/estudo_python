from Diversos1.ex_02  import media_notas, media_notas2

def test_valida_media_notas():
    disciplinas = ['Matematica','Fisica','Portugues','Portugues','Matematica','Fisica','Matematica']
    notas = [7.5, 9.5, 4.5, 6.5, 10, 5.0, 3.5]

    validar_media_notas = media_notas(disciplinas = disciplinas, notas = notas)
    assert validar_media_notas['Matematica'] == 7.0
    assert validar_media_notas['Portugues'] == 5.5
    assert validar_media_notas['Fisica'] == 7.25


def test_valida_media_notas_2():
    disciplinas = ['Matematica','Fisica','Portugues','Portugues','Matematica','Fisica','Matematica']
    notas = [7.5, 9.5, 4.5, 6.5, 10, 5.0, 3.5]

    validar_media_notas = media_notas2(disciplinas = disciplinas, notas = notas)
    assert validar_media_notas['Matematica'] == 7.0
    assert validar_media_notas['Portugues'] == 5.5
    assert validar_media_notas['Fisica'] == 7.25
