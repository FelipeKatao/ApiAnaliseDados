import pymysql

class DataAnalitic():
    def __init__(self) -> None:
        self.con = pymysql.connect(host="",user="",passwd="",database="")
    def AcessarBanco(self,NomeTabela):
        sql = f"""
          SELECT * FROM {NomeTabela} 
          """
        try:
            cursor = self.con.cursor()
            cursor.execute(sql)
            result = cursor.fetchone()
            return result
        except:
            return "Ocorreu um erro no processamento"
        