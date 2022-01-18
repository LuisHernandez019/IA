import numpy as np

class Individuo():
   def __init__(self):
      self.genotipo = None
      self.fenotipo = None
      self.aptitud = None

   def set_genotipo(self,genotipo):
      self.genotipo = genotipo

   def set_fenotipo(self,fenotipo):
      self.fenotipo = fenotipo

   def set_aptitud(self,aptitud):
      self.aptitud = aptitud

   def get_genotipo(self):
      return self.genotipo

   def get_fenotipo(self):
      return self.fenotipo

   def get_aptitud(self):
      return self.aptitud

def apareamiento():
   pass

def proceso_iterativo():
   apareamiento()

# Inicialización

def get_aptitud(fenotipo):
   return (fenotipo / 2) * np.cos((np.pi * fenotipo) / 2)

def get_fenotipo(genotipo):
   i = array_binario_a_int(genotipo)
   return VALOR_MIN + (i * RESOLUCION)

def array_binario_a_int(binary_array):
   binary_array = map(str,binary_array)
   binary_string = "".join(binary_array)
   return int(binary_string, 2)

def get_num_genes():
   num_puntos = get_num_puntos()
   return num_puntos.bit_length()

def get_num_puntos():
   return int(RANGO / RESOLUCION) + 1

def generar_genotipo():
   num_genes = get_num_genes()
   return np.random.randint(0, 2, num_genes)

def generar_poblacion():
   poblacion = []

   while len(poblacion) != TAM_POB_INICIAL:
      ind_tmp = Individuo()

      genotipo = generar_genotipo()
      fenotipo = get_fenotipo(genotipo)
      aptitud = get_aptitud(fenotipo)

      ind_tmp.set_genotipo(genotipo)
      ind_tmp.set_fenotipo(fenotipo)
      ind_tmp.set_aptitud(aptitud)

      if ind_tmp.get_fenotipo() >= VALOR_MIN and ind_tmp.get_fenotipo() <= VALOR_MAX:
         poblacion.append(ind_tmp)

   return poblacion

def inicializacion():
   poblacion = generar_poblacion()

   for individuo in poblacion:
      print(individuo.get_fenotipo())

if __name__ == '__main__':
   TAM_POB_INICIAL = 4                  # Tamaño población inicial
   TAM_POB_MAX = 6                      # Tamaño población máxima
   VALOR_MIN = 4                        # Valor mínimo
   VALOR_MAX = 10                       # Valor máximo
   RANGO = VALOR_MAX - VALOR_MIN
   RESOLUCION = 0.01
   PRO_MUT_IND = 0.15                   # Probabilidad de mutación del individuo
   PRO_MUT_GEN = 0.25                   # Probabilidad de mutación del gen
   PRO_MUT = PRO_MUT_IND * PRO_MUT_GEN  # Probabilidad de mutación

   inicializacion()
   proceso_iterativo()