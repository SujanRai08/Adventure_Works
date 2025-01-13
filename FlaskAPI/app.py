from flask import Flask,render_template,request,redirect,url_for,session
app = Flask(__name__)
app.secret_key ='helloworld12'

@app.route('/')
def home():
    return render_template('Index.html',content = 'Testing')

@app.route('/login', methods=["POST","GET"])
def login():
    if request.method == 'POST':
        user = request.form['user']
        session['users'] = user
        return redirect(url_for('user',users = user))
    else:
        if 'user' in session:
            return redirect(url_for('user'))
        return render_template('Login.html')


@app.route('/<users>')
def user(users):
    if 'users' in session:
        users = session['users']
        return f"<h1>{users}</h1>"
    else:
        return redirect(url_for('login'))
    
@app.route('/logout')
def logout():
    session.pop('users',None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)