from flask import Flask,render_template
from blueprints.Dados import Register_Dados
from repository.DataAnalitic_sevice import DataAnaliticService

app = Flask(__name__)
app.register_blueprint(Register_Dados)
__DataAnaliticService = DataAnaliticService()

@app.route("/")
def initRoute():
    return render_template("paginaInicial.html")

@app.route("/login")
def login():
    return render_template("index.html")


@app.route("/sobre")
def SobreProjeto():
    return {"About":"O projeto é focado em constução de uma aplicação em Python"}


@app.route("/dadosbrutos/<database>")
def AcessarDados(database):
    return __DataAnaliticService.AcessarDadosBrutos(database)

@app.route("/d")
def DadosBrutos():
    return "0"


if(__name__ == '__main__'):
    app.run(debug=True)