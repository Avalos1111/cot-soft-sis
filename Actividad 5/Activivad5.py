import sqlite3
from DataBaseManager import DataBaseManager

dataBaseManager = DataBaseManager()


con = sqlite3.connect(dataBaseManager.database)
materia = (11,'ingles', 'Avalos Marquez Eishel Alexandra', 7)
dataBaseManager.create_materia(con, materia)
cur = con.cursor()
cur.execute("Select * from Materias;")
table_list = cur.fetchall()
for row in table_list:
    print(row)
con.close()