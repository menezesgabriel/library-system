##VAI MANO, ESSA PORRA TA TODA FUNCIONANDO
import sqlite3
import datetime
import time
import random

connection = sqlite3.connect('biblioteca.db')
c = connection.cursor()

class Dados:
    def __init__(self,cod,data):
        self.cod=random.randrange(0,100)
        self.data=datetime.datetime.fromtimestamp(time.time()).strftime('%D-%m-%y %H:%M:%S')

    def criar_tabela_livro(self):
        c.execute('CREATE TABLE IF NOT EXISTS  livros (codigo_livro integer, nome_do_livro TEXT, nome_do_autor text, ano TEXT, edicao real, data_de_indexacao TEXT)')
        data_de_indexacao=self.data
        codigo_livro= self.cod

        print(codigo_livro)
        print(data_de_indexacao)
        c.execute("INSERT  INTO livros(data_de_indexacao,codigo_livro) VALUES (?,?)",
            (data_de_indexacao, codigo_livro))
        connection.commit()
        c.close()
        connection.close()

    def criar_table_funcionário(self):

        c.execute('CREATE TABLE IF NOT EXISTS  funcionario (nome TEXT, cpf integer, rg integer, telefone integer, rua TEXT, numero_da_casa integer, bairro TEXT, cidade TEXT, cep integer, id integer, data_de_indexacao TEXT)')

        data_de_indexacao = self.data
        id = self.cod

        print(id)
        print(data_de_indexacao)
        c.execute("INSERT  INTO funcionario(data_de_indexacao,id) VALUES (?,?)",(data_de_indexacao, id))
        connection.commit()
        c.close()
        connection.close()

    def criar_tabela_cliente(self):
        c.execute('CREATE TABLE IF NOT EXISTS  cliente (nome TEXT, cpf integer, rg integer, telefone integer, rua TEXT, numero_da_casa integer, bairro TEXT, cidade TEXT, cep integer, id integer, data TEXT)')
        data = self.data
        id = self.cod

        print(id)
        print(data)
        c.execute("INSERT  INTO cliente(data,id) VALUES (?,?)", (data, id))
        connection.commit()
        c.close()
        connection.close()


