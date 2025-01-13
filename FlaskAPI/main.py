from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)
@app.route('/<name>')
def home(name):
    return render_template('Index.html',content = ['name','ranger','sanger'])
# @app.route('/<name>')
# def running(name):
#     return f"hello {name}"

# @app.route('/admin')
# def admin():
#     return redirect(url_for('running',name='admin!'))
if __name__ == '__main__':
    app.run()

# Path to Master Flask for Your Goals
# Basics of Flask:

# Learn how to create simple APIs, handle routes, and manage requests/responses.
# API Development:

# Practice creating RESTful APIs for ML model inference and data pipelines.
# Database Integration:

# Use SQLAlchemy to connect Flask with relational databases like PostgreSQL.
# Model Deployment:

# Deploy ML models as REST APIs using Flask. Learn to load and serve models efficiently.
# Deployment:

# Learn to deploy Flask apps using platforms like Heroku, AWS, or Docker.