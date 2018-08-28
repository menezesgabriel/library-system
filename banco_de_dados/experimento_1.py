from tkinter import *
from banco_tipo_classe import Dados
tk=Tk()
janela=tk

class Livro:
    def __init__(self,nome_do_livro,nome_do_autor,ano,edicao):
        self.nome_do_livro=nome_do_livro
        self.nome_do_autor=nome_do_autor
        self.ano=ano
        self.edicao=edicao


    def novo_livro(self):
        Dados.criar_tabela_livro()


    def salvar(self):
        self.lb4 = "livro salvo"
        self.nome_do_livro=Entry(janela,width=28)

        self.nome_do_autor=self.tela()# ed_autor.get()
        self.ano=ed_ano_do_livro.get()
        self.edicao=ed_edicao.get()

        data_de_indexacao=datetime.datetime.fromtimestamp(time.time()).strftime('%D-%m-%y %H:%M:%S')
        codigo_livro=random.randrange(0,100)
        c.execute("INSERT  INTO livros(data_de_indexacao,codigo_livro,nome_do_livro,nome_do_autor,ano,edicao) VALUES (?,?,?,?,?,?)",( data_de_indexacao,codigo_livro,nome_do_livro,nome_do_autor,ano,edicao))
        connection.commit()
        c.close()
        connection.close()


    def tela(self):
        lb4 = Label(janela, text="")
        lb4.place(x=120, y=250)

#        ed_autor.place(x=100, y=75)#####

        ed_titulo=Entry(janela,width=28)
        ed_titulo.place(x=100,y=35)

        ed_autor=Entry(janela,width=28)
        ed_autor.place(x=100,y=75)

        ed_ano_do_livro=Entry(janela,width=28)
        ed_ano_do_livro.place(x=100,y=115)

        ed_edicao=Entry(janela,width=28)
        ed_edicao.place(x=100,y=155)


        lb=Label(janela, text="nome do título:")
        lb.place(x=10,y=30)

        lb2=Label(janela, text="nome do autor :")
        lb2.place(x=10,y=70)

        lb3=Label(janela, text="ano do livro: ")
        lb3.place(x=10,y=110)

        lb3=Label(janela, text="edição do livro:")
        lb3.place(x=10,y=150)

        lb4=Label(janela, text="")
        lb4.place(x=120,y=250)

        bt=Button
        botao_confirmar=bt(janela,width=18, text="Salvar",command=self.salvar)
        botao_confirmar.place(x=90,y=200)


        tk.geometry("300x300+500+200")
        tk.mainloop()




