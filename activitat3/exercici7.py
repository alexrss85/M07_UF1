contactes={"Alex": 21, "Anna": 25, "Carles": 35, "Lucia": 23, "Arnau": 32}
inp=input("Escriu el contacte que vols afegir amb aquest format--> nom edat: ")
contacteNou=inp.split()
while inp!="No vull afegir més":
    if contacteNou[0] in contactes:
        print("Ja existeix")
        inp=input("Escriu el contacte que vols afegir amb aquest format--> nom edat: ")
        contacteNou=inp.split()
    else:
        contactes[contacteNou[0]]=int(contacteNou[1])
        inp=input("Escriu el contacte que vols afegir amb aquest format--> nom edat: ")
        contacteNou=inp.split()
print(contactes)




