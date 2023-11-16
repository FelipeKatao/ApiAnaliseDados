from flask import Flask,render_template
from blueprints.Dados import Register_Dados
from service.DataAnalitic_sevice import DataAnaliticService

app = Flask(__name__)
app.register_blueprint(Register_Dados)
__DataAnaliticService = DataAnaliticService()

@app.route("/")
def initRoute():
    return "seja bem vindo a analise de dados "


@app.route("/<database>")
def AcessarDados(database):
    return __DataAnaliticService.AcessarDadosBrutos(database)

@app.route("/d")
def DadosBrutos():
    return "0"


if(__name__ == '__main__'):
    app.run(debug=True)