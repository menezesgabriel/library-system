from pessoa import Pessoa
from random import randint
class Cliente:
    def __init__(self,cod_cliente):
        self.cod_cliente = randint(0, 1000)

    def novo_cliente(self):
        arquivo = open('cliente.txt', 'r')
        conteudo = arquivo.readlines()
        Pessoa.id = conteudo.append(str(self.cod_cliente) + ' ')
        Pessoa.nome= conteudo.append(input('nome do funcionário:')+ ' ')
        Pessoa.cpf = conteudo.append(input('numero do cpf:')+ ' ')
        Pessoa.rg = conteudo.append(input('número do RG:')+' ')
        Pessoa.telefone = conteudo.append(input('número do seu telefone:')+' ')
        Pessoa.rua = conteudo.append(input('nome da rua:')+' ')
        Pessoa.numero_casa = conteudo.append(input('numero da casa:')+' ')
        Pessoa.bairro = conteudo.append(input('nome do bairro:')+' ')
        Pessoa.cidade = conteudo.append(input('cidade:')+' ')
        Pessoa.cep = conteudo.append(input('numero do cep:')+' ')
        Pessoa.cep = conteudo.append('\n')
        arquivo = open('cliente.txt', 'w')
        arquivo.writelines(conteudo)
        arquivo.close()
        print('cliente criado!\n numero de cadastro:', self.cod_cliente)

    def mostrar_clientes(self):
        arquivo = open('cliente.txt', 'r')
        print(arquivo.read())
        arquivo.close()
    def apagar_clientes(self):
        arquivo = open('clientes.txt', 'w')
        arquivo.close()