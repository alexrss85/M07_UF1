import psycopg2 as psy


def llegir(conn,connection):
    try:
        sql = '''SELECT * FROM personajes'''
        connection.execute(sql)
        print("Dades de la taula Personajes: \n")
        # Llegir i imprimir els registres
        for x in connection:  # Usar fetchall per obtenir tots els resultats
            print(x)
    except (Exception, psy.Error) as error:
        print("Error", error)

        



