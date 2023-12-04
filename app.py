from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def mi_pagina():
    return render_template('index.html')

@app.route('/Adios')
def despedida():
    return 'Vamonos!'

if __name__ == '__main__':
    app.run()
