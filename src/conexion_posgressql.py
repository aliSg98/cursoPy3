import psycopg2

#conexion a base de datos
try:
    conexion = psycopg2.connect(
        host = 'localhost',
        port = '5432',
        user = 'postgres',
        password = 'admin',
        database = 'mydatabase'
        
    )
    print("Conexion correcta")
    #utilizar cursor
    cursor= conexion.cursor()
    #crear sentencia sql
    sql = 'SELECT * FROM robots'

    cursor.execute(sql)

    #mostrar resultado
    registro = cursor.fetchall()
    print(registro)

    #cerrar conexion
    cursor.close()
    conexion.close()


except Exception as exception:
    print(exception)