import os
from acervo import Livros
from cliente import Cliente
from funcionario import Funcionario
from pesquisar import Pesquisar

new_cliente= Cliente(Cliente.novo_cliente)
new_funcionario= Funcionario(Funcionario.novo_funcionario)
new_book=Livros(Livros.novo_livro,Livros.novo_livro,Livros.novo_livro,Livros.novo_livro,Livros.novo_livro)
new_pesquisa=Pesquisar(Pesquisar.pesqusiar_livro)

resp=int (input("1-livro:\n2-funcionários:\n3-cliente:\n4-pesquisar:\nqual serviço você deseja usar?\n--:"))
#while(resp == 1 , 2 , 3):
if resp==1:
      os.system('cls')
      resp1=int (input("1-cadastrar novo livro\n2-mostra livros salvos\n3-apagar livros\n--:"))
      if resp1==1:
          new_book.novo_livro()
      elif resp1==2:
          new_book.mostra_todos_por_linha()
      elif resp1==3:
          new_book.apagar_livro()
      else:
          print('comando não encontrado.')
elif resp==2:
    os.system('cls')
    resp2 = int(input("1-cadastrar funcionário\n2-mostrar funcionários cadastrados\n3-apagar funcionário livros\n--:"))
    if resp2 == 1:
        new_funcionario.novo_funcionario()
    elif resp2 == 2:
        new_funcionario.mostrar_funcionarios()
    elif resp2 == 3:
        new_funcionario.apagar_funcionarios()
    else:
        print('comando não encontrado.')
elif resp==3:
    os.system('cls')
    resp3 = int(input("1-cadastrar clientes\n2-mostrar clientes cadastrados\n3-apagar cliente livros\n--:"))
    if resp3 == 1:
        new_cliente.novo_cliente()
    elif resp3 == 2:
        new_cliente.mostrar_clientes()
    elif resp3 == 3:
        new_cliente.apagar_clientes()
    else:
        print('comando não encontrado.')
elif resp==4:
    os.system('cls')
    resp4 = int(input("1-pesquisar livro\n2-pesquisar cliente:\n3-pesquisar funcionário\n--:"))
    if resp4 == 1:
        new_pesquisa.pesqusiar_livro()
    elif resp4 == 2:
        new_pesquisa.pesquisar_cliente()
    elif resp4 == 3:
        new_pesquisa.pesquisar_funcionario()
    else:
        print('comando não encontrado.')


else:
    print("comando não encontrado")




