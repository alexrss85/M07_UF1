
paraules=(input("Escriu de una a tres paraules separades per espai: "))
paraules=paraules.split()
if len(paraules)<=3:
    for e in paraules:
        print ("Paraula: "+e+"| Num de caracters: "+str(len(e)),"| Primer caràcter: "+str(e[0]),"| Últim caràcter: "+str(e[len(e)-1]))
else:
    print("Escriu menys paraules.")

  
