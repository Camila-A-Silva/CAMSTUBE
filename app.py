from flask import Flask, render_template, request, redirect
import mysql.connector
from model.musica import recuperar_msc, salvarmusic, deletar, ativar_msc
from model.genero import recuperar_gen
from model.usuario import cadastro

app = Flask(__name__)

@app.route("/")
def pg_principal():

    # Chamanda o arquivo dos generos
    dic_gen = recuperar_gen()  
    # Chamanda o arquivo das musicas
    dic_msc = recuperar_msc(True)

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

# O que está entre <> é o valor que vai ser excluida

@app.route("/musica/delete/<codigo>")
def pg_deletar_msc(codigo):
    deletar(codigo)
    return redirect("/admin")

# Vai ativar ou deativar

@app.route("/musica/ativar/<codigo>/<ativo>")
def pg_ativar_msc(codigo,ativo):
    ativar_msc(codigo,ativo)
    return redirect("/admin")

@app.route("/cadastro")
def pg_cadastro():
    return render_template("cadastro.html")

@app.route("/cadastro", methods=["POST"])
def rota_cad():
    dic_usu = request.form.get("usuario")
    dic_sen = request.form.get("senha")
    cadastro(dic_usu, dic_sen)
    return redirect("/cadastro")

@app.route("/login")
def pg_login():
    return render_template("login.html")
   



if (__name__) == "__main__":
    app.run(debug=True)


