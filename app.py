from flask import Flask
from blueprints.Dados import Register_Dados
from repository.DataAnalitic_sevice import DataAnaliticService

app = Flask(__name__)
app.register_blueprint(Register_Dados)
__DataAnaliticService = DataAnaliticService()

@app.route("/")
def initRoute():
    return "Seja bem vindo ao Api Analise Dados"



@app.route("/sobre")
def SobreProjeto():
    return "Projeto de analise de dados: utilizando uma API para esa leitura" 


@app.route("/dadosbrutos/<database>")
def AcessarDados(database):
    return __DataAnaliticService.AcessarDadosBrutos(database)



if(__name__ == '__main__'):
    app.run(debug=True)