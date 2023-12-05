class Obj1():
    def __init__(self) -> None:
        self.lista_obj = []
    @staticmethod
    def Obj_repetir(obj):
        print("a")
    @staticmethod
    def criar_obj(obj):
        print("aa")
    @staticmethod
    def Editar_obj(obj):
        print("aaa")
    
Param = ""
AcoesString = {"Repetir":Obj1.criar_obj,"Criar":Obj1.criar_obj,"Editar":Obj1.Editar_obj}
input_action = input("acao :")
try:
    AcoesString[str(input_action)](Param)
    print()
except:
    print("Não existe")
