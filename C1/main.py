import numpy as np

class Individuo():
   def __init__(self):
      self.genotipo = None
      self.fenotipo_x = None
      self.fenotipo_y = None
      self.aptitud = None

   def set_genotipo(self,genotipo):
      self.genotipo = genotipo

   def set_fenotipo_x(self,fenotipo):
      self.fenotipo_x = fenotipo

   def set_fenotipo_y(self,fenotipo):
      self.fenotipo_y = fenotipo

   def set_aptitud(self,aptitud):
      self.aptitud = aptitud

   def get_genotipo(self):
      return self.genotipo

   def get_fenotipo_x(self):
      return self.fenotipo_x
   
   def get_fenotipo_y(self):
      return self.fenotipo_y

   def get_aptitud(self):
      return self.aptitud

def cruza(parejas):
   pass

def apareamiento():
   pob_tmp = poblacion.copy()
   couples = []

   if len(pob_tmp) % 2 != 0:
      num_random = np.random.randint(0,len(pob_tmp)-1)
      pob_tmp.pop(num_random)

   while len(pob_tmp) > 0:
      num_random = np.random.randint(0,len(pob_tmp)-1)
      padre = pob_tmp.pop(num_random)

      if len(pob_tmp) == 1:
         madre = pob_tmp.pop(0)
      else:
         num_random = np.random.randint(0,len(pob_tmp)-1)
         madre = pob_tmp.pop(num_random)

      couples.append([padre,madre])
   
   return couples

def proceso_iterativo():
   for i in range(len(poblacion)):
      print(f"Individuo {i} \nGenotipo: {poblacion[i].get_genotipo()} Fenotipo X: {poblacion[i].get_fenotipo_x()} Fenotipo Y: {poblacion[i].get_fenotipo_y()} Aptitud: {poblacion[i].get_aptitud()}")

def get_aptitud(x,y):
   return (5 / (pow(y,3) + np.sqrt(pow(x,3))))

def get_fenotipo(genotipo,valor_min):
   value = array_binario_to_int(genotipo)
   return round((valor_min + (value * RESOLUCION)),2)

def array_binario_to_int(binary_array):
   binary_array = map(str,binary_array)
   binary_string = "".join(binary_array)
   return int(binary_string, 2)

def get_num_bits(rango):
   num_puntos = get_num_puntos(rango)
   return num_puntos.bit_length()

def get_num_puntos(rango):
   return int(rango / RESOLUCION) + 1

def generar_genotipo(rango):
   num_genes = get_num_bits(rango)
   return np.random.randint(0, 2, num_genes)

def generar_poblacion():
   population = []

   while len(population) != TAM_POB:
      ind_tmp = Individuo()

      genotipo_i = generar_genotipo(RANGO_X)
      genotipo_j = generar_genotipo(RANGO_Y)
      genotipo = np.concatenate((genotipo_i,genotipo_j))
      fenotipo_x = get_fenotipo(genotipo_i,VALOR_MIN_X)
      fenotipo_y = get_fenotipo(genotipo_j,VALOR_MIN_Y)
      aptitud = get_aptitud(fenotipo_x,fenotipo_y)

      ind_tmp.set_genotipo(genotipo)
      ind_tmp.set_fenotipo_x(fenotipo_x)
      ind_tmp.set_fenotipo_y(fenotipo_y)
      ind_tmp.set_aptitud(aptitud)

      if ind_tmp.get_fenotipo_x() >= VALOR_MIN_X \
         and ind_tmp.get_fenotipo_x() <= VALOR_MAX_X \
         and ind_tmp.get_fenotipo_y() >= VALOR_MIN_Y \
         and ind_tmp.get_fenotipo_y() >= VALOR_MIN_Y:
         population.append(ind_tmp)

   return population

def inicializacion():
   global poblacion
   poblacion = generar_poblacion()

if __name__ == '__main__':
   TAM_POB = 3
   TOTAL_GEN = 1
   RESOLUCION = 0.7

   VALOR_MIN_X = 3
   VALOR_MAX_X = 15
   RANGO_X = VALOR_MAX_X - VALOR_MIN_X

   VALOR_MIN_Y = 50
   VALOR_MAX_Y = 85
   RANGO_Y = VALOR_MAX_Y - VALOR_MIN_Y

   PRO_MUT_IND = 0.15                   # Probabilidad de mutación del individuo
   PRO_MUT_GEN = 0.25                   # Probabilidad de mutación del gen
   PRO_MUT = PRO_MUT_IND * PRO_MUT_GEN  # Probabilidad de mutación

   inicializacion()
   proceso_iterativo()