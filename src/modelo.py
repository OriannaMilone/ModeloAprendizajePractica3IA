import data
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def modelo_predictivo_regresion_lineal(): 
    df_subset = data.df_entrenamiento(data.df_limpio())

    # Separar las características (X) y la variable objetivo (Accident_Severity: y)
    X = df_subset.drop('Accident_Severity', axis=1)
    y = df_subset['Accident_Severity']

    #Dividimos los datos en datos de entrenamiento y datos de prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Normalizar las características
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    #Modelo de Regresión Logística
    modelo_logistico = LogisticRegression(random_state=42)

    #Entrenando el modelo
    modelo_logistico.fit(X_train, y_train)

    #Realizar predicciones en el conjunto de prueba
    y_pred = modelo_logistico.predict(X_test)

    #Evaluar el rendimiento del modelo
    accuracy = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)
    classification_rep = classification_report(y_test, y_pred)

  
    print(f'Exactitud (Accuracy): {accuracy:.4f}')
    print('\nMatriz de Confusión:')
    print(conf_matrix)
    print('\nReporte de Clasificación:')
    print(classification_rep)
    
    return 'Para consultar el paso a paso del modelo, consultar el Readme.md ...'