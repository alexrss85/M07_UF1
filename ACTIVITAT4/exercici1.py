# (A)Trucar a l’exercici 1 i mostrar per pantalla:


# Diferents apartat que he de fer:
    # 1) La matriu com la de la imatge de l’exercici 1
    # 2) La dimensió de la matriu
    # 3) El tamany de la matriu
    # 4) Número total d’elements
    # 5) Tipus d’elements interns
    # 6) Cada punt ha de vindre acompanyat d’un text on quedi clar què s’està mostrant per pantalla.

# 1) Crear matriu com la imatge (números ascendent en diagonal del 0 al 49)
import numpy as np

# Creo un primer array per poder guardar els valors del 0 al 49 (sense diagonal)
ndarray = np.arange(0, 50, 1)

# Cambia el format de la direcció de la matriu
array = np.diag(ndarray)
print(array)

# 2) La dimensió de la matriu
print("Dimensió de la matriu: " + str(array.ndim))

# 3) El tamany de la matriu
# files = len(array)
# resultat  = files * columnes

print("El tamany de la matriu: " + str(array.shape))

# 4) Número total d’elements
print("El número total d'elements és: " + str(array.size))

# 5) Tipus d’elements interns
print("Tipus de tipus dels elements de la matriu: " + str(array.dtype))