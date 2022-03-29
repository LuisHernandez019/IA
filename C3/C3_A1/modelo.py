import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras import models
from tensorflow.keras.layers import Dense, Dropout
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold

def transformar():
    df = pd.read_csv('dataset-turismo.csv')

    temporada = df['Temporada'].values
    preferencia = df['Preferencia'].values
    presupuesto = df['Presupuesto'].values 
    cant_personas = df['Cantidad de personas'].values
    lugar = df['Lugar'].values

    #Transformación y normalización de datos
    categoria_a_num = LabelEncoder()
    temporada = categoria_a_num.fit_transform(temporada)
    preferencia = categoria_a_num.fit_transform(preferencia)
    lugar = categoria_a_num.fit_transform(lugar)
    presupuesto = presupuesto / 10000
    return [temporada, preferencia, presupuesto, cant_personas], lugar

def crossvalidation(K, datos, yd):
    crossvalidation = KFold(n_splits=K)
    entradas = np.array([datos[0], datos[1], datos[2], datos[3]]).T
    datos_entrenamiento, lugar_entrenamiento = [], []
    datos_validacion, lugar_validacion = [], []

    for entrenamiento, validacion in crossvalidation.split(entradas):
        datos_entrenamiento.append(entradas[entrenamiento])
        datos_validacion.append(entradas[validacion])
        lugar_entrenamiento.append(yd[entrenamiento])
        lugar_validacion.append(yd[validacion])
    
    return datos_entrenamiento, lugar_entrenamiento, datos_validacion, lugar_validacion

if __name__ == '__main__':
    K =  3
    datos, lugar = transformar()
    entrenamiento_data, entrenamiento_price , val_data, val_price = crossvalidation(K,datos,lugar)

    fig=plt.figure()
    subplot1=fig.add_subplot(2,1,1)
    subplot2=fig.add_subplot(2,1,2)
    for i,dataset in enumerate(entrenamiento_data):
        model = models.Sequential()
        model.add(Dense(64,input_dim=4,activation='relu',bias_initializer='ones'))
        model.add(Dense(500,activation='relu'))
        model.add(Dense(1000,activation='relu'))
        model.add(Dropout(0.4))
        model.add(Dense(1000,activation='relu'))
        model.add(Dense(1,activation='relu'))
        model.compile(optimizer='rmsprop', loss='mse',metrics=['mae'])
        history = model.fit(dataset, entrenamiento_price[i], validation_data=(val_data[i], val_price[i]), epochs=100,batch_size=10)
        model.save(f'model_{i+1}.h5')
        subplot1.plot(history.history['mae'], label=f'Error Entrenamiento Crossvalidation {i+1}')
        subplot1.legend()
        subplot2.plot(history.history['val_mae'], '--',label=f'Error Validación Crossvalidation {i+1}')
        subplot2.legend()
    plt.show()