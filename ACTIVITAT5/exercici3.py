import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import MultipleLocator

# MOSTRA clockSpeed dels IDs
def clockSpeed():
    id =  [3,13,34,56,70,85,110,120,210,400]
    # Extreure dades de l'arxiu
    arxiu= pd.read_csv("ACTIVITAT5/arxius/test.csv")
    #Filtrar les dades segons el IDs que volem
    dades = arxiu[arxiu['id'].isin(id)][["id","clock_speed"]]
    return(dades)

# MOSTRA pxWidth dels IDs
def megapixels():
    id =  [3,13,34,56,70,85,110,120,210,400]
    # Extreure dades de l'arxiu
    arxiu= pd.read_csv("ACTIVITAT5/arxius/test.csv")
    #Filtrar les dades segons el IDs que volem
    dades = arxiu[arxiu['id'].isin(id)][["id","px_width"]]
    return(dades)

# MOSTRA battery dels IDs
def batteryPower():
    id =  [3,13,34,56,70,85,110,120,210,400]
    # Extreure dades de l'arxiu
    arxiu= pd.read_csv("ACTIVITAT5/arxius/test.csv")
    #Filtrar les dades segons el IDs que volem
    dades = arxiu[arxiu['id'].isin(id)][["id","battery_power"]]
    return(dades)
    
def main():

    # Mostrar per pantalla
    print(clockSpeed())
    print(megapixels())
    print(batteryPower())
    
    # GRAFICS
    id =  [3,13,34,56,70,85,110,120,210,400]

    # Crear la finestra on insertarem els gràfics
    window = plt.figure(figsize=(12,10))

    # Afegir els gràfics
    graf1 = window.add_subplot(2,2,1)
    graf2 = window.add_subplot(2,2,2)
    graf3 = window.add_subplot(2,2,3)

        # GRAFIC 1

    # Fer el gràfic de barres amb les dades corresponents i ajustant l'amplada de les barres
    graf1.bar(clockSpeed()["id"],clockSpeed()["clock_speed"],width=7)
    graf1.set_title("Gràfic 1")
    # Canviar l'eix y perque sigui més precís, la frecuencia de ticks
    graf1.yaxis.set_major_locator(MultipleLocator(0.5))
    graf1.yaxis.set_minor_locator(MultipleLocator(0.1))
    # Títols Eixos
    graf1.set_xlabel("IDs")
    graf1.set_ylabel("Clock Speed")
    # Nomes IDs al eix X
    graf1.set_xticks(id)
    # Fer el tamany més petit
    graf1.set_xticklabels(id,fontsize=8)
    # Girar els nums de l'eix x per a que no es sobreposin
    graf1.tick_params(axis='x', rotation=70)

        # GRÀFIC 2
   
       # Fer el gràfic de barres amb les dades corresponents i ajustant l'amplada de les barres
    graf2.bar(megapixels()["id"],megapixels()["px_width"],width=7)
    graf2.set_title("Gràfic 2")
    # Canviar l'eix y perque sigui més precís, la frecuencia de ticks
    graf2.yaxis.set_major_locator(MultipleLocator(500))
    graf2.yaxis.set_minor_locator(MultipleLocator(100))
    # Títols Eixos
    graf2.set_xlabel("IDs")
    graf2.set_ylabel("PX Width")
    # Nomes IDs al eix X
    graf2.set_xticks(id)
    # Fer el tamany més petit
    graf2.set_xticklabels(id,fontsize=8)
    # Girar els nums de l'eix x per a que no es sobreposin
    graf2.tick_params(axis='x', rotation=70)

        # GRÀFIC 3

    # Fer el gràfic de barres amb les dades corresponents i ajustant l'amplada de les barres
    graf3.bar(batteryPower()["id"],batteryPower()["battery_power"],width=7)
    graf3.set_title("Gràfic 3")
    # Canviar l'eix y perque sigui més precís, la frecuencia de ticks
    graf3.yaxis.set_major_locator(MultipleLocator(500))
    graf3.yaxis.set_minor_locator(MultipleLocator(100))
    # Títols Eixos
    graf3.set_xlabel("IDs")
    graf3.set_ylabel("Battery Power")
    # Nomes IDs al eix X
    graf3.set_xticks(id)
    # Fer el tamany més petit
    graf3.set_xticklabels(id,fontsize=8)
    # Girar els nums de l'eix x per a que no es sobreposin
    graf3.tick_params(axis='x', rotation=70)

    # Ajustar separació de gràfics
    plt.tight_layout()
    # Mostrar gràfic
    plt.show()



    