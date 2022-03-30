from cProfile import label
import numpy as np
import tensorflow as tf

def read_dataset1():
    #Aqui se cambia al Dataset 1 o 3 en la línea 7 (nombre del archivo)
    with open('dataset03.txt', encoding='utf-8', mode= 'r') as values_dataset:
        datos = []
        datos_entrada = []
        y_determinada = []
        _ = values_dataset.readlines(1)
        for linea in values_dataset:
            datos.append([float(x) for x in linea.strip().split(',')])
        
        for dato in datos: 
            datos_entrada.append(dato[0])
            y_determinada.append(dato[1])

        datos_entrada = np.array(datos_entrada)

        y_determinada = np.array(y_determinada)
        return datos_entrada, y_determinada

def read_dataset2():
    with open('dataset02.txt', encoding='utf-8', mode= 'r') as values_dataset:
        datos = []
        datos_entrada1 = []
        datos_entrada2 = []
        datos_entrada3 = []
        y_determinada = []

        _ = values_dataset.readlines(1)
        for linea in values_dataset:
            datos.append([float(x) for x in linea.strip().split(',')])
        i = 0
        for dato in datos: 
            datos_entrada1.append(dato[0])
            datos_entrada2.append(dato[1])
            datos_entrada3.append(dato[2])
            y_determinada.append(dato[3])

        entrada = np.array([datos_entrada1,datos_entrada2,datos_entrada3])
        entrada = entrada.T
        y_determinada = np.array(y_determinada)
        return entrada, y_determinada

if __name__ == "__main__":
    #Dataset01
    #entradas , y_determinada = read_dataset1()

    #Dataset02
    entradas , y_determinada = read_dataset2()

    #Dataset03
    #entradas , y_determinada = read_dataset1()

    #tasa de aprendizaje
    taza_aprendizaje = 0.5 
    taza_aprendizaje_03 = 1.2
    
    perceptron = tf.keras.models.Sequential()
    
    #Dataset 01 y 03
    #perceptron.add(tf.keras.layers.Dense(1, input_dim=1, activation='linear', kernel_initializer='glorot_uniform', bias_initializer='ones'))
    
    #Dataset 02
    perceptron.add(tf.keras.layers.Dense(1, input_dim=3, activation='linear', kernel_initializer='glorot_uniform', bias_initializer='ones'))
    
    #loss = vector del error
    perceptron.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(taza_aprendizaje_03)) 
    perceptron.fit(entradas, y_determinada, epochs=150, batch_size=25, verbose=False)
    
    result = perceptron.predict(entradas)
    print(f'Peso entrada: {perceptron.get_weights()[0]} Peso Bias {perceptron.get_weights()[1]}')
    print(result)