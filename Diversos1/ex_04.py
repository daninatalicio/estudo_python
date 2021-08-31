# def string_to_calculo(expressao):
#     valores = expressao.split(" ")
#     a = int(valores[0])
#     op = valores[1]
#     b = int(valores[2])
#     if op == '+':
#         resultado = a + b
#     elif op == '-':
#         resultado = a - b
#     elif op == '*':
#         resultado = a * b
#     elif op == '/':
#         resultado = a / b
#     return resultado
    
def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

def mult(a, b):
    return a * b

def expo(a, b):
    return a ** b


operacoes = { 
    '+': sum,
    '-': sub,
    '*': mult,
    '/': div,
    '**': expo
}

    
def string_to_calculo(expressao):

    valores = expressao.split(" ")
    a = int(valores[0])
    op = valores[1]
    b = int(valores[2])

    operacao = operacoes[op]
    resultado = operacao(a, b)
    return resultado




