from app import db, app
import datetime


class Todolist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(250), nullable=False)
    task_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime)
    check_task = db.Column(db.Boolean)

    def __repr__(self):
        return f"<task {self.task}, {self.check_task}, {self.crt_date}>"


with app.app_context():
    db.create_all()
