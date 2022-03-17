from sklearn.neural_network import MLPRegressor
import numpy as np
import pandas as pd

def entrenar():
    datos_csv = pd.read_csv('dataset02.csv')

    entrada_1 =datos_csv['x1'].to_numpy()
    entrada_2 =datos_csv['x2'].to_numpy()
    entrada_3 =datos_csv['x3'].to_numpy()
    y_determinada =datos_csv['Y'].to_numpy()
    entradas_X = np.array([entrada_1, entrada_2, entrada_3]).T
    print(entradas_X.shape)
    print(y_determinada.shape)
    perceptron = MLPRegressor(random_state=1, max_iter=5000).fit(entradas_X, y_determinada)
    print(perceptron.predict(np.array([[95.71],[76.75],[30.74]]).T))
    print(perceptron.score(entradas_X, y_determinada))
    for weight in perceptron.coefs_:
        print(weight.T)


if __name__ == '__main__':
    entrenar()