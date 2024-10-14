def ex4Albert():

    import numpy as np

    # Matriu random que va de 1 al 80
    matriu = np.random.randint(0,81, size=(3, 4))
    print("1) Matriu aleatoria:")
    print(matriu)

    # Ultima fila a ultima columna
    # Guardem l'última fila, després l'esborrarem i l'afegim com a columna
    uColuma = matriu[:,-1]
    matriu = np.delete(matriu,3,axis=1)
    matriu = np.insert(matriu, matriu.shape[0], uColuma, axis=0)
    print("\n2) Matriu modificada:")
    print(matriu)

    # Ultima columna nums iguals

        # Guardar primer num de l'ultima columna
    num=matriu[[0],[2]]

        # Substituir els nums de l'ultima columna
    matriu[[1],[2]]=num
    matriu[[2],[2]]=num
    matriu[[3],[2]]=num
    print("\n3) Matriu amb els mateixos números:")
    print(matriu)
ex4Albert()
