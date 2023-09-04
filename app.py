"""
Nao sei pq pede isso, mas ta ai o comentario kk 
"""
from flask import Flask, render_template

app = Flask("Meu Cadu")


# Comenario
@app.route("/")
def home():
    """Rota principal da aplicação"""
    return render_template("home.html")


# Teste teste
@app.route("/novo")
def novo():
    """Nova rota"""
    return "<h1>Eu sou o novo Carlos Eduardo<h1>"
