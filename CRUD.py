# CRUD-Py-MySQL
#Interação entre Python e MySQL
<HTML>
<HEAD>
<TITLE>Hello</TITLE>
</HEAD>
<BODY>
## Esse é um código para integrar Python e SQL (Backend e banco de dados)
# Será um CRUD
# CREATE
# READ
# UPDATE
# DELETE

import mysql.connector
#Aqui você conecta ao seu servidor MySQL
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='', # Caso não tenha selecionado uma senha, apenas deixe em branco.
    database='bdyoutube',
)
cursor = conexao.cursor()

# CRUD
nome_produto = "todynho"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() # edita o banco de dados



#CREATE
nome_produto = "chocolate"
valor = 15
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit() # edita o banco de dados


#READ
comando = f'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall() # ler o banco de dados
print(resultado)


#UPDATE
nome_produto = "todynho"
valor = 6
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() # edita o banco de dados

#DELETE
nome_produto = "todynho"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() # edita o banco de dados

#Esses dois comandos precisam estar abaixo de uma das interações com o MySQL
cursor.close()
conexao.close()
</BODY>
</HTML>