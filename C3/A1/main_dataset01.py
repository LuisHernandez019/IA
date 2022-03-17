import numpy as np

def read_file(filename):
   try:
      with open(filename, 'r', encoding='utf-8') as file:
         values = []
         file.readlines(1)

         for line in file:
            values.append([float(x) for x in line.strip().split('\t')])

         return values
   except:
      print(f"El archivo '{filename}' no existe.")

def activation_function(u):
   return u

def perceptron(W,X):
   u = X.T.dot(W)
   """
   #A = 2 * 1200 = 1200 * 2
   B = 2,
   2 * 2
   """
   return activation_function(u)

def initialize_data():
   values = read_file('datasets/dataset01.txt')
   entry_values = []
   yd = []

   for value in values:
      entry_values.append(value[0])
      yd.append(value[1])

   bias = np.ones(len(entry_values))
   entry_values = np.array(entry_values)
   X = np.array([entry_values, bias])
   yd = np.array(yd)

   return [X, yd]

def start_training(data):
   X = data[0]
   yd = data[1]
   eta = 0.0000001
   error = 1
   Wk = np.random.uniform(-1,1,2)

   while error > 0.5:
      yc = perceptron(X,Wk)
      ek = yd - yc
      Wk = Wk + (eta * (ek.dot(X.T)))
      error = np.linalg.norm(ek)
      print(error)
      print(yc)
   print(f'W: {Wk} \nYc: {yc}')

   return Wk

if __name__=='__main__':
   data = initialize_data()
   start_training(data)