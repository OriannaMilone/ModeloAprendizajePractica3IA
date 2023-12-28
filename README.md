# ModeloAprendizajePractica3IA
Práctica 3. Inteligencia Artificial. Desarrollo de un pequeño modelo de aprendizaje. 

## Objetivo
El objetivo de esta práctica es desarrollar un pequeño modelo de aprendizaje con datos reales. Para ello se utilizará un dataset de accidentes de tráfico en UK en el año 2016. El modelo de aprendizaje será un modelo de regresión logística.
La regresión logística es una elección convincente para abordar el problema de predecir la severidad de los accidentes automovilísticos basándose en diversas características. Su capacidad para manejar variables categóricas, la interpretación sencilla de los coeficientes que indican la influencia relativa de cada característica, y la modelización de probabilidades, hacen que este enfoque sea especialmente apto. Además, la regresión logística es robusta a ciertas violaciones de supuestos, eficiente computacionalmente y está ampliamente implementada en bibliotecas de aprendizaje automático como scikit-learn. 

## Pasos seguidos
1) Obtención de los datos 
- Los datos se obtuvieron de la página web de [Kaggle](https://www.kaggle.com/datasets/bluehorseshoe/uk-2016-road-safety-data/data) - UK 2016 Road Safety Data
- Se descargaron los datos en formato CSV y se guardaron en la carpeta `data` del proyecto
- Se creó un fichero `data.py` para leer los datos y convertirlos en un dataframe de Pandas

2) Preprocesamiento de los datos
- Inicialmente se eliminaron las columnas que no se iban a utilizar
- Se eliminaron las filas que tenían valores nulos
- Se crea un data frame con la mitad de las filas del data frame original para usarlo como datos de entrenamiento

3) Creación del modelo
- Se crea un modelo de regresión logistica con los datos de entrenamiento. Usando la librería de scikit-learn
- "La regresión logística es un modelo de clasificación que predice la probabilidad de pertenencia a una categoría. Es eficiente, interpretable y adecuado para problemas con variables categóricas."

4) Entrenamiento del modelo

5) Predicción con el modelo
- Se evalua la precisión del modelo con los datos de entrenamiento y las predicciones

## Resultados
- Se obtiene una precisión del 83% con los datos de entrenamiento