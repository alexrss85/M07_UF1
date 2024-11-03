import psycopg2 as psy


def borrar(conn,connection):
    try:
        inp=int(input("ID del personatge que vols esborrar?"))
        sql = '''delete from personajes where id ='''+str(inp)
        connection.execute(sql)
        conn.commit()
        print("El personatge amb id: "+str(inp)+" s'ha esborrat.\n")
    except (Exception, psy.Error) as error:
        print("Error", error)

