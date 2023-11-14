from flask import Flask,Blueprint

Register_Dados =  Blueprint("Register_Dados",__name__)

@Register_Dados.route("/database")
def AcessoData():
    return {"Dado":[2,4,6,4,6,67,4,4,43],
            "Titulo":"Analise de dados X"}