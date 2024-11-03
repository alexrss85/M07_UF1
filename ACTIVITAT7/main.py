from connection import conexio
from create_table import crearTaula
from create import afegir
from update import actualitzar
from delete import borrar
from read import llegir


conn, connection = conexio()
    
try:
    print("INICI")
    crearTaula(conn, connection)
    afegir(conn, connection)
    actualitzar(conn, connection)
    borrar(conn, connection)
    llegir(conn, connection)

except Exception as error:
    print("Error", error)
finally:
    conn.close()
