from flask import Flask, render_template, request, redirect
import mysql.connector
from model.musica import recuperar_msc, salvarmusic
from model.genero import recuperar_gen

app = Flask(__name__)

@app.route("/")
def pg_principal():

    # Chamanda o arquivo dos generos
    dic_gen = recuperar_gen()  
    # Chamanda o arquivo das musicas
    dic_msc = recuperar_msc()

    return render_template("principal.html", musc_html = dic_msc, gen_html = dic_gen)
   

@app.route("/admin")
def pg_admin():
    dic_msc = recuperar_msc()
    dic_gen = recuperar_gen()
    return render_template("administracao.html", musc_html = dic_msc, gen_html = dic_gen)

@app.route("/musica/post", methods=["POST"])
def api_inserir_musica():
    cantor = request.form.get("cantor")
    duracao = request.form.get("duracao")
    nome_msc = request.form.get("titulo")
    url = request.form.get("url")
    genero = request.form.get("genero")
    if salvarmusic(cantor, duracao, nome_msc, url, genero):
        return redirect("/admin")
    else:
        "Erro ao adicionar música"



if (__name__) == "__main__":
    app.run(debug=True)


