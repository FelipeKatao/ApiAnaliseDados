from flask import Flask,request,session
from view.data_views import DataRoutes
from controler.data_route import Controler_dadosBrutos

app = Flask(__name__)
DataRoute_= DataRoutes()
DadosBrutos = Controler_dadosBrutos()

app.add_url_rule("/","ListarProdutos",DataRoute_.ListarProdutos)
app.add_url_rule("/dados","ListagemDados",DadosBrutos.ListagemDados)

@app.route("/login")
def loginBase():
    session['username'] = 'DadosMestre'
    return {"Status":"Logado com sucesso"}

@app.route("/baseDados")
def baseDados():
    auth = request.authorization
    if(auth and auth.username == "DadosMestre"):
        return DadosBrutos.BaseDados()
    else:
        {"status":"Login Requerido"}

app.permanent_session_lifetime = 60 
app.secret_key = "SECRET KEY"

if(__name__ == '__main__'):
    app.run(debug=True)