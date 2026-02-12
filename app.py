from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route("/")
def pg_principal():

    # Conectando no banco de dados
    conexao = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "root",
        database = "CamsTube"
    )

    cursor = conexao.cursor(dictionary=True)

    # Executando a consulta
    cursor.execute("SELECT codigo, cantor, duracao, nome, url_imagem, nome_genero FROM musica;")
    # Recuperando os dados 
    dic_msc = cursor.fetchall()
    # Fechando a conexão
    conexao.close()

    return render_template("principal.html", musc_html = dic_msc)

@app.route("/adm")
def pg_adm():
    return render_template("administracao.html")


if (__name__) == "__main__":
    app.run(debug=True)