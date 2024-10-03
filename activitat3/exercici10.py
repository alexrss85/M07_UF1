abecedari= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
abecedariNou=[]
for x in abecedari:
    if abecedari.index(x)%3!=0:
        abecedariNou.append(x)
tupla=tuple(abecedariNou)
print(tupla)

