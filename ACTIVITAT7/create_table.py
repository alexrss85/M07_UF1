import psycopg2 as psy   

def crearTaula(conn,connection):
    try:
        sql = '''CREATE TABLE personajes (
    id int primary key,
    nombre VARCHAR(20) ,
    region VARCHAR(20),
    posicion VARCHAR(20),
    recurso VARCHAR(20),           
    raza VARCHAR(20),
    tipo_ataque VARCHAR(20)              
);'''

        connection.execute(sql)
        conn.commit()
        print("Taula Personajes creada")

    except (Exception, psy.Error) as error:
        print("Error",error)




