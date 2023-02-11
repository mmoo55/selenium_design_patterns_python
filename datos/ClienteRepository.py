from datos.ClienteEntity import ClienteEntity
import mysql.connector

class ClienteRepository:

    def guardarCliente(self, cliente: ClienteEntity):

        try:
            mi_conexion = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "Bolivarcampeon2017",
                database = "miframework"
            )

            mi_cursor = mi_conexion.cursor()
            sql_query = "INSERT INTO Cliente(nombres, apellidos) VALUES(%s, %s)"
            val = (cliente.get_nombres(), cliente.get_apellidos())
            mi_cursor.execute(sql_query, val)
            mi_conexion.commit()
            print(mi_cursor.rowcount, "registros insertados")
            mi_cursor.close()

        except mysql.connector.Error as error:
            print("Fallo al insertar un registro en la tabla Cliente {}".format(error))

        finally:
            if mi_conexion.is_connected():
                mi_conexion.close()
                print("MySQL connection esta cerrada")