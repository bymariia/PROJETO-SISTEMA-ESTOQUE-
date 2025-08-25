import os
from recursos import Fila, Pilha
from defs import erro, acerto

class Cliente:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
        self.total_gasto = 0
   
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
    
class Venda:
    def __init__(self, cliente, produto, quantidade, total):
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade
        self.total = total
    
    def __str__(self):
        return f"Venda: {self.quantidade}x {self.produto.nome} para {self.cliente.nome} ⋯ Total: R${self.total:.2f}"

   
class Sistema:
    def __init__(self):
        self.clientes = {}
        self.produtos = {}
        self.fila_vendas = Fila()
        self.pilha_operacoes = Pilha()
   
    def cadastrar_cliente(self, nome, id):
        if id in self.clientes:
            erro("ID ja cadastrado.")
            return False
        cliente = Cliente(nome, id)
        self.clientes[id] = cliente
        self.pilha_operacoes.empilhar(("cliente", cliente))
        acerto(f"Cliente '{nome}' cadastrado com sucesso!")
        return True
       
    def listar_cliente(self):
        if not self.clientes:
            erro("Nenhum cliente cadastrado.")
            return
        for cliente in self.clientes.values():
            print(cliente)

    def cadastrar_produto(self, nome, preco, quantidade, id):
        if id in self.produtos:
            erro("ID ja cadastrado.")
            return False
        produto = Produto(nome, preco, quantidade, id)
        self.produtos[id] = produto
        self.pilha_operacoes.empilhar(("produto", produto))
        return True

    def listar_produtos(self):
        if not self.produtos:
            erro("Nenhum produto cadastrado.")
            return []
        for p in self.produtos.values():
            print(p)
        return list(self.produtos.values())
    
    def total_estoque(self):
        return sum(p.preco * p.quantidade for p in self.produtos.values())

    def realizar_venda(self):
        #Verificar se tem produtos/clientes cadastrados:
        if not self.produtos:
            erro("Nenhum produto cadastrado.")
            return False
        if not self.clientes:
            erro("Nenhum cliente cadastrado.")
            return False

        #Verificar se os clientes/produtos existem:
        id_cliente = input(" ↪︎ Digite o ID do cliente: ")
        if id_cliente not in self.clientes:
            erro("Cliente inexistente.")
            return False
        cliente = self.clientes[id_cliente]

        id_produto = input(" ↪︎ Digite o ID do produto: ")
        if id_produto not in self.produtos:
            erro("Produto inexistente.")
            return False
        produto = self.produtos[id_produto]

        try:
            quantidade_vendida = int(input(" ↪︎ Digite a quantidade: "))
        except ValueError:
            erro("Quantidade inválida.")
            return False
        
        #Verificar se a quantidade do produto existe:
        if quantidade_vendida > produto.quantidade:
            erro("Quantidade insuficiente.")
            return False
        #Remover a quantidade do produto do estoque:
        produto.quantidade -= quantidade_vendida

        #somar preço:
        preco_total = produto.preco * quantidade_vendida

        #atualizar o total do cliente:
        cliente.total_gasto += preco_total

        #adicionar a venda na fila:
        venda = Venda(cliente, produto, quantidade_vendida, preco_total)
        self.fila_vendas.enfileirar(venda)
        self.pilha_operacoes.empilhar(("venda", venda))

        return True
    
    def ver_fila_vendas(self):
        if self.fila_vendas.esta_vazia():
            erro("Nenhuma venda realizada.")
            return
        print(" ↪︎ Fila de vendas:")
        self.fila_vendas.listar()
       
    def desfazer_ultima_operacao(self):
        if self.pilha_operacoes.esta_vazia():
            erro("Nenhuma operação realizada.")
            return
        
        operacao_tipo, objeto_operado = self.pilha_operacoes.desempilhar()

        if operacao_tipo == "cliente":
            del self.clientes[objeto_operado.id]
            acerto(f"Cadastro de cliente '{objeto_operado.nome}' desfeito.")
        elif operacao_tipo == "produto":
            del self.produtos[objeto_operado.id]
            acerto(f"Cadastro de produto '{objeto_operado.nome}' desfeito.")
        elif operacao_tipo == "venda":
            venda = objeto_operado
            produto = venda.produto
            produto.quantidade += venda.quantidade
            venda.cliente.total_gasto -= venda.total
            try:
                if venda in self.fila_vendas.itens:
                    self.fila_vendas.itens.remove(venda)
            except ValueError:
                erro("Venda inexistente.")
            acerto(f"Venda de '{venda.cliente.nome}' para '{venda.produto.nome}' desfeita.")
        print(f"Operação {operacao_tipo} desfeita.")

    def exibir_valor_total_vendas(self):
        total = 0
        for venda in self.fila_vendas.itens:
            total += venda.total
        print(f"Valor total de vendas: R${total:.2f} reais.")

    def salvar_dados(self, clientes_path="clientes.txt", produtos_path="produtos.txt", vendas_path="vendas.txt"):

        #salvar clientes
        try:
            with open(clientes_path, "w", encoding="utf-8") as arquivo:
                for id, cliente in self.clientes.items():
                    arquivo.write(f"{cliente.id},{cliente.nome},{cliente.total_gasto}\n")
            acerto(f"Clientes salvos em '{clientes_path}'.")
        except IOError as e:
            erro(f"Erro ao salvar clientes: {e}")

        #salvar produtos
        try:
            with open(produtos_path, "w", encoding="utf-8") as arquivo:
                for id, produto in self.produtos.items():
                    arquivo.write(f"{produto.id},{produto.nome},{produto.preco},{produto.quantidade}\n")
            acerto(f"Produtos salvos em '{produtos_path}'.")
        except IOError as e:
            erro(f"Erro ao salvar produtos: {e}")

        #salvar vendas
        try:
            with open(vendas_path, "w", encoding="utf-8") as arquivo:
                for venda in self.fila_vendas.itens:
                    arquivo.write(f"{venda.cliente.id},{venda.produto.id},{venda.quantidade},{venda.total}\n")
            acerto(f"Vendas salvas em '{vendas_path}'.")
        except IOError as e:
            erro(f"Erro ao salvar vendas: {e}")

    def carregar_dados_arquivos(self, clientes_path="clientes.txt", produtos_path="produtos.txt", vendas_path="vendas.txt"):

        # carregar clientes
        if os.path.exists(clientes_path):
            try:
                with open(clientes_path, "r", encoding="utf-8") as arquivo:
                    for linha in arquivo:
                        partes = linha.strip().split(",")
                        if len(partes) == 3:
                            cliente_id, nome, gasto = partes
                            cliente = Cliente(nome, cliente.id)
                            cliente.total_gasto = float(gasto)
                            self.clientes[cliente_id] = cliente
                acerto(f"Clientes carregados do arquivo '{clientes_path}'.")
            except (IOError, ValueError) as e:
                erro(f"Erro ao carregar clientes de '{clientes_path}': {e}. Verifique o formato do arquivo.")
        else:
            print(" ↪︎ Nenhum arquivo de clientes encontrado. Iniciando com clientes vazios.")


        # carregar produtos
        if os.path.exists(produtos_path):
            try:
                with open(produtos_path, 'r', encoding='utf-8') as arquivo:
                    for linha in arquivo:
                        partes = linha.strip().split(',')
                        if len(partes) == 4:
                            id_produto, nome, preco_str, quantidade_str = partes
                            produto = Produto(nome, float(preco_str), int(quantidade_str), id_produto)
                            self.produtos[id_produto] = produto
                acerto(f"Dados de produtos carregados de '{produtos_path}'.")
            except (IOError, ValueError) as e:
                erro(f"Erro ao carregar produtos de '{produtos_path}': {e}. Verifique o formato do arquivo.")
        else:
            print(" ↪︎ Nenhum arquivo de produtos encontrado. Iniciando com produtos vazios.")

        # Carregar vendas
        if os.path.exists(vendas_path):
            try:
                with open(vendas_path, 'r', encoding='utf-8') as arquivo:
                    for linha in arquivo:
                        partes = linha.strip().split(',')
                        if len(partes) == 4:
                            id_cliente, id_produto, quantidade_str, total_str = partes
                            
                            cliente = self.clientes.get(id_cliente)
                            produto = self.produtos.get(id_produto)
                            
                            if cliente and produto:
                                venda = Venda(cliente, produto, int(quantidade_str), float(total_str))
                                self.fila_vendas.enfileirar(venda)
                            else:
                                erro(f"Cliente ou produto com ID '{id_cliente}' ou '{id_produto}' não encontrado para a venda: {linha.strip()}. Venda ignorada.")
                acerto(f"Dados de vendas carregados de '{vendas_path}'.")
            except (IOError, ValueError) as e:
                erro(f"Erro ao carregar vendas de '{vendas_path}': {e}. Verifique o formato do arquivo.")
        else:
            print(" ↪︎ Nenhum arquivo de vendas encontrado. Iniciando com vendas vazias.")

    def __str__(self):
        return f"Clientes: {self.clientes} Produtos: {self.produtos} Fila de vendas: {self.fila_vendas} Pilha de operações: {self.pilha_operacoes}"