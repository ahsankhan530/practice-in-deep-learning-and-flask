from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:03142108238@localhost/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = b'dE\xad2g\x0c\x8d\xb9\x1cq\x86\x04:\xa8>\xc7\xc5\xc2Dr\xe7f\xf9\xeb'

db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)


@app.route('/')
def index():
    incomplete = Todo.query.filter_by(complete=False).all()
    complete = Todo.query.filter_by(complete=True).all()

    return render_template('index.html', incomplete=incomplete, complete=complete)


@app.route('/add', methods=['POST'])
def add():
    todo = Todo(text="Ahsan", complete=False)
    db.session.add(todo)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/complete/<id>')
def complete(id):
    todo = Todo.query.filter_by(id=int(id)).first()
    todo.complete = True
    db.session.commit()

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)