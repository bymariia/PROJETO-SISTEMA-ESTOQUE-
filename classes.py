class Cliente:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
    def cadastrar_cliente(self):
        ...
    def listar_cliente(self):
        ...
    def __str__(self):
        return f"Nome: {self.nome} ⋯ ID: {self.id}"

class Sistema:
    def __init__(self):
        #Listas hist. client. prod.  vend.
        ...
    def cadastrar_produto(self):
        ...
    def listar_produtos(self):
        ...
    def realizar_venda(self):
        ...
    def ver_fila_vendas(self):
        ...
    def desfazer_ultima_operacao(self):
        ...
    def exibir_valor_total_vendas(self):
        ...
    
class Produto:
    def __init__(self, nome, preco, quantidade, id):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.id = id
    def __str__(self):
        return f"Nome: {self.nome} ⋯ ID: {self.id} ⋯ Preço: {self.id} ⋯ Quantidade: {self.quantidade}"