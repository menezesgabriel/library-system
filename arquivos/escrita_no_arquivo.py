class Livros:
    def __init__(self,titulo,autor,ano,edicao,qt_de_livros=0):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.edicao = edicao
        self.qt_de_livros = qt_de_livros

    def novo_livro(self):
        arquivo = open('teste_arquivo_livros.txt', 'r')
        conteudo = arquivo.readlines()
        self.titulo = conteudo.append(input('nome do título: '))
        self.edicao = conteudo.append(' ')
        self.autor = conteudo.append(input('nome do autor : '))
        self.ano = conteudo.append(input('ano do livro: '))
        self.edicao = conteudo.append(input('edição do livro: '))
        self.edicao = conteudo.append('\n')
        arquivo = open('teste_arquivo_livros.txt', 'w')
        arquivo.writelines(conteudo)

    def mostrar_informações_guardadas(self):
        arquivo =open('teste_arquivo_livros.txt', 'r')
        print(arquivo.read())
        arquivo.close()

    def apagar_livro(self):
        arquivo = open('teste_arquivo_livros.txt', 'w')
        arquivo.close()

    def mostrar_todos_os_livros(self):
        #mostrar todos os livros guardados no arquivo
        arquivo = open('teste_arquivo_livros.txt', 'r')
        primeira_linha=arquivo.readline()
        segunda_linha=arquivo.readline()
        terceira_linha = arquivo.readline()
        quarta_linha = arquivo.readline()
        quinta_linha = arquivo.readline()
        sexta_linha = arquivo.readline()
        setima_linha = arquivo.readline()
        oitava_linha = arquivo.readline()
        nona_linha = arquivo.readline()
        print(primeira_linha,segunda_linha,terceira_linha,quarta_linha,quinta_linha,sexta_linha,setima_linha,oitava_linha,nona_linha)
        arquivo.close()

    def mostrar_como_vetor(self):
        arquivo = open('teste_arquivo_livros.txt', 'r')
        x = arquivo.readlines()
        print(x)
        arquivo.close()