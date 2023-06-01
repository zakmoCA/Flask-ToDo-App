from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://admin:spameggs123@localhost:5432/flask_todo_app'

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    date_created = db.Column(db.Date())
    is_completed = db.Column(db.Boolean, default=False)

@app.cli.command('create')
def create_db():
    db.create_all()
    print('Tables created successfully')  

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)