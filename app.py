from flask import Flask

app = Flask(__name__)
# Comenario
@app.route('/')
def hello():
    return "Eu sou o Carlos Eduardo"
    
@app.route('/novo')
def novo():
    return "<h1>Eu sou o novo Carlos Eduardo<h1>"
