import numpy as np

def read_dataset1():
    with open('dataset01.txt', encoding='utf-8', mode= 'r') as values_dataset:
        datos = []
        datos_entrada = []
        y_determinada = []
        _ = values_dataset.readlines(1)
        for linea in values_dataset:
            datos.append([float(x) for x in linea.strip().split('\t')])
        
        for dato in datos: 
            datos_entrada.append(dato[0])
            y_determinada.append(dato[1])
        bias = np.ones(len(datos_entrada))

        datos_entrada = np.array(datos_entrada)

        entrada = np.array([datos_entrada, bias])
        y_determinada = np.array(y_determinada)
        return entrada, y_determinada


def read_dataset2():
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
        bias = np.ones(len(datos_entrada))

        datos_entrada = np.array(datos_entrada)

        entrada = np.array([datos_entrada, bias])
        y_determinada = np.array(y_determinada)
        return entrada, y_determinada



def perceptron(datos_de_entrada,pesos) -> np:
    suma_ponderada : np = datos_de_entrada.T.dot(pesos)
    return suma_ponderada

def entrenar(datos_de_entrada : np,pesos : np, taza_aprendizaje : float, y_determinada : np):
    norm_err : int = 1
    Wk : np = pesos
    
    while norm_err > 0.5:
        y_calculada : np = perceptron(datos_de_entrada,Wk)   
        vector_de_error : np = y_determinada - y_calculada
        norm_err = np.linalg.norm(vector_de_error)
        Wk : np = Wk  + (taza_aprendizaje*(vector_de_error.dot(datos_de_entrada.T)))
    print (f'pesos {Wk} \nY calculada {y_calculada}')
    return Wk


if __name__ == '__main__':
    W0 : np = np.random.uniform(-1,1,2)
    taza_aprendizaje = 0.0000001
    datos_de_entrada, y_determinada = read_dataset1()
    entrenar(datos_de_entrada, W0, taza_aprendizaje, y_determinada)
# print(datos_entrada)
# pesos finales 
# pesos iniciales #*Listo
# funcion de activacion distinta #* Funcion de activacion lineal

#* Pendiente
# BIAS = 1 (Pendiente de poner)
# Pesos iniciales