from repository.DataAnalitc_Repository import DataAnalitic

class DataAnaliticService():
    def __init__(self) -> None:
        self.__DataAnalitic = DataAnalitic()
        
    def AcessarDadosBrutos(self,database):
        return self.__DataAnalitic.AcessarBanco(database)
    def teste(self):
        return {"object":"iooi"}
    