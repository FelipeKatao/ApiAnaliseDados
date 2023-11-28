import pymysql

class AcessarBancoDados():
    def __init__(self) -> None:
        self.con = pymysql.connect(host="",user="",database="",password="")

    def OpenCon(self):
         self.con = pymysql.connect(host="",user="",database="",password="")
    def ConsultarBancoDados(self):
        Cursor = self.con.cursor()
        Sql ="""
        XA START 'Aluno_inserido';
        SELECT * FROM Alunos ;
        XA END 'Aluno_inserido';
        XA PREPARE 'Aluno_inserido';
        XA COMMIT 'Aluno_inserido'
        """
        Cursor.execute(Sql)
        return Cursor.fetchall()