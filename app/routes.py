from flask import render_template, session, request, flash, redirect, url_for
from app import app
import random
import hashlib
#----------------------------------------------------------------
#connect to mysql database
#----------------------------------------------------------------
import mysql.connector
cnx = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="password1779",
  database="PHOTOGRAPHY"
)
#----------------------------------------------------------------
#home page
#----------------------------------------------------------------
@app.route('/')
@app.route('/index')
def index():  
  if 'username' in session:
      username = session['username']  
      #testing database
      cursor = cnx.cursor()
      query = '''SELECT * FROM Users'''
      cursor.execute(query)    
      row = cursor.fetchall()
      cursor.close()
      return render_template('index.html',row=row)
  else:
      return render_template("login.html", error="please login first!")
#----------------------------------------------------------------
#login page
#----------------------------------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")
@app.route('/login_submit', methods=['POST'])
def login_submit():
    uname = request.form['username']
    pword = request.form['password']
    #------authentication---------------
    cursor = cnx.cursor()
    query = '''SELECT * FROM Users WHERE username = %s'''
    cursor.execute(query,(uname,))    
    row = cursor.fetchone()
    cursor.close()
    if row:
            #------check password----------
            salt = row[4]
            db_password = pword+salt
            h = hashlib.md5(db_password.encode())
            if str(h.hexdigest()) == row[3]:
                session['username'] = uname
                flash("You have successfully loggined in!")
                return redirect(url_for('index'))
    return render_template("login.html", error="Invalid Credentials!Try Aagin.")
#----------------------------------------------------------------
#logout page
#----------------------------------------------------------------
@app.route('/logout')
def logout():
  session.pop('username', None)
  return redirect(url_for('index'))
#----------------------------------------------------------------
#register page
#----------------------------------------------------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
  return render_template("register.html")
@app.route('/register_submit', methods=['POST'])
def register_submit():
  uname = request.form['username']
  email = request.form['email'] 
  pword = request.form['password']
  pword2 = request.form['password2']
  #passwords not match
  if pword != pword2:
        return render_template("register.html", error="Password not match!")
  #user exists
  cursor = cnx.cursor()
  query = '''SELECT * FROM Users WHERE username = %s'''
  cursor.execute(query,(uname,))    
  row = cursor.fetchone()
  cursor.close()
  if row:
        return render_template("register.html", error="User already exists!")
  #------generate passwordhash--------
  salt = str(random.randint(1, 20))
  db_password = pword+salt
  h = hashlib.md5(db_password.encode())
  #------register to database---------
  cursor = cnx.cursor()
  query = '''INSERT INTO Users (username,email,password_hash,salt) VALUES (%s,%s,%s,%s)'''
  cursor.execute(query,(uname,email,str(h.hexdigest()),salt))
  cnx.commit()
  cursor.close()
  return redirect(url_for('login'))
#----------------------------------------------------------------
#upload page
#----------------------------------------------------------------
@app.route('/upload', methods=['GET', 'POST'])
def upload():
  if 'username' in session:
      username = session['username']  
      return render_template("upload.html")
  return render_template("login.html", error="please login first!")    
  
@app.route('/upload_submit', methods=['POST'])
def upload_submit():
  return redirect(url_for('index'))