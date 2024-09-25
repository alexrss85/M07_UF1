numSecret= 22
cont=0
intent= int(input("Escriu un numero de l'1 al 100: "))
while  intent != numSecret:
    if intent>numSecret:
        print("El número és massa gran.")
        intent= int(input("Escriu un numero de l'1 al 100: "))
        cont+=1
    else:
        print("El número és massa petit.")
        intent= int(input("Escriu un numero de l'1 al 100: "))
        cont+=1
if intent==numSecret:
    cont+=1
    print("Has encertat! En "+str(cont)+" intents.")
    