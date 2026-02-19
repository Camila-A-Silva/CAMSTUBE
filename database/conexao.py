import mysql.connector

def conectar():
# Conectando no banco de dados
    conexao = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "root",
        database = "CamsTube"
    )

    cursor = conexao.cursor(dictionary=True)

    return conexao, cursor

   