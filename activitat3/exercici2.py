mesos = ("Gener","Febrer","Març","Abril","Maig","Juny","Juliol","Agost","Setembre","Octubre","Novembre","Desembre")
num= int(input("Escriu un número entre 1 i 12: "))
while num!=0:
    print(mesos[num-1])
    num= int(input("Escriu un número entre 1 i 12: "))
