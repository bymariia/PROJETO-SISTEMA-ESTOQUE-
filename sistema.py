import os
from defs import erro, acerto
from recursos import Pilha, Fila

#LISTA de produtos do estoque/FILA para registrar vendas em ordem de chegada/PILHA para desfazer a última operação.
lista_produtos = []
fila_vendas = Fila()
pilha_operacoes = Pilha()

while True: #Esse é o menu principal do estoque:
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
    escolha_menu = input(" ✎  Digite sua escolha: ") #Aqui é dada a opção para o usuário fazer sua escolha.
    if escolha_menu == "1": #Caso faça escolha 1:
        os.system('cls')
        nome_cliente = input('''⋰――――――――――――――――⋯ ESCOLHA 1 ⋯――――――――――――――――⋱
 ↪︎ Digite o nome do cliente: ''')
        acerto(f"Cliente '{nome_cliente}' cadastrado com sucesso.")

    elif escolha_menu == "2": #Caso faça escolha 2:
        os.system('cls')
        print('''⋰――――――――――――――――⋯ ESCOLHA 2 ⋯――――――――――――――――⋱
 ↪︎ Clientes cadastrados: ''')
        
    elif escolha_menu == "3": #Caso faça escolha 3:
        os.system('cls')
        print('''⋰――――――――――――――――⋯ ESCOLHA 3 ⋯――――――――――――――――⋱
 ↪︎ Clientes cadastrados e totais gastos: ''')
        
    elif escolha_menu == "4": #Caso faça escolha 4:
        os.system('cls')
        print('''⋰――――――――――――――――⋯ ESCOLHA 4 ⋯――――――――――――――――⋱
 ↪︎ Digite o nome do produto: 
 ↪︎ Digite a quantidade:
 ↪︎ Digite o valor unitário: ''')
        
    elif escolha_menu == "5": #Caso faça escolha 5:
        os.system('cls')
        print('''⋰――――――――――――――――⋯ ESCOLHA 5 ⋯――――――――――――――――⋱
 ↪︎ Produtos cadastrados:
⋱――――――――――――――――――――――⋯――――――――――――――――――――――⋰''')
        
    elif escolha_menu == "6": #Caso faça escolha 6:
        os.system('cls')
        print('''⋰――――――――――――――――⋯ ESCOLHA 6 ⋯――――――――――――――――⋱
 ↪︎ Produtos cadastrados:
⋱――――――――――――――――――――――⋯――――――――――――――――――――――⋰''')
        
    elif escolha_menu == "7": #Caso faça escolha 7:
        os.system('cls')
        print('''⋰――――――――――――――――⋯ ESCOLHA 7 ⋯――――――――――――――――⋱
 ↪︎ Valor total do estoque:
⋱――――――――――――――――――――――⋯――――――――――――――――――――――⋰''')
        
    elif escolha_menu == "8": #Caso faça escolha 8:
        os.system('cls')
        print('''⋰――――――――――――――――⋯ ESCOLHA 8 ⋯――――――――――――――――⋱
 ↪︎ Vendas realizadas:
⋱――――――――――――――――――――――⋯――――――――――――――――――――――⋰''')
        
    elif escolha_menu == "9": #Caso faça escolha 9:
        os.system('cls')
        print('''⋰――――――――――――――――⋯ ESCOLHA 9 ⋯――――――――――――――――⋱
 ↪︎ Valor total de vendas realizadas:
⋱――――――――――――――――――――――⋯――――――――――――――――――――――⋰''')
        
    elif escolha_menu == "10": #Caso faça escolha 10:
        os.system('cls')
        ...

    elif escolha_menu == "11": #Caso faça escolha 11:
        os.system('cls')
        print('''⋰―――――――――――――――⋯ ESCOLHA 11 ⋯――――――――――――――――⋱
 ↪︎ Saindo...
⋱――――――――――――――――――――――⋯――――――――――――――――――――――⋰''')
        break

    else: #Caso sua escolha seja inválida:
        os.system('cls')
        erro("Escolha inválida. Tente novamente.")