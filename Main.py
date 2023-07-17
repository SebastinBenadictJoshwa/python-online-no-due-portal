from flask import Flask,  session, send_from_directory, render_template,  request, redirect
import os
import datetime
import mysql.connector

app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'



@app.route("/")
def homepage():
    return render_template('index.html')


@app.route("/AdminLogin")
def AdminLogin():
    return render_template('AdminLogin.html')


@app.route("/StudentLogin")
def StudentLogin():
    return render_template('StudentLogin.html')

@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    error = None
    if request.method == 'POST':
        if request.form['uname'] == 'admin' and request.form['password'] == 'admin':

            return render_template('AdminHome.html')

        else:
            error="Incorrect Username or Password"
            return render_template('index.html', error=error)

@app.route("/admin")
def admin():
    return render_template("AdminHome.html")

@app.route("/approve_nodue/<string:id>")
def approve_nodue(id):
    conn = mysql.connector.connect(user='root', password='', host='localhost', port='3307', database='1CollegeAsspy')
    cursor = conn.cursor()
    cursor.execute("UPDATE noduetb SET status='Approved' WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return redirect("/NoDueManagement")

@app.route("/reject_nodue/<string:id>")
def reject_nodue(id):
    conn = mysql.connector.connect(user='root', password='', host='localhost', port='3307', database='1CollegeAsspy')
    cursor = conn.cursor()
    cursor.execute("UPDATE noduetb SET status='Rejected' WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return redirect("/NoDueManagement")

@app.route("/Applications")
def Applications():
    conn = mysql.connector.connect(user='root', password='', host='localhost', port='3307', database='1CollegeAsspy')
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM noduetb WHERE status='Pending'")
    data=cursor.fetchall()
    return render_template("Pending.html", data=data)

@app.route("/NewStudent1", methods=['GET', 'POST'])
def NewStudent1():
    if request.method == 'POST':
        regno = request.form['regno']
        name = request.form['name']
        gender = request.form['gender']
        Age = request.form['Age']
        email = request.form['email']
        pnumber = request.form['pnumber']
        address = request.form['address']
        Degree = request.form['degree']
        depart = request.form['dept']
        year1 = request.form['year1']
        conn = mysql.connector.connect(user='root', password='', host='localhost', port='3307', database='1CollegeAsspy')
        cursor = conn.cursor()
        cursor.execute(
            "insert into regtb values('" + regno + "','" + name + "','" + gender + "','" + Age + "','" + email + "','" + pnumber + "','" + address + "','" + Degree + "','" + depart + "','" + year1 + "')")
        conn.commit()
        conn.close()
    conn = mysql.connector.connect(user='root', password='', host='localhost', port='3307', database='1CollegeAsspy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb")
    data = cur.fetchall()
    return render_template('AdminStudentInfo.html', data=data)


@app.route("/AdminStudentInfo")
def AdminStudentInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', port='3307', database='1CollegeAsspy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb")
    data = cur.fetchall()
    return render_template('AdminStudentInfo.html', data=data)

@app.route("/NoDueManagement")
def NoDueManagement():
    conn = mysql.connector.connect(user='root', password='', host='localhost', port='3307', database='1CollegeAsspy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM noduetb")
    data = cur.fetchall()
    return render_template('NoDueManagement.html', data=data)

@app.route("/studentlogin", methods=['GET', 'POST'])
def studentlogin():
    error = None
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['regno'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', port='3307', database='1CollegeAsspy')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where regno='" + username + "' and Phone='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            error="Incorrect Username or Password"
            return render_template('index.html',error=error)
        else:
            print(data[0])
            session['uid'] = data[0]
            conn = mysql.connector.connect(user='root', password='', host='localhost', port='3307', database='1CollegeAsspy')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where regno='" + username + "' and Phone='" + password + "'")
            data = cur.fetchall()

            return render_template('StudentHome.html', data=data)

@app.route("/student")
def Student1():
    conn = mysql.connector.connect(user='root', password='', host='localhost', port='3307', database='1CollegeAsspy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where regno='" + session['regno']+"'")
    data = cur.fetchall()
    return render_template('StudentHome.html', data=data)

@app.route("/StudentRequest")
def StudentRequest():
    return render_template("Student Request.html")

@app.route("/NoDueRequest", methods=['GET', 'POST'])
def NoDueRequest():
    if request.method == 'POST':
        regno = session['regno']
        department = request.form['department']
        year = request.form['year']
        request_date = datetime.datetime.now().strftime("%Y-%m-%d")
        status = 'Pending'
        conn = mysql.connector.connect(user='root', password='', host='localhost', port='3307', database='1CollegeAsspy')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO noduetb (regno, department, year, request_date, status) VALUES (%s, %s, %s, %s, %s)", (regno, department, year, request_date, status))
        conn.commit()
        conn.close()
    conn = mysql.connector.connect(user='root', password='', host='localhost', port='3307', database='1CollegeAsspy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM noduetb where regno='" + session['regno'] + "'")
    data = cur.fetchall()
    return render_template('Status.html', data=data)

@app.route("/Status")
def Status():
    conn = mysql.connector.connect(user='root', password='', host='localhost', port='3307', database='1CollegeAsspy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM noduetb where regno='" + session['regno'] + "'")
    data = cur.fetchall()
    return render_template('Status.html', data=data)

@app.route('/generate_report')
def generate_report():
    conn = mysql.connector.connect(user='root', password='', host='localhost', port='3307', database='1CollegeAsspy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb WHERE regno = %s", (session['regno'],))
    data = cur.fetchone()
    name = data[1]
    regno = data[0]
    dept = data[7]
    year = data[9]
    phone = data[5]
    filename = f"{regno}.html"
    filepath = os.path.join(app.root_path, 'static/upload', filename)
    with open(filepath, 'w') as f:
        f.write(render_template('report.html', name=name, regno=regno, dept=dept, year=year, phone=phone))
    directory = os.path.join(app.root_path, 'static/upload')
    return send_from_directory(directory, filename, as_attachment=True)
  

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
