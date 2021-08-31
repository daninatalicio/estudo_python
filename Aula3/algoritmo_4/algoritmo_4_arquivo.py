
def _sum(a, b):
    return a + b

def _sub(a, b):
    return a - b

def _div(a, b):
    is_valid = valida_se_divisao_por_zero(b)
    if (is_valid == True):
        return a / b
    else:
        raise Exception('Divisão por zero é inválida')


def _mult(a, b):
    return a * b 

def execucao(a, b, operacao):
    if operacao == '+':
        return _sum(a, b)
    elif operacao == '-':
        return _sub(a, b)
    elif operacao == '*':
        return _mult(a, b)
    elif operacao == '/':
        return _div(a, b)


def valida_se_divisao_por_zero(b):
    validacao = True
    if (b != 0):
        return validacao
    else:
        return False