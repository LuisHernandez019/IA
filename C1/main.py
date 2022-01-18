class Individuo():
   def __init__(self):
      self.genotipo
      self.fenotipo
      self.aptitud

def get_fenotipo(genotipo):
   i = binary_array_to_int(genotipo)
   return MIN_VALUE + (i * RESOLUCION)

def binary_array_to_int(binary_array):
   binary_array = map(str,binary_array)
   binary_string = "".join(binary_array)
   return int(binary_string,2)

def get_num_genes():
   return num_puntos.bit_length()

def get_num_puntos():
   return int(RANGO/RESOLUCION)+1

if __name__ == '__main__':
   MAX_VALUE = 10
   MIN_VALUE = 4
   RANGO = MAX_VALUE - MIN_VALUE
   RESOLUCION = 0.01

   num_puntos = get_num_puntos()
   num_genes = get_num_genes()


   array_binarios = [0,1,1,0,1,0,1,0,1,1]
   print(binary_array_to_int(array_binarios))