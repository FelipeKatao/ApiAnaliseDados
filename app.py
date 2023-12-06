import logging
import io
import os
from flask import Flask,request
import requests
from flask_cors import CORS
from routes.login_route import Login_route
from view.data_views import DataRoutes
from controler.data_route import Controler_dadosBrutos
from io import BytesIO
import pymysql

app = Flask(__name__)
DataRoute_= DataRoutes()
DadosBrutos = Controler_dadosBrutos()
app.register_blueprint(Login_route)
#app.view_functions['static'] = False    
app.app_context()

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.add_url_rule("/","ListarProdutos",DataRoute_.ListarProdutos,methods=['GET','POST'])
app.add_url_rule("/dados","ListagemDados",DadosBrutos.ListagemDados) 

@app.post("/upload")
def Upload():
    input_file = request.files['file'].read()
    f = BytesIO(input_file)
    Nm_id = request.files['file'].filename
    Nm_Tipo = request.files['file'].content_type
    print(Nm_Tipo)
    if( Nm_Tipo == "image/jpeg"):
        with open(f"{Nm_id}.png", 'wb') as f: 
            f.write(input_file)
        return "Arquivo concluido!"
    
    return "Arquivo não suportado"


@app.route("/static/img/<param>")
def RouteValues(param):
    return app.config['UploadFiles']

@app.route("/alterarambiente")
def alet():
    app.name = "ModulosAdicionais"
    return "ambiente trocado com sucesso"

@app.route("/analises")
def RouteReturn():
    if 2>1:
        app.config["UploadFiles"] = "none"
    return "ok"

@app.do_teardown_appcontext
def therd(exception):
    print("Realiza manutenções em caso de erro?")
#logging.basicConfig(filename='C:/Users/SNMACT145/Desktop/ApiAnaliseDados/logs/Dataserver.log')

app.secret_key = "SECRET KEY"
app.permanent_session_lifetime = 60


if(__name__ == '__main__'):
    app.run(debug=True)
    
