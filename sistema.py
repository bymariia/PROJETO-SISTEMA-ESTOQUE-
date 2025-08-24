import os
from defs import erro, acerto
from classes import Sistema
sistema = Sistema()
os.system('cls')

#Arrumar opções 3 e 8!!! Fazer coisas que valem pontos extras(arquivo .txt + pesquisa por nome/id)

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
        sistema.cadastrar_cliente(nome_cliente, id_cliente)

    elif escolha_menu == "2": 
        os.system('cls')
        print('''⋰――――――――――――――――⋯ ESCOLHA 2 ⋯――――――――――――――――⋱
 ↪︎ Clientes cadastrados: ''')
        sistema.listar_cliente()
        print('''⋱――――――――――――――――――――――⋯――――――――――――――――――――――⋰''')

    elif escolha_menu == "3": # TEM Q FAZER !!!
        os.system('cls')
        print('''⋰――――――――――――――――⋯ ESCOLHA 3 ⋯――――――――――――――――⋱
 ↪︎ Clientes cadastrados e totais gastos: ''')
        
        print('''⋱――――――――――――――――――――――⋯――――――――――――――――――――――⋰''')
        #COLOCAR O TOTAL DE GASTOS!!!
        
    elif escolha_menu == "4": 
        os.system('cls')
        print('''⋰――――――――――――――――⋯ ESCOLHA 4 ⋯――――――――――――――――⋱''')
        nome = input(" ↪︎ Digite o nome do produto: ")
        try:
            quantidade = int(input(" ↪︎ Digite a quantidade: "))
        except ValueError:
            erro("Quantidade inválida.")
            continue
        try:
            preco = float(input(" ↪︎ Digite o valor unitário: ")) 
        except ValueError:
            erro("Preço inválido.")
            continue
        id_produto = input(" ↪︎ Digite o ID do produto: ")
        sistema.cadastrar_produto(nome, preco, quantidade, id_produto)
        acerto(f"Produto '{nome}' cadastrado com sucesso!")
        
    elif escolha_menu == "5":
        os.system('cls')
        print('''⋰――――――――――――――――⋯ ESCOLHA 5 ⋯――――――――――――――――⋱
 ↪︎ Produtos cadastrados: ''')
        sistema.listar_produtos()
        print('''⋱――――――――――――――――――――――⋯――――――――――――――――――――――⋰''')
        
    elif escolha_menu == "6": 
        os.system('cls')
        print('''⋰――――――――――――――――⋯ ESCOLHA 6 ⋯――――――――――――――――⋱''')
        if not sistema.listar_produtos:
            erro("Nenhum produto cadastrado.")
        else:
            total = sistema.total_estoque()
            print(f" ↪︎ Valor total do estoque: R${total:.2f}")
            print('''⋱――――――――――――――――――――――⋯――――――――――――――――――――――⋰''')

    elif escolha_menu == "7":
        os.system('cls')
        print('''⋰――――――――――――――――⋯ ESCOLHA 7 ⋯――――――――――――――――⋱''')
        sistema.realizar_venda()
        
    elif escolha_menu == "8":   # TEM QUE ARRUMAR TA APARECENDO ESTRANHO !!!!
        os.system('cls')
        print('''⋰――――――――――――――――⋯ ESCOLHA 8 ⋯――――――――――――――――⋱
 ↪︎ Vendas realizadas: ''')
        sistema.ver_fila_vendas()
        print('''⋱――――――――――――――――――――――⋯――――――――――――――――――――――⋰''')
        
        
    elif escolha_menu == "9":
        os.system('cls')
        print('''⋰――――――――――――――――⋯ ESCOLHA 9 ⋯――――――――――――――――⋱
 ↪︎ Valor total de vendas realizadas: ''')
        sistema.exibir_valor_total_vendas()
        print('''⋱――――――――――――――――――――――⋯――――――――――――――――――――――⋰''')


    elif escolha_menu == "10": 
        os.system('cls')
        print('''⋰―――――――――――――――⋯ ESCOLHA 10 ⋯――――――――――――――――⋱''')
        sistema.desfazer_ultima_operacao()
        print('''⋱――――――――――――――――――――――⋯――――――――――――――――――――――⋰''')

    elif escolha_menu == "11": 
        os.system('cls')
        print('''⋰―――――――――――――――⋯ ESCOLHA 11 ⋯――――――――――――――――⋱
 ↪︎ Saindo...
⋱――――――――――――――――――――――⋯――――――――――――――――――――――⋰''')
        break

    else: 
        os.system('cls')
        erro("Escolha inválida. Tente novamente.")