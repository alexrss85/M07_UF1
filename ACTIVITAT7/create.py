import psycopg2 as psy

def afegir(conn,connection):
    try:
        sql = '''INSERT INTO personajes VALUES (1,'Akali', 'Ionia', 'Energía', 'Humana', 'Melee', 'Mid'),
    (2,'Katarina', 'Noxus', 'Sin Mana', 'Humana', 'Melee', 'Mid'),
    (3,'Yasuo', 'Jonia', 'Sin Mana', 'Humano', 'Melee', 'Mid'),
    (4,'Yone', 'Jonia', 'Sin Mana', 'Humano', 'Melee', 'Mid'),
    (5,'Galio', 'Demacia', 'Mana', 'Coloso', 'Melee', 'Mid'),
    (6,'KaiSa', 'Shurima', 'Mana', 'Humana', 'Rango', 'ADC');'''
        connection.execute(sql)
        conn.commit()
        print("Valors afegits a la taula Personajes")
 
    except (Exception, psy.Error) as error:
        print("Error", error)

