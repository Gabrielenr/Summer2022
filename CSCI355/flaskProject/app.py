from flask import Flask, render_template, request, session
import pymysql
import hashlib


app = Flask(__name__)
app.secret_key = 'your secret key'


def connect_to_mars():
    password = read_password()
    conn = pymysql.connect(host="mars.cs.qc.cuny.edu", port=3306, user="ruga8262", passwd=password, database="ruga8262")
    return conn


def read_password():
    password = '14098262'
    return password


@app.route('/states')
def show_states():
    if not session['loggedin']:
        return 'you are not logged in'
    query = "SELECT * FROM state ORDER BY state_name"
    conn = connect_to_mars()
    cursor = conn.cursor()
    cursor.execute(query)
    states = cursor.fetchall()
    conn.commit()
    conn.close()
    headers = ['Name', 'Abbreviation', 'Capital']
    return render_template('states.html', headers=headers, data=states)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('login.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    msg = ''
    if request.method == 'POST' and 'login' in request.form and 'password' in request.form:
        conn = connect_to_mars()
        cursor = conn.cursor()
        typed_login = request.form['login']
        typed_password = request.form['password']
        md5_password = hashlib.md5(typed_password.encode('utf-8')).hexdigest()
        query = "SELECT login FROM app_user WHERE login = '" + typed_login + "' AND pwd = '" + md5_password + "'"
        print(query)
        cursor.execute(query)
        user_row = cursor.fetchone()
        if user_row:
            session['loggedin'] = True
            session['login'] = user_row[0]
            msg = 'Logged in successfully !'
            return show_states()
        else:
            msg = 'Incorrect username / password !'
            # not rendering login.html if password is incorrect.
            # jinja2.exceptions.TemplateNotFound: login.html
            # return render_template('login.html', msg=msg)
    print(msg)
    return msg


if __name__ == '__main__':
    app.run()
