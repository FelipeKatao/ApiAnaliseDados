
class DataControl():
    def __init__(self) -> None:
        pass
    def AcessarDados(self):
        return {"Dado":[2,4,6,4,6,67,4,4,43],
            "Titulo":"Analise de dados X"}
    def DadosLocais(self,LocalData):
        return {"Dado":{LocalData},
            "Titulo":"Analise de dados X"}