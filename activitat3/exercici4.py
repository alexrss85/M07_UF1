nums=input("Escriu 10 numeros separats per espai:  ")
l=nums.split()
llista=[]
for x in l:
    llista.append(int(x))
tupla=tuple(sorted(llista))
print(tupla)