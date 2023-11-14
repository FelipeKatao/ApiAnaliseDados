import pymysql

class DataAnalitic():
    def __init__(self) -> None:
        self.con = pymysql.connect(host="127.0.0.1",user="root",passwd="alunolab",database="folhadepagamento")
        
    def AtualizarBanco(self):
        self.con.close()
        self.con = pymysql.connect(host="127.0.0.1",user="root",passwd="alunolab",database="folhadepagamento")
        
    def AcessarBanco(self,NomeTabela):
            
        self.AtualizarBanco()         
        sql = f"""
          SELECT * FROM {NomeTabela} 
          """
        try:
            cursor = self.con.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            return list(result)
        except  Exception as e :
            return "Ocorreu um erro no processamento "+str(e)
        