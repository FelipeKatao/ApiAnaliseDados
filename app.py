import logging
import io
import os
from flask import Flask,request,g,redirect,url_for
import requests
from functools import wraps
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
#app.url_map.add(Rule('/', endpoint='index'))
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.add_url_rule("/","ListarProdutos",DataRoute_.ListarProdutos,methods=['GET','POST'])
app.add_url_rule("/dados","ListagemDados",DadosBrutos.ListagemDados) 
user = None
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if user == None:
            return "404";
        return f(*args, **kwargs)
    return decorated_function
 
@app.route('/secret_page')
@login_required
def secret_page():
    pass  

@app.get("/imagem/<nome>/<receita>")
def ObterImagem(nome,receita):
    ObterCaminhoRelativo = os.path.relpath("./static/upload/"+nome)   #Caminho relativo 
    for i  in os.listdir(path=ObterCaminhoRelativo):
        if(receita in i):
            return ObterCaminhoRelativo+"/"+i
    return "Imagem não existe"

@app.post("/upload/<nome>/<receita>")
def Upload(nome,receita):
    input_file = request.files['file'].read()                   #Recebendo e lendo o arquivo recebido
    f = BytesIO(input_file)                                     # Transformando em Bytes 
    NomeArquivo= request.files['file'].filename                 #Nome do arquivo
    
    NomeReceita = receita+"."+NomeArquivo.split(".")[1]         #Escrever o nome do  arquivo
    Nm_Tipo = request.files['file'].content_type                #Tipo do Arquivo
    PastaExistente = False                                      # Variavel para verificar se a pasta existe
    ObterCaminhoRelativo = os.path.relpath("./static/upload")   #Caminho relativo 

    for i  in os.listdir(path=ObterCaminhoRelativo):
        if(i == nome):                                          #Verifica se a pasta existe
            PastaExistente = True                               # Se existe fica Verdadeiro
    
    if(PastaExistente == False):                                #Verificar se existe a pasta pela variavel
        os.mkdir("static/upload/"+nome)                         #Criar pasta para o usuario

    if( str("image") in Nm_Tipo):                               #Validao de arquivo
        with open(f"./static/upload/{nome}/{NomeReceita}", 'wb') as f: #Abrindo para leitura de Bits
            f.write(input_file) #Escrevendo de Bits para Arquvio
        return "Arquivo concluido!"
    
    return "Arquivo não suportado"


@app.route("/static/upload/<nome>/<param>")
def RouteValues(nome,param):
    return "Aceso negado"

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
    
