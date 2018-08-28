class Pesquisar:
    def __init__(self,resp):
        self.resp=resp

    def pesqusiar_livro(self):
        MsgOk = 'Encontrado'
        MsgNok = 'Não encontrado'

        self.resp = int(input('Pesquisar livro:\n1-Codigo;\n2-nome do livro;\ndigite a opção que deseja usar:'))

        if self.resp == 1:
            num = (input("digite o código do livro:"))
        elif self.resp == 2:
            num = (input("digite o nome do livro:"))

        def check():
            datafile = open('livros.txt')
            for line in datafile:
                if num in line:
                    found = True
                    break
                else:
                    found = False
            return found

        if check():
            print(MsgOk)
        else:
            print(MsgNok)

    def pesquisar_cliente(self):
        MsgOk = 'Encontrado'
        MsgNok = 'Não encontrado'

        self.resp = int(input('Pesquisar cliente:\n1-Codigo;\n2-nome ;\ndigite a opção que deseja usar:'))

        if self.resp == 1:
            num = (input("digite o código do cliente:"))
        elif self.resp == 2:
            num = (input("digite o nome do cliente:"))

        def check():
            datafile = open('cliente.txt')
            for line in datafile:
                if num in line:
                    found = True
                    break
                else:
                    found = False
            return found

        if check():
            print(MsgOk)
        else:
            print(MsgNok)

    def pesquisar_funcionario(self):
        MsgOk = 'Encontrado'
        MsgNok = 'Não encontrado'

        self.resp = int(input('Pesquisar funcionario:\n1-Codigo;\n2-nome do funcionario;\ndigite a opção que deseja usar:'))

        if self.resp == 1:
            num = (input("digite o código do funcionario:"))
        elif self.resp == 2:
            num = (input("digite o nome do fucionario:"))

        def check():
            datafile = open('funcionario.txt')
            for line in datafile:
                if num in line:
                    found = True
                    break
                else:
                    found = False
            return found

        if check():
            print(MsgOk)
        else:
            print(MsgNok)
