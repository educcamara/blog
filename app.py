"""
Nao sei pq pede isso, mas ta ai o comentario kk 
"""
from flask import Flask, render_template

app = Flask("Meu Cadu")

# Banco de dados Mock
posts = [
    {"título": "Andre: a thread", "texto": "teste teste"},
    {"título": "Minha segunda postagem", "texto": "segundo teste"},
]


# Comenario
@app.route("/")
def home():
    """Rota principal da aplicação"""
    return render_template("home.html")


@app.route("/sobre")
def sobre():
    """Rota sobre"""
    return render_template("sobre.html")

