from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


@app.route('/')
def index():
    # show all todos
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template('base.html', todo_list=todo_list)


@app.route('/about')
def about():
    return "<h3>About<h3>"


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == "__main__":
    db.create_all()
    db.session.commit()
    new_todo = Todo(title='todo 1', complete=False)
    db.session.add(new_todo)
    db.session.commit()

    app.run(debug=True)
