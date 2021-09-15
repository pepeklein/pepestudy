class Cliente:
    def__init__(self, nome):
    self.nome = nome


class Produto:
    def__init__(self, descricao, valor):
    self.descricao = descricao
    self.valor = valor


class Carrinho:
    def__init__(self,cliente):
    self.produtos = []


    def adicionar_produto(self, produto):
        self.produtos.append(produto)


    def listar_produtos(self):
        for produto in self.produtos:
            print(produto.descricao, produto.valor)
    

    def calcular_total(self):
        soma = 0
        for produto in self.produtos:
            soma += produto.valor
        return soma


cliente1 = Cliente('Paulo')
produto1 = Produto('Pen Drive', 35.0)
produto2 = Produto('HD Externo', 100.0)
produto3 = Produto('Teclado', 70.0)

carrinho = Carrinho(cliente1)
carrinho.adicionar_produto(produto1)
carrinho.adicionar_produto(produto2)
carrinho.adicionar_produto(produto3)

carrinho.listar_produtos()
print('Total: ', carrinho.calcular_total())
