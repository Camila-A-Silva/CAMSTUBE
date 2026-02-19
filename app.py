from flask import Flask, render_template
import mysql.connector
from model.musica import recuperar_msc
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


if (__name__) == "__main__":
    app.run(debug=True)


