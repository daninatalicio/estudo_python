from typing import List



class Produto(object):

    def __init__(self, nome, categoria, valor_unitario):
        self.nome = nome
        self.categoria = categoria
        self.valor_unitario = valor_unitario

class Carrinho(object):

    def __init__(self):
        self.quantidade: int = 0
        self.produtos: List[Produto] = []

    def adiciona_produto(self, produto: Produto):
        self.produtos.append(produto)
        self.quantidade = self.quantidade + 1

    def valor_total(self):
        valor_total = 0
        for produto in self.produtos:
            valor_total = valor_total + produto.valor_unitario
        return valor_total

    



