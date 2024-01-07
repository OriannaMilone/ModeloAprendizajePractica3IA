import modelo

def main():
    print('----------------------------------------------------------------')
    print('Modelo de aprendizaje/predicción basado en regresión logistica')
    print('----------------------------------------------------------------')
    print('El modelo de aprendizaje/predicción basado en regresión logistica predice la severidad de un accidente de tráfico en función de las características del mismo')

    while True: 
        print('----------------------------------------------------------------\n')
        user_input = input('Si desea usar los valores predeterminados para ver las predicciones escriba "0"\nSi desea personalizarlos escriba "1": ')
        if(user_input == '0'):
            print(modelo.realizar_prediccion(2,1,2,20,1,8,2,1))
            
            print('\nEl modelo ha sido entrenado con regresión logística\nLas siguientes son estadísticas con referencia al entrenamiento: ')
            print(modelo.testing_accuracy())
            print('\nPara más información consultar el Readme.md')
            break
        elif(user_input == '1'):
            print('A continuación deberá rellanar 8 caracteristicas necesarias para realizar la predicción entorno a la severidad del accidente de tráfico: \n')
            numeroVehiculos = input('Numero de vehiculos involucrados en el accidente (el valor debe estar comprendido entre [1-4]): ')   
            numeroBajas  = input('Numero de bajas (humanas) en el accidente (el valor debe estar comprendido entre [0-5]): ')   
            diaSemana  = input('Día de la semana en que ocurre el accidente (el valor debe estar comprendido entre [1-7]): ')   
            limiteVelocidad  = input('Limite de velocidad de la vía (el valor debe estar comprendido entre [30-120]): ')   
            condicionVisual = input('Nivel de visibilidad (menor el numero = menor la visibilidad) (el valor debe estar comprendido entre [1-5]): ')   
            condicionClima  = input('Condición climática (menor el numero = mejor la condición = menor el peligro) (el valor debe estar comprendido entre [1-10]): ')   
            condicionVial = input('Condición de la vía (menor el numero = mejor la condición de la via) (el valor debe estar comprendido entre [1-5]): ')   
            urbanoRural  = input('1 para vía Urbana | 2 para vía Rural: ')   
            print('---------------------------------------------------------------------------------------------------------------------------------------\n')
            print(modelo.realizar_prediccion(numeroVehiculos, numeroBajas, diaSemana, limiteVelocidad, condicionVisual, condicionClima, condicionVial, urbanoRural))
            
            print('\nEl modelo ha sido entrenado con regresión logística\n Las siguientes son estadísticas con referencia al entrenamiento: ')
            print(modelo.testing_accuracy())
            print('\nPara más información consultar el Readme.md')
            break
        else: 
            salir = input('Desea salir sin consultar el modelo? (yes/no): ')
            if salir.lower() not in ('no', 'n'):
                print('Hasta la proxima!')
                break 
            
    
    
    
if __name__ == "__main__":
    main()