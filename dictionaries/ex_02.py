def dias_da_semana_italiano(dia):

    dias_dict = {'Lunedi': ['Segunda','Segunda-Feira','Segunda Feira'], 
                'Martedi': ['Terça','Terça-Feira','Terça Feira'],
                'Mercoledi': ['Quarta', 'Quarta-Feira', 'Quarta Feira'],
                'Giovedi': ['Quinta', 'Quinta-Feira', 'Quinta Feira'],
                'Vernedi': ['Sexta', 'Sexta-Feira', 'Sexta Feira'],
                'Sabato': ['Sábado'],
                'Domenica': ['Domingo']
    }
    


    for chave in dias_dict.keys():
        for dias in dias_dict[chave]:
            if dia == dias:
                return chave

    # dias_dict = {'Segunda': 'Lunedi',
    #             'Segunda-Feira': 'Lunedi',
    #             'Segunda Feira': 'Lunedi'}

    # return dias_dict(dia)