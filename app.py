"""
Nao sei pq pede isso, mas ta ai o comentario kk 
"""
from flask import Flask, render_template, redirect, url_for

app = Flask("Meu Cadu")


# Comenario
@app.route("/")
def home():
    """Rota principal da aplicação"""
    return render_template("home.html")


@app.route("/novo")
def novo():
    """Nova rota"""
    return "<h1>Eu sou o novo Carlos Eduardo<h1>"


@app.route("/redireciona")
def redireciona():
    """Redireciona para a rota novo"""
    return redirect(url_for("novo"))
