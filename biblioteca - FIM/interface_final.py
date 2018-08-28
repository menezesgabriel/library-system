from tkinter import *
class Application:
    def __init__(self, master=None):
        # telinha com o x de fechar
        self.fontePadrao = ("Times", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        #frame para escrita do usuario 1
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20  # largura do bloco de tela
        self.segundoContainer.pack()

        #frame para escrita do usuario 2

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 150
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 150  # altura do bloco
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Pesquisar Livro")
        self.titulo["font"] = ("Times", "14", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer, text="Nome do livro", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30  # espaço para escreber o nome do livro
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)




root = Tk()
Application(root)
root.mainloop()