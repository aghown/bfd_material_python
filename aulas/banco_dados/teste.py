# importando o driver do mysql
import mysql.connector


# inicia a conexao com o banco de dados.
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="Fred",
    password="fred1234",
    database="sakila"
)

# cria o cursor
cursor = db_connection.cursor()

# executa qualquer comando SQL
cursor.execute("""
SELECT * 
FROM actor
""")

# Salva o resultado da query na variável
#query_result = cursor.fetchall()

# Imprime o resultado da query
#print(query_result)

for linha in cursor:
    print(linha)

# Encerra a conexao com o banco de dados
db_connection.close()
