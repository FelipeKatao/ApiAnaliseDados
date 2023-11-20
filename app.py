from flask import Flask,render_template,jsonify,session,request
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

@app.route('/profile')
def profile():
    username = session.get('username')
    auth = request.authorization
    auth.username = 'User'
    app.session_interface.save_session()
    if auth and auth.username == 'User':
        return 'Autorizado'
    print("==========================")
    if username is not None:
        return "Você esta logado"
    return "sign in"

app.permanent_session_lifetime = 60
app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'

if(__name__ == '__main__'):
    app.run(debug=True)