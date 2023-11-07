from flask import Flask
from blueprints.Dados import Register_Dados

app = Flask(__name__)
app.register_blueprint(Register_Dados)

@app.route("/")
def initRoute():
    return "Seja bem vindo ao Api Analise Dados"


@app.route("/sobre")
def SobreProjeto():
    return "Projeto de analise de dados: utilizando uma API para esa leitura"

if(__name__ == '__main__'):
    app.run(debug=True)