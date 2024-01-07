# ModeloAprendizajePractica3IA
Práctica 3. Inteligencia Artificial. Desarrollo de un pequeño modelo de aprendizaje. 
Consultar al final para la ejecución 

## Objetivo
El objetivo de esta práctica es desarrollar un pequeño modelo de aprendizaje con datos reales. Para ello se utilizará un dataset de accidentes de tráfico en UK en el año 2016. El modelo de aprendizaje será un modelo de regresión logística.
La regresión logística es una elección convincente para abordar el problema de predecir la severidad de los accidentes automovilísticos basándose en diversas características. Su capacidad para manejar variables categóricas, la interpretación sencilla de los coeficientes que indican la influencia relativa de cada característica, y la modelización de probabilidades, hacen que este enfoque sea especialmente apto. Además, la regresión logística es robusta a ciertas violaciones de supuestos, eficiente computacionalmente y está ampliamente implementada en bibliotecas de aprendizaje automático como scikit-learn. 

## Pasos seguidos
1) Obtención de los datos 
- Los datos se obtuvieron de la página web de [Kaggle](https://www.kaggle.com/datasets/bluehorseshoe/uk-2016-road-safety-data/data) - UK 2016 Road Safety Data
- Se descargaron los datos en formato CSV y se guardaron en la carpeta `data` del proyecto
- Se creó un fichero `data.py` para leer los datos y convertirlos en un dataframe de Pandas

2) Preprocesamiento de los datos
- Inicialmente se eliminaron las columnas que no se iban a utilizar. Para mirar con más detalle las columnas eliminadas se recomienda mirar la linea 23 del archivo 'data.py' dentro de la función df_limpio(), que se encarga de gestionar los cambios. Se ha decidido eliminar dichas columnas ya que tendían a sesgar los resultados... Por ejemplo, en muchos escenarios la patrulla 4 asistia los accidentes de tráfico, simultaneamente los casos que asistía la pratulla tenían todos un rango de severidad similar, el modelo tendía a 'pensar' que si la pratulla 4 asistía después del accidente la severidad sería 'X' siempre, lo cual sabemos que es falso. Este es un escenario que se repitió para varias columnas, otras fueron eliminadas por criterio personal, se evaluó qué elementos podrían tener más o menos influencia en los accidentes de tráfico y se trabajó con ello. 
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

## Intrucciones para ejecutar 
1) Será necesario contar con un entorno de desarrollo y con la version: Python 3.9.13
2) Será necesario descargar todos los archivos incluyendo en excel que contiene los datos para su estudio
3) IMPORTANTE: Será necesario cambiar la ruta local en el archivo 'data.py' linea 6.
- Ejemplo: ruta_local = 'C:/  * introduce la ruta de este proyecto en tu ordenador *     /ModeloAprendizajePractica3IA/RoadSafetyAccidents.csv'
4) Finalmente, el proyecto se debe ejecutar desde el archivo '__init__.py' 
5) A partir de ahí la ejecución será guiada e intuitiva

## Modelos consultados además de la Regresión Logística 
1) Modelo/Algoritmo de Árbol de Decisión --> Se desempeñó con un 80% de exactitud (un 2% menos que el modelo seleccionado)
- Si desea probar el modelo, deberá ir al codigo contenido en el archivo 'modelo.py' y descomentar las lineas (7, 30, 38, 45, 75)

2) Modelo/Algoritmo Ramdon Forest --> Se desempeñó con un 81% de exactitud (un 1% menos que el modelo seleccionado)
- Si desea probar el modelo, deberá ir al codigo contenido en el archivo 'modelo.py' y descomentar las lineas (8, 33, 40, 46, 76)