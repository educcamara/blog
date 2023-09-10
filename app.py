""" My Blog Site """
from flask import Flask, render_template, request, redirect, \
    flash, url_for, session, abort
from posts import blog_posts

app = Flask(__name__)
app.config['SECRET KEY'] = 'cadu'


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
    posts = blog_posts
    return render_template('all_posts.html', posts=posts)


@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    """ Blog post page """
    try:
        post = blog_posts[post_id - 1]
        return render_template('post.html', post=post)
    except IndexError:
        abort(404)
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
