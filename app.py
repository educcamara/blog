"""
Nao sei pq pede isso, mas ta ai o comentario kk 
"""
from flask import Flask, render_template

app = Flask("Meu Cadu")

# Banco de dados Mock
posts_list = [
    {
        "titulo": "Andre: a thread", 
        "texto": "teste teste", 
        "data": "01/01/2021"},
    {
        "titulo": "Jaide: o merda",
        "texto": "segundo teste",
        "data": "01/03/2022"},
    {
        "titulo": "Por que guilhermes tendem a serem mais gostosos",
        "texto": "terceiro teste",
        "data": "05/10/2023"}
]


# Comenario
@app.route("/")
def home():
    """Rota principal da aplicação"""
    return render_template("main.html")


@app.route("/sobre")
def sobre():
    """Rota sobre"""
    return render_template("sobre.html")


@app.route("/posts")
def posts():
    """Rota posts"""
    return render_template("posts.html", posts=posts_list)
