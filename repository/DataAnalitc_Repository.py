import pymysql

class DataAnalitic():
    def __init__(self) -> None:
        self.con = pymysql.connect(host="bd4free.net",user="datauser_ds",passwd="Datauser23",database="datascience")
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
        