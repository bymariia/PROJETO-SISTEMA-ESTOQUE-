import os
from defs import erro, acerto
from recursos import Pilha, Fila
from classes import Sistema, Cliente, Produto
Sistema = Sistema()

while True: 
    print('''
⋰―――――――――――――――⋯ MENU ESTOQUE ⋯――――――――――――――⋱
 1- Cadastrar clientes.
 2- Listar clientes.
 3- Exibir clientes e valores totais gastos.
 4- Cadastrar produtos.
 5- Listar produtos do estoque.
 6- Exibir valor total do estoque.
 7- Realizar venda.
 8- Visualizar fila de vendas.
 9- Exibir valor total de vendas realizadas.
 10- Desfazer última operação.
 11- Sair.
⋱――――――――――――――――――――――⋯――――――――――――――――――――――⋰
''')
    escolha_menu = input(" ✎  Digite sua escolha: ")

    if escolha_menu == "1": 
        os.system('cls')
        nome_cliente = input('''⋰――――――――――――――――⋯ ESCOLHA 1 ⋯――――――――――――――――⋱
 ↪︎ Digite o nome do cliente: ''')
        id_cliente = input(" ↪︎ Digite o ID do cliente: ")
        Sistema.cadastrar_cliente(nome_cliente, id_cliente)
        acerto(f"Cliente '{nome_cliente}' cadastrado com sucesso!")

    elif escolha_menu == "2": 
        os.system('cls')
        print('''⋰――――――――――――――――⋯ ESCOLHA 2 ⋯――――――――――――――――⋱
 ↪︎ Clientes cadastrados: ''')
        Sistema.listar_cliente()

    elif escolha_menu == "3": # TEM Q FAZER !!!
        os.system('cls')
        print('''⋰――――――――――――――――⋯ ESCOLHA 3 ⋯――――――――――――――――⋱
 ↪︎ Clientes cadastrados e totais gastos: ''')
        #COLOCAR O TOTAL DE GASTOS!!!

        
    elif escolha_menu == "4": 
        os.system('cls')
        print('''⋰――――――――――――――――⋯ ESCOLHA 4 ⋯――――――――――――――――⋱''')
        nome = input(" ↪︎ Digite o nome do produto: ")
        quantidade = int(input("↪︎ Digite a quantidade: "))
        preco = float(input("↪︎ Digite o valor unitário: ")) 
        id_produto = input("↪︎ Digite o ID do produto: ")
        Sistema.cadastrar_produto(nome, preco, quantidade, id_produto)
        acerto(f"Produto '{nome}' cadastrado com sucesso!")
        
    elif escolha_menu == "5":
        os.system('cls')
        print('''⋰――――――――――――――――⋯ ESCOLHA 5 ⋯――――――――――――――――⋱
 ↪︎ Produtos cadastrados:
⋱――――――――――――――――――――――⋯――――――――――――――――――――――⋰''')
        Sistema.listar_produtos()
        
    elif escolha_menu == "6": # TEM Q ARRUMAR!!!
        os.system('cls')
        print('''⋰――――――――――――――――⋯ ESCOLHA 6 ⋯――――――――――――――――⋱
 ↪︎ Produtos cadastrados:
⋱――――――――――――――――――――――⋯――――――――――――――――――――――⋰''')
        if not Sistema.listar_produtos:
            erro("Nenhum produto cadastrado.")
        else:
            total = sum(p.preco * p.quantidade for p in Produto)
            print(f"↪︎ Valor total do estoque: R${total:.2f}")

    elif escolha_menu == "7":
        os.system('cls')
        print('''⋰――――――――――――――――⋯ ESCOLHA 7 ⋯――――――――――――――――⋱
 ↪︎ Valor total do estoque:
⋱――――――――――――――――――――――⋯――――――――――――――――――――――⋰''')
        Sistema.realizar_venda()
        
    elif escolha_menu == "8":   # TEM QUE ARRUMAR TA APARECENDO ESTRANHO !!!!
        os.system('cls')
        print('''⋰――――――――――――――――⋯ ESCOLHA 8 ⋯――――――――――――――――⋱
 ↪︎ Vendas realizadas:
⋱――――――――――――――――――――――⋯――――――――――――――――――――――⋰''')
        Sistema.ver_fila_vendas()
        
    elif escolha_menu == "9":
        os.system('cls')
        print('''⋰――――――――――――――――⋯ ESCOLHA 9 ⋯――――――――――――――――⋱
 ↪︎ Valor total de vendas realizadas:
⋱――――――――――――――――――――――⋯――――――――――――――――――――――⋰''')
        Sistema.exibir_valor_total_vendas()

    elif escolha_menu == "10": 
        os.system('cls')
        Sistema.desfazer_ultima_operacao()

    elif escolha_menu == "11": 
        os.system('cls')
        print('''⋰―――――――――――――――⋯ ESCOLHA 11 ⋯――――――――――――――――⋱
 ↪︎ Saindo...
⋱――――――――――――――――――――――⋯――――――――――――――――――――――⋰''')
        break

    else: 
        os.system('cls')
        erro("Escolha inválida. Tente novamente.")