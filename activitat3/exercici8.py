nums=input("Escriu 10 numeros separats per espai: ")
llista=nums.split()
llistaNums=[]
for x in llista:
    llistaNums.append(int(x))
sumaTotal=0
for x in llistaNums:
    sumaTotal+=x
mitjana=sumaTotal/len(llistaNums)
llistaNums.append(sumaTotal)
llistaNums.append(mitjana)
print("Números de l'usuari: "+ str(llista))
print("Suma Total: "+ str(sumaTotal))
print("Mitjana: "+ str(mitjana))