from poo.carrinho import Carrinho, Produto

def test_valida_criacao_carrinho():
    carrinho = Carrinho()
    assert carrinho.quantidade == 0
    assert carrinho.produtos == []
    
def test_valida_adicionar_produto():
    carrinho = Carrinho()
    produto = Produto('TV', 'Eletrodomestico', 2000)
    carrinho.adiciona_produto(produto)
    produto = carrinho.produtos[0]
    assert produto.nome == 'TV'
    assert produto.categoria == 'Eletrodomestico'
    assert produto.valor_unitario == 2000


   
    
