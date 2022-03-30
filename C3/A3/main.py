from tkinter import Tk, Entry, Button, Label, font
from tkinter.ttk import Combobox
from tensorflow.keras.models import load_model
import numpy as np

#yc = model.predict(train_data[0]).astype(int)


def elegir_lugar(num):
    resultado = ''
    if num == 0:
        resultado = 'Bernal, Querétaro'
    elif num == 1:
        resultado = 'CDMX'
    elif num == 2:
        resultado = 'Cancún, Quintana Roo'
    elif num == 3:
        resultado = 'Cholula, Puebla'
    elif num == 4:
        resultado = 'Comitán, Chiapas'
    elif num == 5:
        resultado = 'Guadalajara, Jalisco'
    elif num == 6:
        resultado = 'Monterrey, Nuevo León'
    elif num == 7:
        resultado = 'Mérida, Yucatán'
    elif num == 8:
        resultado = 'San Cristóbal, Chiapas'
    elif num == 9:
        resultado = 'Tijuana'
    elif num == 10:
        resultado = 'Tulum, Quintana Roo'

    return resultado

def ejecutar():
    model = load_model('./model_2.h5')
    temporada = temporada_combo.get()

    sitio = sitio_combo.get()
    presupuesto = int(input_presupuesto.get())
    cantidad = int(input_cantidad.get())
    datos = np.zeros(4)

    if temporada == 'Fiestas Patrias':
        datos[0] = np.array([0])
    elif temporada == 'Fin de año':
        datos[0] = np.array([1])
    elif temporada == 'Navidad':
        datos[0] = np.array([2])
    elif temporada == 'Semana Santa':
        datos[0] = np.array([3])
    else:
        datos[0] = np.array([4])

    if sitio == 'Ciudad':
        datos[1] = np.array([0])
    elif sitio == 'Mar':
        datos[1] = np.array([1])
    else:
        datos[1] = np.array([2])

    presupuesto = presupuesto / 10000
    datos[2] = np.array([presupuesto])
    datos[3] = np.array([cantidad])
    datos = datos.reshape(4,1)
    res = model.predict(datos.T).astype(int)
    prediction = res[0][0]
    lugar = elegir_lugar(prediction)
    resultado['text'] = lugar

if __name__ == '__main__':
    master = Tk()
    master.geometry('600x500')
    master.title('Recomendación de destinos')


    label_temporada = Label(master,text='Escoja una temporada preferida',font=font.Font(size=13)).place(x=10,y=10)
    temporada_combo = Combobox(master,font=font.Font(size=13))
    temporada_combo['values'] = ('Fiestas Patrias','Fin de año','Navidad','Semana Santa','Verano')
    temporada_combo['state'] = 'readonly'
    temporada_combo.place(x=20,y=50)

    label_sitio = Label(master,text='Escoja un sitio de preferencia',font=font.Font(size=13)).place(x=300,y=10)
    sitio_combo = Combobox(master,font=font.Font(size=13))
    sitio_combo['values'] = ('Ciudad','Mar','Pueblo Mágico')
    sitio_combo['state'] = 'readonly'
    sitio_combo.place(x=320,y=50)

    label_presupuesto = Label(master,text='Ingrese su presupuesto',font=font.Font(size=13)).place(x=10,y=200)
    input_presupuesto = Entry(master,width=15,font=13)
    input_presupuesto.place(x=10,y=250)

    label_cantidad = Label(master,text='Ingrese la cantidad de personas a viajar',font=font.Font(size=13)).place(x=270,y=200)
    input_cantidad = Entry(master,width=15,font=13)
    input_cantidad.place(x=300,y=250)

    resultado = Label(master,text='',font=font.Font(size=15))
    resultado.place(x=200,y=400)

    btn_ejecutar = Button(master,text='Ejecutar',font=font.Font(size=14),command=ejecutar,width=20)
    btn_ejecutar.place(x=180,y=330)

    master.mainloop()