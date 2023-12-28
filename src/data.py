import pandas as pd
import numpy as np

ruta_local = 'C:/Orianna/CEU San Pablo/5Semestre5/IA/ModeloAprendizajePractica3IA/RoadSafetyAccidents.csv'

df = pd.read_csv(ruta_local)

def df_original():
    columnas_originales = []
    for i in df.columns:
        columnas_originales.append(i)
    
    tamaño = df.shape
    print(f'El set de datos original contiene {tamaño[1]} columnas y {tamaño[0]} filas')
    return(f'Las columnas originales son: {columnas_originales}')

def df_limpio():
    df_limpio = df.drop(['Location_Easting_OSGR', 'Time', 'Location_Northing_OSGR', 'Longitude', 'Latitude',
                    'Date', 'Local_Authority_(District)', 'Local_Authority_(Highway)',
                    '1st_Road_Class', '1st_Road_Number', 'Junction_Detail', 'Junction_Control',
                    '2nd_Road_Class', '2nd_Road_Number', 'Pedestrian_Crossing-Human_Control',
                    'Pedestrian_Crossing-Physical_Facilities', 'Special_Conditions_at_Site',
                    'Carriageway_Hazards', 'Did_Police_Officer_Attend_Scene_of_Accident',
                    'LSOA_of_Accident_Location', 'Police_Force' ,'Accident_Index'], axis=1)

    df_limpio = df_limpio.dropna() #Eliminamos las filas con valores nulos
    tamaño = df_limpio.shape
    print(f'El set de datos limpio contiene {tamaño[1]} columnas y {tamaño[0]} filas')
    print(f'Las columnas limpias son: {df_limpio.columns}')
    return df_limpio


def df_entrenamiento(df_limpio):
    df_limpio_mitad = df_limpio.sample(frac=0.5, random_state=42) # Selecciona aleatoriamente la mitad de las filas
    tamaño = df_limpio_mitad.shape
    print(f'El set de datos limpio y reducido contiene {tamaño[1]} columnas y {tamaño[0]} filas')
    print(f'Las columnas limpias y reducidas son: {df_limpio_mitad.columns}')
    return df_limpio_mitad


