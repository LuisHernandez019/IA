import numpy as np
import pandas as pd
from sklearn.neural_network import MLPRegressor

def entrenar():
    df = pd.read_csv('dataset03.csv')
    datos_entrada =df['X'].to_numpy().reshape(-1,1)
    y_determinada =df['Y'].to_numpy()
    perceptron = MLPRegressor(random_state=1, max_iter=5000).fit(datos_entrada, y_determinada)
    print(perceptron.predict(np.array([52.57]).reshape(-1,1)))

if __name__ == '__main__':
    entrenar()