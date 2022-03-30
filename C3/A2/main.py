import tensorflow as tf
from tensorflow.keras.layers import Conv2D, Dense, MaxPooling2D, Flatten
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
import matplotlib.pyplot as plt

data_augmentation = ImageDataGenerator(
   rescale=1./255,
   rotation_range=45,
   width_shift_range=0.2,
   height_shift_range=0.2,
   horizontal_flip=True
)

data_test_augmentation = ImageDataGenerator(rescale=1./255)
datos_entrenamiento = data_augmentation.flow_from_directory('dataset/train',target_size=(28,28), batch_size=32, class_mode='categorical')

def red_convolucional():
   model = Sequential()

   model.add(Conv2D(16,(3,3),activation='relu', input_shape=(28,28,3)))
   model.add(MaxPooling2D((2,2)))

   model.add(Conv2D(32,(3,3),activation='relu'))
   model.add(MaxPooling2D((2,2)))

   model.add(Flatten())
   model.add(Dense(180,activation='relu'))
   model.add(Dense(90,activation='softmax'))

   model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

   historial = model.fit(datos_entrenamiento, epochs= 15)

   datos_prueba = data_test_augmentation.flow_from_directory('dataset/test', target_size=(28,28), batch_size=32, class_mode='categorical')

   print(model.evaluate(datos_prueba))
   return historial.history['loss']

def primer_red_densa():
   red_densa = Sequential()
   red_densa.add(Flatten())
   red_densa.add(Dense(8,activation='relu'))
   red_densa.add(Dense(90,activation='softmax'))

   red_densa.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

   historial = red_densa.fit(datos_entrenamiento, epochs= 15)

   datos_prueba = data_test_augmentation.flow_from_directory('dataset/test', target_size=(28,28), batch_size=32, class_mode='categorical')

   print(red_densa.evaluate(datos_prueba))
   return historial.history['loss']

def segunda_red_densa():
   red_densa = Sequential()
   red_densa.add(Flatten())
   red_densa.add(Dense(8,activation='relu'))
   red_densa.add(Dense(16,activation='relu'))
   red_densa.add(Dense(4,activation='relu'))
   red_densa.add(Dense(90,activation='softmax'))

   red_densa.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

   historial = red_densa.fit(datos_entrenamiento,epochs= 15)

   datos_prueba = data_test_augmentation.flow_from_directory('dataset/test', target_size=(28,28), batch_size=32, class_mode='categorical')

   print(red_densa.evaluate(datos_prueba))
   return historial.history['loss']

perdida_convolucional = red_convolucional()
perdida_primera_densa = primer_red_densa()
perdida_segunda_densa = segunda_red_densa()

plt.plot(perdida_convolucional, label='Convolucional')
plt.plot(perdida_primera_densa, label='Densa 1')
plt.plot(perdida_segunda_densa, label='Densa 2')
plt.legend()
plt.show()