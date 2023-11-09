import pymysql

connection = pymysql.connect(host="db4free.net",
                             user="datauser_ds",
                             password="datauser23",
                             database="datascience")

cursor = connection.cursor()
sql= "INSERT INTO AnaliseDados VALUES(0,'dados',0,'Unico')"
cursor.execute(sql)
connection.commit()

sql = "SELECT * FROM AnaliseDados"
cursor.execute(sql)
result = cursor.fetchone()
print(result)