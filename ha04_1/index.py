from flask import Flask, request, redirect, url_for, render_template as render
from config import config

app = Flask(__name__)
config.init_db()


@app.route('/')
def index():
    posts = config.get_posts()
    return render('index.html', posts=posts)


@app.route('/<int:post_id>')
def post(post_id):
    post = config.get_post(post_id)
    return render('post.html', number=post[0], title=post[1], content=post[3], date=post[2])


@app.route('/del/<int:post_id>')
def del_post(post_id):
    config.del_post(post_id)
    return index()


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'GET':
        return render('create.html')
    else:
        title = request.form['title']
        content = request.form['content']
        msg = None
        alert = None
        if title and content:
            config.new_post(title, content)
            msg = 'New post was added successfully'
            alert = 'alert-success'
        else:
            msg = 'Please, fill in the required fields: title and content'
            alert = 'alert-warning'
        print(msg)
        return render('create.html', message=msg, alert=alert)
