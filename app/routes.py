from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'username': 'zek' }
    posts = [
        {
            'author': { 'username': 'zek' },
            'body': 'Comment of zek'
        },
        {
            'author': { 'username': 'mah' },
            'body': 'Comment of mah'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
