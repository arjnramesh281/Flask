from flask import Flask, render_template,request,redirect,url_for
import sqlite3
import os

app = Flask(__name__) # to create app 

@app.route('/')
def fun1():
    return('welcome')

@app.route('/fun2')
def fun2():
    return('Fun2')

@app.route('/form',methods=['POST','GET'])
def fun3():
    if request.method=="POST":
        name=request.form['name']
        age=request.form['age']
        print(name,age)
        con = sqlite3.connect("database/form.db")
        con.execute("INSERT INTO User(name,age) values(?,?)",(name,age))
        con.commit()
        return redirect(url_for('fun3'))
    else:
        return render_template('demo.html')
    
@app.route('/view')
def view_data():
    con = sqlite3.connect("database/form.db")
    data=con.execute("SELECT * FROM User")
    for i in data:
        print(data)
    # return render_template('view.html', )

@app.route('/index')
def fun4():
    return render_template('index.html')



# database
os.makedirs("database", exist_ok=True)

# Connect to the database

con = sqlite3.connect("database/form.db") #connection

try:
    con.execute("CREATE TABLE IF NOT EXISTS User (name TEXT, age INTEGER)")
    print("Table created successfully.")
except:
    pass


app.run()