import datetime
import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="ProjetoEletroMoveis",
    user="postgres",
    password="pipoca69")

cursor = connection.cursor()


def menuInicial():
    print("** MENU **")
    print("1- Ver Moveis disponiveis")
    print("2- Acessar Sistema")


def menuFuncionario():
    print("** MENU **")
    print("1- Cadastrar funcionario")
    print("2- Cadastrar produto")
    print("3- Verificar entregas pendentes")


def verMoveis():
    cursor.execute("SELECT cod_produto, nome, valor FROM tabelas.produto")
    result = cursor.fetchall()
    print(result)


def cadastrarFuncionario(cpf, nome, rua, num, cep, cidade, uf, senha):
    comando = """insert into tabelas.funcionario (cpf,nome,rua,num,cep,cidade,uf,senha) values (%s, %s, %s, %s, %s, %s, 
    %s, %s)"""
    cursor.execute(comando, (cpf, nome, rua, num, cep, cidade, uf, senha))
    connection.commit()
    print("Funcionario cadastrado com sucesso")


def cadastrarCliente(cpf, nome, rua, num, cep):
    comando = """insert into tabelas.cliente (cpf,nome,rua,num,cep) values (%s, %s, %s, %s, %s,)"""
    cursor.execute(comando, (cpf, nome, rua, num, cep))
    connection.commit()
    print("Cliente cadastrado com sucesso")


def cadastrarProduto(cod_produto, nome, valor, data_recebimento, quantidade):
    comando = """insert into tabelas.produto (cod_produto, nome, valor, data_recebimento, quantidade) values (%s, %s, %s,
     %s, %s)"""
    cursor.execute(comando, (cod_produto, nome, valor, data_recebimento, quantidade))
    connection.commit()
    print("Produto cadastrado com sucesso")


def fazerCompra(compra):
    if compra == 1:
        cadastroCliente()
    elif compra == 2:
        print("Tenha um otimo dia e obrigado por utilizar nossa loja!")


def comprarProduto():
    cpf_cliente = int(input("Digite o cpf do cliente: "))
    id_produto = int(input("Digite o id do produto: "))
    status = 'pendente'
    comando = """ INSERT INTO tabelas.vendas (cpf_cliente,id_produto,status) VALUES (%s, %s,%s)"""
    cursor.execute(comando, (cpf_cliente, id_produto, status,))
    connection.commit()
    print("Compra finalizada")


def inserirCliente():
    cpf = int(input("Digite seu CPF sem pontos ou traço :"))
    nome = input("Insira seu nome :")
    rua = input("Digite sua rua :")
    num = int(input("Digite seu numero: "))
    cep = int(input("Digite o cep de sua cidade: "))
    cidade = input("Digite sua cidade:")
    uf = input("Digite seu estado: ")
    '''cursor.execute("INSERT INTO tabelas.cliente (cpf, nome, rua, num, cep, cidade, uf) "
                   "VALUES (%d, '%s', '%s', %d, %d,'%s','%s')" % (cpf, nome, rua, num, cep, cidade, uf))'''

    comando = """insert into tabelas.cliente (cpf,nome,rua,num,cep,cidade,uf) values (%s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(comando, (cpf, nome, rua, num, cep, cidade, uf,))
    connection.commit()
    print("Cliente cadastrado com sucesso")


def cadastroCliente(cadastro):
    if cadastro == 1:
        comprarProduto()
    elif cadastro == 2:
        inserirCliente()
        comprarProduto()


def entregaPendente():
    cursor.execute("select* from tabelas.vendas")
    print(cursor.fetchall())


menuInicial()
op = int(input("Qual opção você deseja escolher?"))

if op == 1:
    verMoveis()
    compra = int(input("Deseja efetuar sua compra? (1)Sim (2)Não:"))
    if compra == 1:
        cadastro = int(input("Já é cadastrado em nossa loja? (1)Sim (2) Não:"))
        cadastroCliente(cadastro)
    elif compra == 2:
        print("Volte sempre a EletreMoveis agradece a sua preferencia")

else:
    menuFuncionario()
    opcao = int(input("Qual opção voce deseja escolher"))
    if opcao == 1:
        cpf = int(input("Insira seu CPF sem pontos ou traço:"))
        nome = input("Digite o nome:")
        rua = input("Digite a rua:")
        num = int(input("Digite o telefone:"))
        cep = int(input("Digite o CEP:"))
        cidade = input("Digite a cidade:")
        uf = input("Digite o estado:")
        senha = int(input("Digite a senha (Em numeros):"))
        cadastrarFuncionario(cpf, nome, rua, num, cep, cidade, uf, senha)
    if opcao == 2:
        cod_produto = int(input("Digite o codigo do produto"))
        nome = input("Digite o nome do produto")
        valor = int(input("Digite o valor do produto"))
        ano = int(input("Digite o ano"))
        mes = int(input("Digite o mes"))
        dia = int(input("Digite o dia"))
        data_recebimento = datetime.date(ano, mes, dia)
        quantidade = int(input("Digite a quantidade"))
        cadastrarProduto(cod_produto, nome, valor, data_recebimento, quantidade)
    if opcao == 3:
        entregaPendente()
        print("EletroMoveis sistema de compras pendentes")

