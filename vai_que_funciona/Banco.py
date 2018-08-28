
import sqlite3
class Banco():

    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute('CREATE TABLE IF NOT EXISTS  livros (codigo_livro integer, nome_do_livro TEXT, nome_do_autor text, ano TEXT, edicao real, data_de_indexacao TEXT)')
        self.conexao.commit()
        c.close()


