from flask import Flask

app = Flask(__name__)

@app.route("/")
def initRoute():
    return "Seja bem vindo ao Api Analise Dados"


@app.route("/sobre")
def SobreProjeto():
    return "Projeto de analise de dados: utilizando uma API para esa leitura"


app.run(debug=True)