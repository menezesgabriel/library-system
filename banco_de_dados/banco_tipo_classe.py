##VAI MANO, ESSA PORRA TA TODA FUNCIONANDO
import sqlite3
import datetime
import time
import random
from tkinter import *

connection = sqlite3.connect('biblioteca.db')
c = connection.cursor()

class Dados:
    def __init__(self,cod,data):
        self.cod=random.randrange(0,100)
        self.data=datetime.datetime.fromtimestamp(time.time()).strftime('%D-%m-%y %H:%M:%S')

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

    def criar_tabela_livro(self):
        self.lb4 = "livro salvo"
        c.execute(
            'CREATE TABLE IF NOT EXISTS  livros (codigo_livro integer, nome_do_livro TEXT, nome_do_autor text, ano TEXT, edicao real, data_de_indexacao TEXT)')
        data_de_indexacao = datetime.datetime.fromtimestamp(time.time()).strftime('%D-%m-%y %H:%M:%S')
        codigo_livro = random.randrange(0, 100)
        nome_do_livro = ed_titulo.get()
        nome_do_autor = ed_autor.get()

        print(codigo_livro)
        print(data_de_indexacao)
        c.execute("INSERT  INTO livros(data_de_indexacao,codigo_livro) VALUES (?,?)",
                  (data_de_indexacao, codigo_livro))
        connection.commit()
        c.close()
        connection.close()



tk = Tk()
janela = tk

ed_titulo = Entry(janela, width=28)
ed_titulo.place(x=100, y=35)

ed_autor = Entry(janela, width=28)
ed_autor.place(x=100, y=75)

ed_ano_do_livro = Entry(janela, width=28)
ed_ano_do_livro.place(x=100, y=115)

ed_edicao = Entry(janela, width=28)
ed_edicao.place(x=100, y=155)

lb = Label(janela, text="nome do título:")
lb.place(x=10, y=30)

lb2 = Label(janela, text="nome do autor :")
lb2.place(x=10, y=70)

lb3 = Label(janela, text="ano do livro: ")
lb3.place(x=10, y=110)

lb3 = Label(janela, text="edição do livro:")
lb3.place(x=10, y=150)

lb4 = Label(janela, text="")
lb4.place(x=120, y=250)

bt = Button
botao_confirmar = bt(janela, width=18, text="Salvar",command=)
botao_confirmar.place(x=90, y=200)

tk.geometry("300x300+500+200")
tk.mainloop()





