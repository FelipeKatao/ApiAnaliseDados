from flask import Flask,render_template,jsonify,session,request
from dotenv import load_dotenv
import os 
from blueprints.Dados import Register_Dados
from blueprints.paginas import Paginas_site
from service.DataAnalitic_sevice import DataAnaliticService

app = Flask(__name__)
app.register_blueprint(Register_Dados)
app.register_blueprint(Paginas_site)
__DataAnaliticService = DataAnaliticService()

@app.route("/")
def initRoute():
    return "seja bem vindo a analise de dados "

@app.route("/<database>")
def AcessarDados(database):
    return __DataAnaliticService.AcessarDadosBrutos(database)


@app.route("/d/<d>")
def DadosBrutos(d):
    return "0"

@app.get("/TesteBase")
def route_teste():
    session['username'] = 'Felipe'
    return "GETDATA "+str(session.get('username'))

@app.route('/profile',methods=['GET'])
def profile():
    username = session.get('username')
    if username is not None:
        return "Você esta logado"
    return "sign in"

@app.route('/acesso',methods=['GET'])
def Acesso():
    auth = request.authorization
    load_dotenv()
    print(os.getenv('CHAVE_SECRETA_API'))
    if(auth and auth.username == 'Usuario'):
        return "Logado com sucesso",200
    return "Não possui autorização",401

app.permanent_session_lifetime = 60
load_dotenv()

# b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'
app.secret_key = os.getenv('CHAVE_SECRETA_API')

if(__name__ == '__main__'):
    app.run(debug=True)