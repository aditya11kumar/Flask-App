from Application import app,db
from flask import render_template,request,url_for,redirect,flash
from datetime import datetime
from Application.models import trainee


@app.route("/data", methods=['POST'])
def data():
    if request.method == "POST":
        d1 = request.form['firstName']
        d2 = request.form['middleName']
        d3 = request.form['lastName']
        d4 = request.form['gender']
        d5 = request.form['education']
        d6=request.form['skills']
        d7 = datetime.strptime(request.form['dob'], '%m/%d/%Y')
        d8 = request.form['address']
        d9 = request.form['phone']
        d10 = request.form['email']
        t1 = trainee(d1, d2, d3, d4,  d5, d6, d7, d8, d9, d10)
        db.session.add(t1)
        db.session.commit()
        flash("your data are successfully added") 
    return  redirect(url_for('traineeList') )

@app.route("/details", methods=["POST"])
def details():
    id_detail=request.form['details']
    return  redirect(url_for('traineeDetails',id=id_detail) )
