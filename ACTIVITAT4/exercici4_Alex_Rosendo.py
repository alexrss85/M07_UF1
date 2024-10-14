def ex4Alex():

    import numpy as np

    # Matriu aleatoria 1-80
    matriu = np.random.randint(0,81, size=(3, 4))
    print("\nMATRIU 1: \n")
    print(matriu)

    # Ultima fila a ultima columna


        # Guardar ultima fila, esborrar-la i afegirla com columna
    ultColuma=matriu[:,-1]
    matriu = np.delete(matriu,3,axis=1)
    matriu = np.insert(matriu, matriu.shape[0], ultColuma, axis=0)
    print("\nMATRIU 2: \n")
    print(matriu)

    # Ultima columna nums iguals

        # Guardar primer num de l'ultima columna
    num=matriu[[0],[2]]

        # Substituir els nums de l'ultima columna
    matriu[[1],[2]]=num
    matriu[[2],[2]]=num
    matriu[[3],[2]]=num
    print("\nMATRIU 3: \n")
    print(matriu)
ex4Alex()


