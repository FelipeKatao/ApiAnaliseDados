from flask import Flask,Blueprint

Register_Dados =  Blueprint("Register_Dados",__name__)

@Register_Dados.route("/database")
def AcessoData():
    return "dados"