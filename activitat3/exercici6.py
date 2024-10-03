areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]
print(areas_pis[1])
print(areas_pis[-1])
print(areas_pis[areas_pis.index("Terrassa")+1])
print(areas_pis[1:4])
print(areas_pis[3:])
print("Suma areas: "+str(areas_pis[5]+areas_pis[13]))
areas_pis[9]=30
print(areas_pis)
areas_pis.append("Patin interior")
areas_pis.append(2.78)
print(areas_pis)
sumaAreas=0
for x in areas_pis:
    if isinstance(x,(int,float)):
        sumaAreas+=x
print(sumaAreas)
print(6%3)

