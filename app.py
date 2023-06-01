from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://admin:spameggs123@localhost:5432/flask_todo_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    date_created = db.Column(db.Date())
    is_completed = db.Column(db.Boolean, default=False)

@app.cli.command('create')
def create_db():
    db.drop_all()
    db.create_all()
    print('Tables created successfully')  



@app.route('/todos', methods=['POST'])
def create_todo():
    
    # I need to somehow set Todo.title to the user input
    # Everything else is taken care of by the model
    # I need to link the creation of this todo (the POST api call) to the submit button/enter key
    # I need to render this todo to the page
    title = request.form.get('title')
    new_todo = Todo(title=title, date_created=date.today())
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/todos', methods=['GET'])
def get_todo():
    pass

@app.route('/todos', methods=['PUT'])
def update_todo():
    pass

@app.route('/todos', methods=['DELETE'])
def delete_todo():
    pass

@app.route('/')
def index():
    # display Todos
    todo_list = Todo.query.all()
    return render_template('index.html', todo_list=todo_list)


if __name__ == "__main__":

    app.run(debug=True)