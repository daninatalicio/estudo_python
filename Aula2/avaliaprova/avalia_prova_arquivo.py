def avalia_prova(r1, r2, r3, g1, g2, g3):
    is_valid = valida_type_string(r1, r2, r3, g1, g2, g3)
    if (is_valid == True):
        acertos = 0
        if (r1 != g1 and r2 != g2 and r3 != g3):
            return acertos
        else:
            if r1==g1:
                acertos = acertos + 1
            if r2==g2:
                acertos = acertos + 1
            if r3==g3:
                acertos = acertos + 1
            return acertos
    else:
        raise Exception('Erro tipo inválido no parâmetro')

def valida_type_string(r1, r2, r3, g1, g2, g3):
    validacao = True
    if (type(r1) == str and type(r2) == str and type(r3) == str ):
        return validacao
    else:
        return False

    

