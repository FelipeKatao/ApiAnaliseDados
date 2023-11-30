import logging
from flask import Flask
from routes.login_route import Login_route
from view.data_views import DataRoutes
from controler.data_route import Controler_dadosBrutos
import pymysql

app = Flask(__name__)
DataRoute_= DataRoutes()
DadosBrutos = Controler_dadosBrutos()
app.register_blueprint(Login_route)

app.add_url_rule("/","ListarProdutos",DataRoute_.ListarProdutos,methods=['GET','POST'])
app.add_url_rule("/dados","ListagemDados",DadosBrutos.ListagemDados)

@app.route("/teste")
def testeRota():
    pymysql.Connect.connect_timeout = 5000
    con = pymysql.connect(host='db4free.net',user='usuaro_0_poli',password='9090ola1',port=3306,charset='utf8')

    return 'None'

#logging.basicConfig(filename='C:/Users/SNMACT145/Desktop/ApiAnaliseDados/logs/Dataserver.log')

app.secret_key = "SECRET KEY"
app.permanent_session_lifetime = 60

if(__name__ == '__main__'):
    app.run(debug=True)