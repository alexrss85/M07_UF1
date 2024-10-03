paraula1=(input("Escriu la primera paraula: "))
paraula2=(input("Escriu la segona paraula: "))
primeraLletra1=paraula1[0]
segonaLletra1=paraula1[1]
primeraLletra2=paraula2[0]
segonaLletra2=paraula2[1]
paraula1=paraula1.replace(primeraLletra1,primeraLletra2)
paraula2=paraula2.replace(primeraLletra2,primeraLletra1)
paraula1=paraula1.replace(segonaLletra1,segonaLletra2)
paraula2=paraula2.replace(segonaLletra2,segonaLletra1)
print(paraula1,paraula2)
