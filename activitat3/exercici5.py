frase=input("Escriu una frase: ")
fraseSenseRep=""
for x in frase:
    if x==" ":
        fraseSenseRep+=x
    if x not in fraseSenseRep:
        fraseSenseRep+=x 
frase=frase.replace(" ","")
tupla=tuple(frase)
print(tupla)  
print(fraseSenseRep)
