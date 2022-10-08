# Importa framework Flask
from flask import Flask

# Cria a app
app = Flask(__name__)

# Para a app ficar no diretorio raiz
@app.route("/")

# Cria funcao hello
def hello():
    return "Hello World"

if __name__ == "__main__":
    app.run()