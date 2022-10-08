#Importa funções do flask
from flask import Flask, flash, redirect, render_template, request, session, abort

# render_template - renderiza o template
# Cria a aplicação
app = Flask(__name__)

# rota raiz
@app.route("/")
def index():
    return "Flask App!"

# rota hello (alimenta o template1.html e retorna o resultado)
@app.route("/hello/<string:name>/")
def hello(name):
    return render_template('template2.html', name=name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)