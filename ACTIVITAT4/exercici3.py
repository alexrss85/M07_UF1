import numpy as np
# Matriu de nums aleatoris de l'1 al 100
def matriuNumsAleatoris():
    fil = int(input("Escriu el num de files: "))
    col = int(input("Escriu el num de files: "))
    matriu = np.random.randint(0,101, size=(fil, col))
    return(matriu)


# Num més alt d'una matriu
def maximMatriu(matriu):
    print("El màxim es : "+str(np.max(matriu)))

# Mínim d'una matriu
def minimMatriu(matriu):
    print("El mínim es : "+str(np.min(matriu)))


