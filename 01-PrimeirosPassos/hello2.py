#Importando o Flask
from flask import Flask

# Define o nome da app
app = Flask(__name__)

# Cria a rota raiz da aplicação
@app.route("/")
def index():
    return "Index!"

# Cria rota hello
@app.route("/hello")
def hello():
    return "Hello World!"

# Cria rota members
@app.route("/members")
def members():
    return "Members"

# Cria um parametro em members que retorna a string que eu colocar após o /members/
@app.route("/members/<string:name>/")
def getMember(name):
    return name

if __name__ == "__main__":
    app.run()