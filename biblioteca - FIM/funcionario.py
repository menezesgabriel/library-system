from random import randint
from pessoa import Pessoa
class Funcionario:
    def __init__(self,cod_funcionario):
        self.cod_funcionario = randint(0, 1000)

    def novo_funcionario(self):
            arquivo = open('funcionario.txt', 'r')
            conteudo = arquivo.readlines()
            Pessoa.id= conteudo.append(str(self.cod_funcionario)+ ' ')
            Pessoa.nome = conteudo.append(input('nome do funcionário: ')+ ' ')
            Pessoa.cpf = conteudo.append(input('CPF: : ')+ ' ')
            Pessoa.rg = conteudo.append(input('RG: ')+ ' ')
            Pessoa.telefone = conteudo.append(input('telefone: ')+ ' ')
            Pessoa.rua = conteudo.append(input('rua: ') + ' ')
            Pessoa.numero_casa = conteudo.append(input('número da casa: ') + ' ')
            Pessoa.bairro = conteudo.append(input('bairro: ') + ' ')
            Pessoa.cidade = conteudo.append(input('cidade: ') + ' ')
            Pessoa.cep = conteudo.append(input('cep: ') + ' ')
            Pessoa.cep = conteudo.append('\n')
            arquivo = open('funcionario.txt', 'w')
            arquivo.writelines(conteudo)
            arquivo.close()
            print('cliente criado!\nnumero de cadastro:', self.cod_funcionario)

    def mostrar_funcionarios(self):
        arquivo = open('funcionario.txt', 'r')
        print(arquivo.read())
        arquivo.close()
    def apagar_funcionarios(self):
            arquivo = open('funcionario.txt', 'w')
            arquivo.close()
