from random import randint
    class Livros:
        def __init__(self, titulo, autor, ano, edicao, qt_de_livros=0):
            self.titulo = titulo
            self.autor = autor
            self.ano = ano
            self.edicao = edicao
            self.qt_de_livros = qt_de_livros
            self.id_livro = randint(0, 1000)

    def novo_livro(self):
        arquivo = open('livros.txt', 'r')
        conteudo = arquivo.readlines()
        self.edicao = conteudo.append (str(self.id_livro)+' ')
        self.titulo = conteudo.append(input('nome do título:' )+ ' ')
        self.autor = conteudo.append(input('nome do autor : ')+ ' ')
        self.ano = conteudo.append(input('ano do livro: ')+ ' ')
        self.edicao = conteudo.append(input('edição do livro: ')+ ' ')
        self.edicao = conteudo.append('\n')
        print('livro criado!\ncodigo do livro:', self.id_livro)
        arquivo = open('livros.txt', 'w')
        arquivo.writelines(conteudo)
    def mostrar_livros_salvos(self):
        arquivo = open('livros.txt', 'r')
       # print('livro criado!\ncodigo do livro:', self.id_livro)
       #print('quantidade de livros cadastrados: ', self.qt_de_livros)
        print(arquivo.read())
        arquivo.close()
    def qtd_mais_um (self):
       self.qt_de_livros=+1
    def qtd_menos_um (self):
        self.qt_de_livros=-1
    def apagar_livro(self):
        arquivo = open('livros.txt', 'w')
        arquivo.close()
    def mostra_todos_por_linha(self):
        arquivo = open('livros.txt', 'r')
        primeira_linha = arquivo.readline()
        segunda_linha = arquivo.readline()
        terceira_linha = arquivo.readline()
        quarta_linha = arquivo.readline()
        quinta_linha = arquivo.readline()
        sexta_linha = arquivo.readline()
        setima_linha = arquivo.readline()
        oitava_linha = arquivo.readline()
        nona_linha = arquivo.readline()
        print(primeira_linha, segunda_linha, terceira_linha, quarta_linha, quinta_linha, sexta_linha, setima_linha,oitava_linha, nona_linha)
        arquivo.close()

