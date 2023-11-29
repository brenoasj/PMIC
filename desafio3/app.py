from flask import Flask, render_template, request 
from flask_mysqldb import MySQL
import os
from dotenv import load_dotenv

app = Flask("__name__")

app.config["MYSQL_Host"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD")
app.config["MYSQL_DB"] = "elitehoopers"

db = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/servicos')
def servicos():
    return render_template('servicos.html')

@app.route('/contato', methods = ["POST","GET"])
def contato():
    if request.method == "POST":
        nome = request.form['nome']
        email = request.form['email']
        tel = request.form['tel']
        mensagem = request.form['mensagem']
        if nome == '' or email == '' or tel == '' or mensagem  == '':
             return render_template('contato.html', status = 'Erro algum dos campos está vazio')
        cursor =  db.connection.cursor()
        cursor.execute(f"insert into contatos (nome, email, tel, mensagem) values ('{nome}', '{email}', {tel}, '{mensagem}')")
        db.connection.commit() 
        cursor.close()  
        return 'sucesso'          
    return render_template('contato.html')

@app.route('/users')
def users():
        cursor = db.connection.cursor()
        users = cursor.execute("select * from contatos")
        if users > 0:
            userDetails = cursor.fetchall()
            return render_template('users.html', userDetails = userDetails)
        else:
            return render_template('users.html')
            

  