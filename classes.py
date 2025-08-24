from recursos import Fila, Pilha
from defs import erro
class Cliente:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
   
    def __str__(self):
        return f"Nome: {self.nome} ⋯ ID: {self.id}"
   
class Produto:
    def __init__(self, nome, preco, quantidade, id):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.id = id
    def __str__(self):
        return f"Nome: {self.nome} ⋯ ID: {self.id} ⋯ Preço: {self.preco} ⋯ Quantidade: {self.quantidade}"
   
class Sistema:
    def __init__(self):
        self.clientes = {}
        self.produtos = {}
        self.fila_vendas = Fila()
        self.pilha_operacoes = Pilha()
   
    def cadastrar_cliente(self, nome, id):
        cliente = Cliente(nome, id)
        self.clientes[id] = cliente
        self.pilha_operacoes.empilhar(("cliente", cliente))
       
    def listar_cliente(self):
        if not self.clientes:
            erro("Nenhum cliente cadastrado.")
            return
        for cliente in self.clientes.values():
            print(cliente)
    def cadastrar_produto(self, nome, preco, quantidade, id):
        produto = Produto(nome, preco, quantidade, id)
        self.produtos[id] = (produto)
        self.pilha_operacoes.empilhar(("produto", produto))


    def listar_produtos(self):
        if not self.produtos:
            erro("Nenhum produto cadastrado.")
            return
        for produto in self.produtos.values():
            print(produto)


    def realizar_venda(self):


        #Verificar se tem produtos e clientes cadastrados
        if not self.produtos:
            erro("Nenhum produto cadastrado.")
            return
        if not self.clientes:
            erro("Nenhum cliente cadastrado.")
            return


        #Verificar se os clientes e produtos existem
        id_cliente = input("Digite o ID do cliente: ")
        if id_cliente not in self.clientes:
            erro("Cliente inexistente.")
            return


        cliente = self.clientes[id_cliente]


        id_produto = input("Digite o ID do produto: ")
        if id_produto not in self.produtos:
            erro("Produto inexistente.")
            return
        produto = self.produtos[id_produto]


        quantidade_vendida = int(input("Digite a quantidade: "))


        #Verificar se a quantidade do produto existe
        if quantidade_vendida > produto.quantidade:
            erro("Quantidade insuficiente.")
            return
        #Remover a quantidade do produto do estoque
        produto.quantidade -= quantidade_vendida


        #somar preço
        preco_total = produto.preco * quantidade_vendida


        #adicionar a venda na fila
        venda = (cliente, produto, quantidade_vendida, preco_total)
        self.fila_vendas.enfileirar(venda)
        self.pilha_operacoes.empilhar(("venda", venda))
       
        print(f"Venda do produto {produto.nome} e ID {produto.id} com quantidade {quantidade_vendida} realizada para o cliente {cliente.nome} no total de R${preco_total} reais.")
       


    def ver_fila_vendas(self):
        if self.fila_vendas.esta_vazia():
            erro("Nenhuma venda realizada.")
            return
        print("Fila de vendas:")
        self.fila_vendas.listar()
       
    def desfazer_ultima_operacao(self):
        if self.pilha_operacoes.esta_vazia():
            erro("Nenhuma operação realizada.")
            return
        operacao = self.pilha_operacoes.desempilhar()
        if operacao[0] == "cliente":
            del self.clientes[operacao[1].id]
        elif operacao[0] == "produto":
            del self.produtos[operacao[1].id]
        elif operacao[0] == "venda":
            venda = operacao[1]
            produto = venda[1]
            produto.quantidade += venda[2]


        print(f"Operação {operacao[0]} desfeita.")
    def exibir_valor_total_vendas(self):
        total = 0
        for venda in self.fila_vendas.itens:
            total += venda[3]
        print(f"Valor total de vendas: R${total} reais.")

    def __str__(self):
        return f"Clientes: {self.clientes} Produtos: {self.produtos} Fila de vendas: {self.fila_vendas} Pilha de operações: {self.pilha_operacoes}"