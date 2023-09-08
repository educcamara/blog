""" My Blog Site """
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """ Homepage """
    return render_template('home.html')
