
from Banco import Banco


class Usuarios(object):

    def __init__(self, codigo_livro=0, nome_do_livro="", nome_do_autor="", ano="", edicao="", data_de_indexacao=""):
        self.codigo_livro=codigo_livro
        self.nome_do_livro=nome_do_livro
        self.nome_do_autor=nome_do_autor
        self.ano=ano
        self.edicao=edicao
        self.data_de_indexacao=data_de_indexacao

    def insertUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()
            c.execute("insert into livros (codigo_livro, nome_do_livro, nome_do_autor, ano, edicao,data_de_indexacao) values ('" + self.codigo_livro + "', '" + self.nome_do_livro + "', '" + self.nome_do_autor + "', '" + self.ano + "', '" + self.edicao + "','" + self.data_de_indexacao + "' )")

            banco.conexao.commit()
            c.close()

            return "Livro cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do Livro"


    def deleteUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("delete from livros where codigo_do_livro = " + self.codigo_livro + " ")

            banco.conexao.commit()
            c.close()

            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"


    def selectUser(self, codigo_livro):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("select * from livros where cod_livro = " + codigo_livro + "  ")

            for linha in c:
                self.codigo_livro = linha[0]
                self.nome_do_livro = linha[1]
                self.nome_do_autor = linha[2]
                self.ano = linha[3]
                self.edicao = linha[4]
                self.edicao = linha[5]
                self.data_de_indexacao= linha[6]

            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"