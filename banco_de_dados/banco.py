import sqlite3
import datetime
import time
import random

connection = sqlite3.connect('livros.db')
c = connection.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS  livros (codigo_livro integer, nome_do_livro TEXT, nome_do_autor text, ano TEXT, edicao real, data_de_indexacao TEXT)')


def dataentry():
    c.execute("INSERT  INTO livros VALUES (1,'matematica para burros' , 'Gabriel', '11-jun-2018', 2.0,'12-jun-2018','1' )")
    connection.commit()
    c.close()
    connection.close()

def gerar_data():
    hora=time.time
    data_de_indexacao=datetime.datetime.fromtimestamp(hora).strftime('%D-%m-%y %H:%M:%S')
    codigo_livro=random.randrange(0,100)
    c.execute("INSERT  INTO livros(hora,data_de_indexacao,codigo_livro) VALUES (?,?)",( data_de_indexacao,codigo_livro))



def ler_do_bando():
    c.execute('SELECT  * FROM livros')
    #data=c.fetchall()
    #print(data)

    for row in c.fetchall():
        print(row[0])


#create_table()
#for i in range(10):
#    gerar_data()
#    time.sleep(1)
#ler_do_bando()

gerar_data()
c.close()
connection.commit()



#dataentry()



