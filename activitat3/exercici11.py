monedes  = {'Dólar nord-americà': '$', 'Euro': '€', 'Lliura esterlina': '£', 'Ien japonès': '¥', 'Iuan xinès': '¥', 
            'Dólar australian': 'A$', 'Dólar canadenc': 'C$', 'Franc suís': 'CHF', 'Pesos mexicà': 'MX$', 
            'Real brasiler': 'R$', 'Rupi índia': '₹', 'Rublo rus': '₽', 'Rand sud-africà': 'R', 'Won sud-coreà': '₩', 'Pesos argentí': 'AR$'}
moneda= input("Escriu el nom d'una moneda en català: ")
if moneda in monedes:
    print("Símbol de la moneda: "+ monedes[moneda])
else:
    print("Aquesta moneda no està al diccionari.")