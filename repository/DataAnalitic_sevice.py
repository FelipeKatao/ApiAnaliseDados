from DataAnalitc_Repository import DataAnalitic

class DataAnaliticService():
    def __init__(self) -> None:
        self.__DataAnalitic = DataAnalitic()
        
    def AcessarTabelaDadosFrios(self):
        return self.__DataAnalitic.AcessarBanco("DadosFrios")
    