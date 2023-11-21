
import logging
from flask import request,session,Blueprint

Login_route = Blueprint("Login_route",__name__)

@Login_route.route("/login")
def loginBase():
    auth = request.authorization
    logging.info("Aviso sobre tal coisa")
    if(auth.username != 'DadoMestre'):
        Login_route.logger.error("Login realizado com falha"+str(auth.get('username')))
        return {'status':'Erro ao logar na conta',f'username':''+auth.get('username')}
    session['name'] = auth.username
    return {"Status":"Logado com sucesso"}

@Login_route.route("/baseDados")
def baseDados():
    if(session.get('name') == "DadoMestre"):
        return Login_route.BaseDados()
    else:
       return {'a':'Erro de autorização'}