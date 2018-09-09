# from flask import Flask, render_template, request, jsonify, url_for, redirect
# from flask_sqlalchemy import SQLAlchemy
# from bson.objectid import ObjectId
# import time
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:03142108238@localhost/todoapp'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db=SQLAlchemy(app)
# class Todo():
#     id=db.Column(db.Integer,primary_key=True)
#     text=db.Column(db.String(200))
#     complete = db.Column(db.Boolean)
# @app.route('/')
# def index():
#     incomplete = Todo.query.filter_by(complete=False).all()
#     complete = Todo.query.filter_by(complete=True).all()
#
#     return render_template('index.html', incomplete=incomplete, complete=complete)
#
#
# @app.route('/add', methods=['POST'])
# def add():
#     todo = Todo(text=request.form['todoitem'], complete=False)
#     db.session.add(todo)
#     db.session.commit()
#
#     return redirect(url_for('index'))
# @app.route('/complete/<id>')
# def complete(id):
#     todo = Todo.query.filter_by(id=int(id)).first()
#     todo.complete = True
#     db.session.commit()
#
#     return redirect(url_for('index'))
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:03142108238@localhost/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class Example(db.Model):
    __tablename__ = 'furqzn'
    q = db.Column(db.Integer, primary_key=True)
    data = db.Column('data',db.Unicode)
    def __init__(self ,q,data):
        self.q=q
        self.data=data
