from flask import render_template, request, redirect, url_for
from app import app
from app.models import Todolist
from app import db
import datetime

dt = None
flag = 0


@app.route('/')
def index():
    activ_tasks = Todolist.query.filter_by(check_task=False).all()
    completed_tasks = Todolist.query.filter_by(check_task=True).all()
    return render_template('index.html', incomplete=activ_tasks, complete=completed_tasks, curr_date=dt, flag=flag)


@app.route('/add', methods=['POST'])
def add_task():
    if request.method == 'POST':
        global dt
        dt = datetime.datetime.strptime(request.form.get('deadline'), '%Y-%m-%dT%H:%M')
        date = Todolist.query.filter_by(task_date=dt).all()
        if date:
            global flag
            flag = 1
        else:
            new_task = Todolist(task=request.form['task'], task_date=dt,
                                check_task=False)
            db.session.add(new_task)
            db.session.commit()
            flag = 0
        return redirect(url_for('index'))


@app.route('/check_task/<int:id>')
def check_status(id):
    task = Todolist.query.get(id)
    task.check_task = True
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete')
def delete_all_complete():
    completed_tasks = Todolist.query.filter_by(check_task=True).all()
    for i in completed_tasks:
        db.session.delete(i)
    db.session.commit()
    return redirect(url_for('index'))
