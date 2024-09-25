valor = int(input("Valor en euros: "))
iva = int(input("4%,10%,21% IVA?"))

while(iva not in (4,10,21)):
    iva = int(input("4%,10%,20% d'IVA?"))

resIVA = (valor*iva)/100
res = valor+resIVA
print("VALOR: "+ str(valor)+" euros.  % IVA: "+str(iva)+"%. VALOR FINAL: "+str(res)+" euros.")
