import pandas as pd
import matplotlib.pyplot as plt

def llegir_dades_csv(nom_fitxer):
    df = pd.read_csv(nom_fitxer, usecols=['City', 'Population', 'Density (/km²)', 'Density (/mi²)'])
    return df

def limpiar_population(population):
    num = ''
    for char in population:
        if char.isdigit() or char == ',':
            num += char
        else:
            break 
    return float(num.replace(',', ''))

# Funció 1: Total de població per ciutat
def mostrar_poblacio_per_ciutat(df):
    print("Població per ciutat:")
    print(df[["City", "Population"]])

# Funció 2: Densitat per KM2
def mostrar_densitat_per_km2(df):
    print("\nDensitat per km²:")
    print(df[["City", "Density (/km²)"]])
    
# Funció 3: Densitat per M2
def mostrar_densitat_per_m2(df):
    print("\nDensitat per mi²:")
    print(df[["City", "Density (/mi²)"]])  

def main():
    # Leer datos del csv
    nom_fitxer = "ACTIVITAT5/arxius/ciutats.csv"
    df = llegir_dades_csv(nom_fitxer)

    df['Population'] = df['Population'].apply(limpiar_population)

    # Llamado a les funcions
    mostrar_poblacio_per_ciutat(df)
    mostrar_densitat_per_km2(df)
    mostrar_densitat_per_m2(df)

    # Gràfica circular per població
    plt.pie(df['Population'], labels=df['City'], autopct="%0.1f%%")
    plt.axis("equal")  
    plt.show()

    # Gràfica circular per densitat KM2
    plt.pie(df['Density (/km²)'], labels=df['City'], autopct="%0.1f%%")
    plt.axis("equal")  
    plt.show()
 
    # Gràfica circular per densitat M2
    plt.pie(df['Density (/mi²)'], labels=df['City'], autopct="%0.1f%%")
    plt.axis("equal")  
    plt.show()

main()
