from flask import jsonify
from pathlib import Path
import json

class Controler_dadosBrutos():
    def __init__(self) -> None:
        pass

    def ListagemDados(self):
        path = str(Path('Data'))
        with open(path+"\data.json",'r') as arquivo:
            dados = json.load(arquivo)
        return jsonify(dados)
    
    def BaseDados(self):
        return "all data"
    
    def Teste(self):
        print("Executando em segundo plano")

    