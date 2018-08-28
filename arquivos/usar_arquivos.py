arq = open('lista.txt', 'w')
texto = []
texto.append('Lista de Alunos\n')
texto.append('---\n')
texto.append('João da Silva\n')
texto.append('José Lima\n')
texto.append('Maria das Dores')
arq.writelines(texto)
arq.close()