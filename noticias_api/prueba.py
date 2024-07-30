import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=192.168.0.3;'
    'DATABASE=master;'
    'UID=sa;'
    'PWD=Nacion1846;'
)

cursor = conn.cursor()
cursor.execute('SELECT 1+500+1000')
row = cursor.fetchone()
print(row)
