from flask import Flask, render_template, redirect, url_for

app = Flask("Meu Cadu")
# Comenario
@app.route('/')
def hello():
    return render_template('home.html')
    
@app.route('/novo')
def novo():
    return "<h1>Eu sou o novo Carlos Eduardo<h1>"

@app.route('/redireciona')
def redireciona():
    return redirect(url_for('novo'))
