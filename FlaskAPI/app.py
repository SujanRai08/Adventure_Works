from datetime import timedelta
from flask import Flask,render_template,request,redirect,url_for,session,flash,message_flashed
app = Flask(__name__)
app.secret_key ='helloworld12'
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route('/')
def home():
    return render_template('Index.html',content = 'Testing')

@app.route('/login', methods=["POST","GET"])
def login():
    if request.method == 'POST':
        user = request.form['user']
        session.permanent = True
        session['users'] = user
        flash('user login successfully','info')
        return redirect(url_for('user',users = user))
    else:
        if 'user' in session:
            return redirect(url_for('user'))
        return render_template('Login.html')


@app.route('/<users>')
def user(users):
    if 'users' in session:
        users = session['users']
        return render_template('userss.html', users = users)
    else:
        flash('not login try again','info')
        return redirect(url_for('login'))
    
@app.route('/logout')
def logout():
    if 'users' in session:
        users = session['users']
        flash(f'you have been logout, {users}','info')
    session.pop('users',None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)