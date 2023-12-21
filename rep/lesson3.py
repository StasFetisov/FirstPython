import mysql.connector

try:
    sql_connection = mysql.connector.connect(
    user='firstpython0612', password = 'qaz159okm',
    host = 'db4free.net', database = 'firstpython0612')
except Exception as err:
    print (err1)

try:
    sql_connection = mysql.connector.connect(
        user='firstpython0612', password='qaz159okm',
        host='db4free.net', database='firstpython0612')
    query_str = 'select name2, number2 from first_table'
    sql_cursor = sql_connection.cursor()
    sql_cursor.execute(query_str)
except Exception as err:
    print(err2)
    #for (name1,number2) in sql_cursor:
   #print (f'number:{number2} name:{name1}')


finally: sql_connection.close()

sql_connection = mysql.connector.connect (
user = 'firstpython0612', password = 'qaz159okm',
host = 'db4free.net', database = 'firstpython0612')

query_str = 'select name2, number2 from first_table'
sql_cursor = sql_connection.cursor()
sql_cursor.execute(query_str)

for (name2,number2) in sql_cursor:
#    print (f'number:{number2} name:{name2}')
    print (f'{number2} {name2}')


sql_connection.close()

