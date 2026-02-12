from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)

app.secret_key = "202026"

lista_comentario = []

@app.route("/")
def pg_principal():
    return render_template("principal.html")

@app.route("/adm")
def pg_adm():
    return render_template


if (__name__) == "__main__":
    