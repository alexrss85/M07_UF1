import pandas as pd
import matplotlib.pyplot as plt

# Llegir el csv
df = pd.read_csv("ACTIVITAT5/arxius/covid.csv")

# Funció per mostrar la quantitat total de casos per mes i país (10 països i 4 mesos)
def mostrarCasosTotals():
    df['date'] = pd.to_datetime(df['date'])                                         # Convertim la columna 'date' al format de data
    paisos = df['location'].unique()                                                # Obtenim una llista de països únics
    paisos_aleatoris = pd.Series(paisos).sample(10, random_state=42).tolist()       # Seleccionem 10 països aleatoris
    df['mes'] = df['date'].dt.to_period('M')                                        # Afegim una columna 'mes' per agrupar per mesos

    # Filtrant pels mesos que ens interessen
    mesos = ['2020-03', '2020-04', '2020-05', '2020-06']                            
    df_filtrat = df[(df['location'].isin(paisos_aleatoris)) & (df['mes'].astype(str).isin(mesos))]
    
    # Agrupem i sumem els casos totals
    df_agrupat = df_filtrat.groupby(['location', 'mes'])['total_cases'].sum().reset_index()
    
    print("\nTotal de casos per mes per país:")
    print(df_agrupat)                                                               
    return df_agrupat, paisos_aleatoris                                             # Retornem el DataFrame agrupat i la llista de països

# Funció per mostrar les morts totals per mes i país (10 països i 4 mesos) del 2021
def mostrarMortsTotals():
    df['date'] = pd.to_datetime(df['date'])                                             
    paisos = df['location'].unique()                                                # Obtenim una llista de països únics
    paisos_aleatoris = pd.Series(paisos).sample(10, random_state=42).tolist()       # Seleccionem 10 països aleatoris
    df['mes'] = df['date'].dt.to_period('M')                                        # Afegim una columna 'mes' per agrupar per mesos

    # Filtrant pels mesos de 2021
    mesos = ['2021-01', '2021-02', '2021-03', '2021-04']    
    df_filtrat = df[(df['location'].isin(paisos_aleatoris)) & (df['mes'].astype(str).isin(mesos))]
    
    # Agrupem i sumem les morts totals
    df_agrupat = df_filtrat.groupby(['location', 'mes'])['total_deaths'].sum().reset_index()
    
    print("\nTotal de morts per mes per país (2021):")
    print(df_agrupat)
    return df_agrupat, paisos_aleatoris

# Funció per mostrar la “reproduction_rate” per mes i país (10 països i 4 mesos)
def mostrarTaxaReproduccio():
    df['date'] = pd.to_datetime(df['date']) 
    paisos = df['location'].unique()                                                
    paisos_aleatoris = pd.Series(paisos).sample(10, random_state=42).tolist()       
    df['mes'] = df['date'].dt.to_period('M')

    mesos = ['2020-03', '2020-04', '2020-05', '2020-06']    
    df_filtrat = df[(df['location'].isin(paisos_aleatoris)) & (df['mes'].astype(str).isin(mesos))]
    
    # Agrupem i calculem la mitjana de la taxa de reproducció
    df_agrupat = df_filtrat.groupby(['location', 'mes'])['reproduction_rate'].mean().reset_index()
    
    print("\nTaxa de reproducció per mes per país:")
    print(df_agrupat)   
    return df_agrupat, paisos_aleatoris     

# Funció principal per executar les altres funcions i mostrar les gràfiques
def main():
    casos_df, paisos_1 = mostrarCasosTotals()  
    morts_df, paisos_2 = mostrarMortsTotals()  
    taxa_df, paisos_3 = mostrarTaxaReproduccio()
    
    # Creem gràfiques
    plt.figure(figsize=(15, 15))

    # Gràfica de casos totals
    plt.subplot(3, 1, 1)
    for pais in paisos_1:
        subset = casos_df[casos_df['location'] == pais]  
        plt.plot(subset['mes'].astype(str), subset['total_cases'], marker='o', label=pais)  
    
    plt.title('Total de casos per mes')     # Títol de la gràfica
    plt.xlabel('Mes')                       # Etiqueta l'eix X
    plt.ylabel('Total de casos')            # Etiqueta l'eix Y
    plt.xticks(rotation=45)                 # Rotem les etiquetes de l'eix X
    plt.legend()                            # Mostrem la llegenda

    # Gràfica de morts totals
    plt.subplot(3, 1, 2)
    for pais in paisos_2:
        subset = morts_df[morts_df['location'] == pais]  
        plt.plot(subset['mes'].astype(str), subset['total_deaths'], marker='o', label=pais) 
    plt.title('Total de morts per mes (2021)')  # Títol
    plt.xlabel('Mes')                       # Etiqueta de l'eix X
    plt.ylabel('Total de morts')            # Etiqueta de l'eix Y
    plt.xticks(rotation=45)                 # Rotem les etiquetes de l'eix X
    plt.legend()                            # Mostrem la llegenda

    # Gràfica de taxa de reproducció
    plt.subplot(3, 1, 3)
    for pais in paisos_3:
        subset = taxa_df[taxa_df['location'] == pais]  # Filtra la taxa de reproducció per país
        plt.plot(subset['mes'].astype(str), subset['reproduction_rate'], marker='o', label=pais)
        plt.title('Taxa de reproducció per mes')
        plt.xlabel('Mes')                        
        plt.ylabel('Taxa de reproducció')  
        plt.xticks(rotation=45)
        plt.legend()  
        plt.tight_layout()  
        plt.show()  