from flask import Flask, render_template, request, jsonify, url_for, redirect
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
import time
app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'servicess'
app.config['MONGO_URI'] = 'mongodb://todo:todo1234@ds117422.mlab.com:17422/servicess'

mongo = PyMongo(app)

@app.route('/')
def index():
    tasks = mongo.db.tasks.find().sort('created_at', pymongo.ASCENDING)
    return  render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    if request.method == 'POST':
        tasks = mongo.db.tasks
        tasks.insert_one({
            'task':request.form['task'],
            'status': 'view',
            'created_at': time.strftime('%d-%m-%Y %H:%M:%S'),
            'updated_at': time.strftime('%d-%m-%Y %H:%M:%S')
        })

        return redirect(url_for('index'))
@app.route('/delete')
def delete_task():
    task=mongo.db.tasks
    task.delete_({'id':ObjectId(oid="5b7a96045e8ed81c64862372")})
    return redirect(url_for('index'))
@app.route('/Remove_all')
def remove_all():
    tasks=mongo.db.tasks
    tasks.remove()
    return redirect(url_for('index'))
@app.route('/update')
def update():
    if request.method == 'POST':
        tasks = mongo.db.tasks
        tasks.update({
            'status': 'completed',
            'created_at': time.strftime('%d-%m-%Y %H:%M:%S'),
            'updated_at': time.strftime('%d-%m-%Y %H:%M:%S')
        })

    return redirect(url_for('index'))

app.run(debug=True)