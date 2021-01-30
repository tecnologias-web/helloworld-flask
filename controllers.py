from app import app
from flask import render_template, request


@app.route('/ola')
def hello_world():
    return render_template('ola.html')


@app.route('/form', methods=['GET', 'POST'])
def formulario():

    if request.method == 'POST':
        print('Isso é um POST feito por', request.form['nome'])
    else:
        print('Isso é um GET!')

    return render_template('form.html')
