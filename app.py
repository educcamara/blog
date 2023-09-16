""" My Blog Site """
import sqlite3
from flask import Flask, render_template, request, redirect, \
    flash, url_for, session, abort, g

app = Flask(__name__)
app.secret_key = 'cadu'
app.config["DATABASE"] = "posts.db"

def connect():
    """ Connect to database """
    return sqlite3.connect(app.config["DATABASE"])


@app.before_request
def before_request():
    """ Connect to database before request """
    g.db = connect()


@app.teardown_request
def teardown_request(exception):
    """ Close database connection after request """
    if exception:
        pass
    if hasattr(g, 'db'):
        g.db.close()


#
#
#

@app.route('/')
def home():
    """ Homepage """
    return render_template('home.html')


@app.route('/about')
def about():
    """ About page """
    return render_template('about.html')


@app.route('/blog')
def blog():
    """ Blog page """
    sql_str = "SELECT title, body, created_at FROM posts ORDER BY id DESC"
    cur = g.db.execute(sql_str)

    posts = []
    for title, body, created_at in cur.fetchall():
        posts.append({
            'title': title, 
            'body': body, 
            'created_at': created_at
            })
    return render_template('all_posts.html', posts=posts)


@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    """ Blog post page """
    sql_str = "SELECT title, body, created_at FROM posts WHERE id = ?"
    cur = g.db.execute(sql_str, [post_id])

    title, body, created_at = cur.fetchone()
    post = {
        'title': title, 
        'body': body, 
        'created_at': created_at
        }
    return render_template('single_post.html', post=post)


@app.route('/new_post')
def new_post():
    """ New post page """
    if not session['logged_in']:
        abort(401)
    return render_template('new_post.html')


@app.route('/create_post', methods=['POST'])
def create_post():
    """ Create post """
    if not session['logged_in']:
        abort(401)
    title = request.form['title']
    body = request.form['body']

    sql_str = "INSERT INTO posts (title, body) VALUES (?, ?)"
    g.db.execute(sql_str, [title, body])
    g.db.commit()

    flash('Post criado com sucesso!')
    return redirect(url_for('blog'))


#
# Login & Logout
#

@app.route('/login', methods=['GET', 'POST'])
def login():
    """ Login page """
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Senha ou usuário inválidos'
        else:
            session['logged_in'] = True
            flash('Salve ADM!')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    """ Logout page """
    session.pop('logged_in')
    flash('Até mais ADM!')
    return redirect(url_for('home'))
