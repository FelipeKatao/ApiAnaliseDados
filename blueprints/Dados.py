from flask import Flask,Blueprint
from controller.dataController import DataControl

Register_Dados =  Blueprint("Register_Dados",__name__)
Data_ = DataControl()

@Register_Dados.route("/database")
def AcessoData():
    return Data_.AcessarDados()

@Register_Dados.route("/databaselocal/dados/<data>")
def datalocal(data):
    return Data_.DadosLocais(data)