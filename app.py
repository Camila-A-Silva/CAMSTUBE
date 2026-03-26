from flask import Flask, render_template, request, redirect, session, flash
import mysql.connector
from model.musica import recuperar_msc, salvarmusic, deletar, ativar_msc
from model.genero import recuperar_gen
from model.usuario import cadastro, verificar_usuario

app = Flask(__name__)

app.secret_key = "tinkerbell"

@app.route("/")
def pg_principal():

    # Chamanda o arquivo dos generos
    dic_gen = recuperar_gen()  
    # Chamanda o arquivo das musicas
    dic_msc = recuperar_msc(True)

    return render_template("principal.html", musc_html = dic_msc, gen_html = dic_gen)
   

@app.route("/admin")
def pg_admin():
    if "usuario_logado" not in session:
        return redirect("/login")
    
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
    login = request.form.get("login")
    senha = request.form.get("senha")
    cadastro(login, senha)
    return redirect("/cadastro")

@app.route("/login")
def pg_login():
    if "usuario_logado" in session:
        return redirect("/admin")
    session.clear()
    return render_template("login.html")
    

@app.route("/login", methods=["POST"])
def rota_log():
    login = request.form.get("usuario")
    senha = request.form.get("senha") 
    usuario = verificar_usuario(login, senha)
    session.clear()

    if usuario:
        session["usuario_logado"] = usuario
        return redirect("/admin")
    else:
        flash("Usuário ou senha inválida!","danger")
        return redirect("/login")
    
@app.route("/logoff")
def logoff():
    session.clear()
    return redirect("/login")
   
if (__name__) == "__main__":
    app.run(debug=True)


