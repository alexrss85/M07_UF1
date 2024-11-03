import psycopg2 as psy

def actualitzar(conn,connection):
    try:
        sql = """update personajes set raza='humano' where nombre='Galio'"""
        connection.execute(sql)
        conn.commit()

    except (Exception, psy.Error) as error:
        print("Error", error)

