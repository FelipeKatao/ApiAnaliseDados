import logging
from flask import Flask,request,session,Response
from view.data_views import DataRoutes
from controler.data_route import Controler_dadosBrutos

app = Flask(__name__)
DataRoute_= DataRoutes()
DadosBrutos = Controler_dadosBrutos()

app.add_url_rule("/","ListarProdutos",DataRoute_.ListarProdutos)
app.add_url_rule("/dados","ListagemDados",DadosBrutos.ListagemDados)

@app.route("/login")
def loginBase():
    auth = request.authorization
    app.logger.info("logando...")
    if(auth.username != 'DadoMestre'):
        return {'status':'Erro ao logar na conta',f'username':''+auth.get('username')+''}
    
    session['name'] = auth.username
    
    return {"Status":"Logado com sucesso"}

@app.route("/baseDados")
def baseDados():
    if(session.get('name') == "DadosMestre"):
        return DadosBrutos.BaseDados()
    else:
       return Response("{'a':'Erro de autorização'}", status=401)
app.permanent_session_lifetime = 60 
app.secret_key = "SECRET KEY"


logging.basicConfig(filename='C:/Users/SNMACT145/Desktop/ApiAnaliseDados/Data/Dataserver.log')

if(__name__ == '__main__'):
    app.run(debug=True)