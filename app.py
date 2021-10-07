import os
from re import template
from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

app = Flask(__name__)
##postgress
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://banul:2285553a$@localhost:3306/python_for_web"
app.config['SECRET_KEY'] = "random string"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
class Students(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    batch_title = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DATE, default=datetime.now())

class Notification(db.Model):
    __tablename__ = "notification"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    reference_num = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DATE, default=datetime.now())

class Timetable(db.Model):
    __tablename__ = "timetable"
    id = db.Column(db.Integer, primary_key=True)
    session = db.Column(db.String(100), nullable=False)
    monday = db.Column(db.String(100), nullable=False)
    tuesday = db.Column(db.String(100), nullable=False)
    wednesday = db.Column(db.String(100), nullable=False)
    thursday = db.Column(db.String(100), nullable=False)
    friday = db.Column(db.String(100), nullable=False)



# @app.route("/", methods=['GET', 'POST'])
# def index():
#     notification = Notification.query.all()
#     return render_template("note.html",  notification=notification)
@app.route("/batch/<bt>", methods=['GET'])
def batch_filter(bt):
    students = Students.query.filter(Students.batch_title == bt).all()
    return render_template("intro.html", students=students)

@app.route("/", methods=['GET', 'POST'])
def index():
    # session.query(Notification).join(timedelta).count()
    notification = Notification.query.all()
    timetable = Timetable.query.all()
    noteCount = Notification.query.count()
    timeCount = Timetable.query.count()
    return render_template("graph.html", noteCount=noteCount, timeCount=timeCount, notification=notification, timetable=timetable)


@app.route("/table", methods=['GET'])
def table():
    return render_template("table.html")


@app.route('/time', methods=['GET', 'POST'])
def time():
    time = Timetable.query.all()
    return render_template("time.html", time=time)



@app.route('/show', methods=['GET', 'POST'])
def show():
    timetable = Timetable.query.all()
    return render_template("table.html", timetable=timetable)

@app.route("/add_table", methods=['GET', 'POST'])
def add_table():
    if request.method == "POST":
        session = request.form.get("session")
        monday = request.form.get("monday")
        tuesday = request.form.get("tuesday")
        wednesday = request.form.get("wednesday")
        thursday = request.form.get("thursday")
        friday = request.form.get("friday")
        # Creat new record
        time = Timetable(session=session, monday=monday, tuesday=tuesday, wednesday=wednesday, thursday=thursday,
                         friday=friday)
        db.session.add(time)
        db.session.commit()
        timetable = Timetable.query.all()
        return render_template("table.html", timetable=timetable)
    return render_template("add_time.html")

@app.route("/time", methods=['GET', 'POST'])
def Go():
    if request.method == "POST":
        session = request.form.get("session")
        monday = request.form.get("monday")
        tuesday = request.form.get("tuesday")
        wednesday = request.form.get("wednesday")
        thursday = request.form.get("thursday")
        friday = request.form.get("friday")
        # Creat new record
        time = Timetable(session=session, monday=monday, tuesday=tuesday, wednesday=wednesday, thursday=thursday,
                         friday=friday)
        db.session.add(time)
        db.session.commit()
        timetable = Timetable.query.all()
        return render_template("table.html", timetable=timetable)
    return render_template("add_time.html")

@app.route("/form/<int:id>", methods=['GET', 'POST'])
def form(id):
    #note = Notification.query.all()
    note = Notification.query.filter_by(id = id).first()
    return render_template("form.html", note=note, id=id)

@app.route("/insert", methods=['GET', 'POST'])
def insert():
    if request.method == "POST":
        title = request.form.get("title")
        reference_num = request.form.get("reference_num")
        content = request.form.get("content")
        # Creat new record
        note= Notification(title = title, reference_num = reference_num, content = content)
        db.session.add(note)
        db.session.commit()
        notification = Notification.query.all()
        return render_template("note.html", notification=notification)
    return render_template("add_note.html")



@app.route("/view", methods=['GET', 'POST'])
def view():
    if request.method == "POST":
        title = request.form.get("title")
        reference_num = request.form.get("reference_num")
        content = request.form.get("content")
        # Creat new record
        note= Notification(title = title, reference_num = reference_num, content = content)
        db.session.add(note)
        db.session.commit()
        notification = Notification.query.all()
        return render_template("note.html", notification=notification)
    return render_template("add_note.html")

@app.route("/intro", methods=['POST', 'GET'])
def intro():
    if request.method == "POST":
        title = request.form.get("title")
        reference_num = request.form.get("reference_num")
        content = request.form.get("content")
        # Get all records again
        notification = Notification.query.all()
        return render_template("intro.html", notification=notification)
    else:
        notification = Notification.query.all()
        return render_template("intro.html", notification=notification)
@app.route("/update/<int:id>/", methods=['POST','GET'])
def update(id):
    if request.method == "POST":
        title = request.form.get("title")
        reference_num = request.form.get("reference_num")
        content = request.form.get("content")
        note = Notification.query.filter_by(id = id).first()
        note.title = title
        note.ref_num = reference_num
        note.content = content
        db.session.commit()
        return redirect(url_for('intro'))
    else:
        note = Notification.query.filter(Notification.id == id).first()
        return render_template("update.html", note=note, id=id)
@app.route("/delete/<int:id>/", methods=['POST','GET'])
def delete(id):
    if request.method=="POST":
        name = request.form.get("name")
        email = request.form.get("email")
        program = request.form.get("program")
        stud = Students.query.filter_by(id = id).delete()
        db.session.delete(id)
        db.session.commit()
        return redirect(url_for('intro'))
    else:
        stud = Students.query.filter(Students.id == id).delete()
        return render_template("add_student.html", stud=stud, id=id)

if __name__ == "__main__":
    app.run(debug=True)