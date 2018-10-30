from flask import Flask
from flask import render_template,redirect,url_for,abort

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('user_index',username='biyong'))


@app.route('/user/<username>')
def user_index(username):
    if username == 'invalid' :
        abort(404)
    return render_template('user_index.html',username=username)

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'),404

if __name__ == '__main__':
    app.run(debug=True)


