from flask import Flask, render_template

app = Flask("__name__")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/servicos')
def servicos():
    return render_template('servicos.html')

@app.route('/portifolio')
def portifolio():
    return render_template('portifolio.html')    