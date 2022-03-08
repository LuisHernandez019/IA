import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, Entry, font

def escalon(u):
    return np.heaviside(u,1)

def perceptron(X,W):
    u = X.dot(W)
    return escalon(u)

def entrenar(X,W, eta, yd):
    errors = []
    yc = perceptron(X,W)
    ek = yd - yc
    errors.append(ek.sum())
    Wk = W
    while ek.sum() != 0:
      Wk = Wk  + (eta*(ek.T.dot(X)))
      yc = perceptron(X,Wk)
      ek = yd - yc
      errors.append(ek.sum())
    return errors , Wk

def extender_arreglos(errors, max_size_array):
    Y = []
    for err in errors:
        error_array = np.array(err)
        size_diff = max_size_array - len(err)
        if size_diff > 0:
            rest_of_array = np.zeros(size_diff, dtype=int)
            error_array = np.concatenate((error_array, rest_of_array))
        Y.append(error_array)
    return Y

def execute_nn():
    X = np.array([[1,0,0],[1,0,1],[1,1,0],[1,1,1]])
    W0 = np.random.rand(3)
    label_FW['text'] = f'Pesos iniciales: {W0}'

    etas = [float(entry_eta1.get()),float(entry_eta2.get()),float(entry_eta3.get()),float(entry_eta4.get()),float(entry_eta5.get())] 

    yd = np.array([int(entry_Y0.get()),int(entry_Y1.get()),int(entry_Y2.get()),int(entry_Y3.get())]) 

    errors = []
    pesos = []
    for eta in etas:
        error, pesos_finales = entrenar(X,W0,eta,yd) 
        errors.append(error)
        pesos.append(pesos_finales)
    max_size_array = len(max(errors,key=len))
    Y = extender_arreglos(errors,max_size_array)

    x = np.arange(0,len(Y[0]))

    label_W0['text'] = f'Pesos finales con Eta {etas[0]}: w0:{round(pesos[0][0],5)} w1:{round(pesos[0][1],5)} w2:{round(pesos[0][2],5)}'
    label_W1['text'] = f'Pesos finales con Eta {etas[1]}: w0:{round(pesos[1][0],5)} w1:{round(pesos[1][1],5)} w2:{round(pesos[1][2],5)}'
    label_W2['text'] = f'Pesos finales con Eta {etas[2]}: w0:{round(pesos[2][0],5)} w1:{round(pesos[2][1],5)} w2:{round(pesos[2][2],5)}'
    label_W3['text'] = f'Pesos finales con Eta {etas[3]}: w0:{round(pesos[3][0],5)} w1:{round(pesos[3][1],5)} w2:{round(pesos[3][2],5)}'
    label_W4['text'] = f'Pesos finales con Eta {etas[4]}: w0:{round(pesos[4][0],5)} w1:{round(pesos[4][1],5)} w2:{round(pesos[4][2],5)}'

    plt.plot(x,Y[0],color='purple',label=f'Eta {etas[0]}')
    plt.plot(x,Y[1],color='yellow',label=f'Eta {etas[1]}')
    plt.plot(x,Y[2],color='red',label=f'Eta {etas[2]}')
    plt.plot(x,Y[3],color='blue',label=f'Eta {etas[3]}')
    plt.plot(x,Y[4],color='pink',label=f'Eta {etas[4]}')
    plt.legend(loc="upper right")
    plt.xlabel('Iteraciones')
    plt.ylabel('Error')
    plt.title('Evaluación del perceptrón')
    plt.show()

if __name__=='__main__':
    root = Tk()
    my_font = font.Font(size=13)
    root.geometry('800x575')
    root.title('[193269/193291] C2.A2.Perceptrón')
    root.configure(bg='#2A0C4E')

    background = '#2A0C4E'

    label_eta1 = Label(root, width=15, font=my_font, text='Eta 1', background=background, fg='white')
    label_eta1.place(x=40,y=20)
    label_eta2 = Label(root, width=15, font=my_font,text='Eta 2', background=background, fg='white')
    label_eta2.place(x=40,y=90)
    label_eta3 = Label(root, width=15, font=my_font,text='Eta 3', background=background, fg='white')
    label_eta3.place(x=40,y=160)
    label_eta4 = Label(root, width=15, font=my_font,text='Eta 4', background=background, fg='white')
    label_eta4.place(x=40,y=230)
    label_eta5 = Label(root, width=15, font=my_font,text='Eta 5', background=background, fg='white')
    label_eta5.place(x=40,y=300)

    entry_eta1 = Entry(root,width=14, font=my_font)
    entry_eta1.place(x=40,y=50)
    entry_eta2 = Entry(root,width=14, font=my_font)
    entry_eta2.place(x=40,y=120)
    entry_eta3 = Entry(root,width=14, font=my_font)
    entry_eta3.place(x=40,y=190)
    entry_eta4 = Entry(root,width=14, font=my_font)
    entry_eta4.place(x=40,y=260)
    entry_eta5 = Entry(root,width=14, font=my_font)
    entry_eta5.place(x=40,y=330)

    label_Ys = Label(root, width=15, font=my_font, text='Yd:', background=background, fg='white')
    label_Ys.place(x=90,y=400)

    entry_Y0 = Entry(root,width=8, font=my_font)
    entry_Y0.place(x=250,y=400)
    entry_Y1 = Entry(root,width=8, font=my_font)
    entry_Y1.place(x=350,y=400)
    entry_Y2 = Entry(root,width=8, font=my_font)
    entry_Y2.place(x=450,y=400)
    entry_Y3 = Entry(root,width=8, font=my_font)
    entry_Y3.place(x=550,y=400)

    btn_exec_nn = Button(root, width=14, text='Ejecutar', font=my_font, command=execute_nn)
    btn_exec_nn.place(x=360,y=500)

    label_FW = Label(root, width=60, font=my_font, background=background, fg='white')
    label_FW.place(x=190,y=450)
    label_W0 = Label(root, width=60, font=my_font, background=background, fg='white')
    label_W0.place(x=190,y=50)
    label_W1 = Label(root, width=60, font=my_font, background=background, fg='white')
    label_W1.place(x=190,y=120)
    label_W2 = Label(root, width=60, font=my_font, background=background, fg='white')
    label_W2.place(x=190,y=190)
    label_W3 = Label(root, width=60, font=my_font, background=background, fg='white')
    label_W3.place(x=190,y=260)
    label_W4 = Label(root, width=60, font=my_font, background=background, fg='white')
    label_W4.place(x=190,y=330)

    root.mainloop()