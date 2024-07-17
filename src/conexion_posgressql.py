import psycopg2

#conexion a base de datos
def conexion_posgres():
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

        num = int(input("Ingrese 1 para SELECT, 2 para hacer INSERT, 3 para hacer UPDATE, 4 para DELETE: "))
    
        # match case
        match num:
            case num if num == 1:
                #crear sentencia sql
                sql = 'SELECT * FROM robots'
                cursor.execute(sql)
                #mostrar resultado
                registro = cursor.fetchall()
                print(registro)
            case num if num == 2:
                sql = 'INSERT INTO robots(name_robot,status_creation,status_pdf,path_pdf,final_status) values (%s,%s,%s,%s,%s)'
                nombre = input("Ingrese nombre robot: ")
                status = input("Ingrese estado de creacion: ")
                status_pdf = input("Ingrese estado pdf: ")
                path = input('Ingrese path pdf: ')
                final_status = input("Ingrese estado final: ")

                datos = (nombre,status,status_pdf,path,final_status)
                cursor.execute(sql,datos)

                #guardar datos
                conexion.commit()

                #guardar registros
                registro = cursor.rowcount

                print(f'registro insertado: {registro}')
            case num if num == 3:
                sql = 'UPDATE robots SET name_robot=%s, status_creation=%s, status_pdf=%s, path_pdf=%s,final_status=%s WHERE name_robot=%s'  
                name_robot_old = input("Ingrese nombre robot a cambiar: ")
                nombre2 = input("Ingrese nuevo nombre: ")
                status_creation = input("Ingrese estado de creacion: ")
                status_pdf = input("Ingrese estado pdf: ")
                path_pdf = input("Ingrese estado pdf: ")
                final_status = input("Ingrese estado final: ")

                datos = (nombre2,status_creation,status_pdf,path_pdf,final_status,name_robot_old)
                cursor.execute(sql,datos)
                conexion.commit()
                actualizacion = cursor.rowcount
                print(f'Registro actualizado: {actualizacion}')
            case num if num == 4:
                sql = 'DELETE FROM robots WHERE name_robot = %s'
                name_robot = input("Ingrese nombre del robot a eliminar: ")
                cursor.execute(sql,(name_robot,))
                conexion.commit()
                eliminado = cursor.rowcount
                print(f'Registro eliminado: {eliminado}')
            
            case _:
                print("Error")

        #cerrar conexion
        cursor.close()
        conexion.close()


    except Exception as exception:
        print(exception)
