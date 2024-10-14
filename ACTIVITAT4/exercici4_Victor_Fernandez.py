import numpy as np

def ex4Victor():
    # Matriu 3x4 de números aleatoris de 0 a 80
    matriu = np.random.randint(0, 81, size=(3, 4))
    print("Matriu 3x4: ")
    print(matriu)

    ultColumna=matriu[:,-1]
    matriu = np.delete(matriu,3,axis=1)
    matriu = np.insert(matriu, matriu.shape[0], ultColumna, axis=0)
    print("\nMATRIU 2:")
    print(matriu)

    # Guardar primer número de la última columna
    num=matriu[[0],[2]]

    # Substituir els nums de la última columna
    matriu[[1],[2]]=num
    matriu[[2],[2]]=num
    matriu[[3],[2]]=num
    print("\nMATRIU 3:")
    print(matriu)

ex4Victor()
