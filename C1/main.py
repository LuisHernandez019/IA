import matplotlib.pyplot as plt
from random import randint, uniform
import math
import statistics
from tkinter import Label, Tk, Button, Entry, StringVar
from tkinter import font

min_val_x = '' 
min_val_y = '' 
max_val_x = ''
max_val_y = ''

res_x = ''
res_y = ''
generaciones = ''
poblacion = ''
prob_mutate_individual = ''
prob_mutate_gen = ''

def crear_genotipo(tamanio_gen):
    genotipo = []
    for i in range(tamanio_gen):
        genotipo.append(randint(0,1))
    return genotipo

def tamanio_gen(num_puntos):
    return num_puntos.bit_length()

def calcular_puntos(rango, resolucion):
    return int((rango/resolucion) + 1)

def obtener_rango(val_min, val_max):
    return val_max - val_min

def juntar_lista(lista):
    return "".join(map(str, lista))

def g(x,y):
    try:
        aptitud = 5 / (math.pow(y,3) + math.sqrt(math.pow(x,3)))
    except (ValueError, ZeroDivisionError):
        aptitud = 0
    return aptitud

def get_fenotipo(min_val,gen,res):
    gen = juntar_lista(gen)
    i = int(gen,2)
    return min_val + (i*res)

def get_fenotipos(individual, min_val_x, min_val_y, resolutions):
    x = get_fenotipo(min_val_x, individual[0], resolutions[0])
    y = get_fenotipo( min_val_y, individual[1], resolutions[1])
    return (x,y)

def get_all_fenotipos(population, min_val_x, min_val_y, max_val_x, max_val_y, resolutions):
    fenotipos = []

    for individual in population:
        fenotipo = get_fenotipos(individual, min_val_x, min_val_y, resolutions)
        fenotipos.append(fenotipo)
    for i, j in enumerate(fenotipos):
        if j[0] > max_val_x or j[1] > max_val_y:
            fenotipos.pop(i)
            population.pop(i)

    return [population,fenotipos]

def generate_individuo(gen_x, gen__y):
    gen_x = crear_genotipo(gen_x)
    gen_y = crear_genotipo(gen__y)
    return [gen_x, gen_y]

def generate_population(gen_size_x, gen_size_y, min_val_x, max_val_x, min_val_y, max_val_y,resolutions, population_size):
    population = crear_poblacion_inicial(gen_size_x,gen_size_y, population_size)
    matrix_individual = get_all_fenotipos(population, min_val_x, min_val_y, max_val_x, max_val_y, resolutions)
    return matrix_individual

def crear_poblacion_inicial(gen_size_x, gen_size_y, poblacion_size):
    poblacion_inicial = []

    for i in range(poblacion_size):
        new_individuo = generate_individuo(gen_size_x, gen_size_y)
        poblacion_inicial.append(new_individuo)

    return poblacion_inicial

def create_parejas(population):
    temp = population.copy()
    parejas = []

    if (len(temp) % 2) != 0:
        temp.pop(randint(0,len(temp)-1))
    while len(temp) > 0:
        parent_1 =temp.pop(randint(0,len(temp)-1))
        if len(temp) == 1:
            parent_2 = temp.pop(0)
        else:
            parent_2 = temp.pop(randint(0,len(temp)-1))
        parejas.append([parent_1,parent_2])

    return parejas

def create_hijos(couple, population, prob_mutate_individual, prob_mutate_gen):
    parent_1 = couple[0]
    parent_2 = couple[1]

    gen_p1_x = parent_1[0]
    gen_p1_y = parent_1[1]
    gen_p2_x = parent_2[0]
    gen_p2_y = parent_2[1]

    pos_x = randint(0,len(gen_p1_x)-1)
    pos_y = randint(0,len(gen_p1_y)-1)

    pasar_gen1_x = gen_p1_x[pos_x:]
    pasar_gen2_x = gen_p2_x[:pos_x]

    pasar_gen1_y = gen_p1_y[pos_y:]
    pasar_gen2_y = gen_p2_y[:pos_y]

    hijo_1_x = gen_p1_x[pos_x:] + pasar_gen2_x
    hijo_1_y = gen_p1_y[pos_y:] + pasar_gen2_y

    hijo_2_x = gen_p2_x[:pos_x] + pasar_gen1_x
    hijo_2_y = gen_p2_y[:pos_y] + pasar_gen1_y
    
    for gen in [hijo_1_x, hijo_1_y, hijo_2_x, hijo_2_y]:
        mutatacion(gen, prob_mutate_individual, prob_mutate_gen )

    population.append([hijo_1_x, hijo_1_y])
    population.append([hijo_2_x, hijo_2_y])

def mutatacion(genotipo, prob_mutate_individual ,prob_mutate_gen):
    if uniform(0,1) <= prob_mutate_individual:
        new_gen =  genotipo.copy()
        for i,j in enumerate(new_gen):
            if uniform(0,1) <= prob_mutate_gen:
                if j == 1:
                    new_gen[i] = 0
                else:
                    new_gen[i] = 1
        genotipo = new_gen

    return genotipo

def evaluate_population(individuos):
    fitness_list = []
    for fenotipo in individuos[1]:
        fitness_list.append(g(fenotipo[0],fenotipo[1]))

    return [individuos[0], individuos[1],fitness_list]

def cortar_minimos(individuos):
    index_to_crop = individuos[2].index(min(individuos[2]))
    individuos[0].pop(index_to_crop) 
    individuos[1].pop(index_to_crop) 
    individuos[2].pop(index_to_crop) 

def cortar_maximos(individuos):
    index_to_crop = individuos[2].index(max(individuos[2]))
    individuos[0].pop(index_to_crop) 
    individuos[1].pop(index_to_crop) 
    individuos[2].pop(index_to_crop) 

def get_best_individual(individuos,mejores_soluciones, maximo):
    normalized_fitness = [individual_fitness for individual_fitness in individuos[2] if individual_fitness is not None]
    if maximo:
        index = individuos[2].index(max(normalized_fitness))
    else:
        index = individuos[2].index(min(normalized_fitness))

    mejores_soluciones[0].append(individuos[0][index]) 
    mejores_soluciones[1].append(individuos[1][index])
    mejores_soluciones[2].append(individuos[2][index])

def algoritmo_genetico(maximo):
    global min_val_x
    global min_val_y
    global res_x
    global res_y
    global generaciones  
    global poblacion 
    global prob_mutate_individual
    global prob_mutate_gen 
    min_val_x = float(field_min_x.get())
    min_val_y = float(field_min_y.get())
    max_val_x = float(field_max_x.get())
    max_val_y = float(field_max_y.get())
    res_x = float(field_res_x.get())
    res_y = float(field_res_y.get())
    generaciones = int(field_generaciones.get())
    poblacion = int(field_generaciones.get())
    prob_mutate_individual = float(field_mutar_i.get())
    prob_mutate_gen = float(field_mutar_g.get())

    aptitud_maxima = []
    aptitud_minima = []
    aptitud_promedio = []
    mejores_soluciones = [[],[],[]]

    range_x = obtener_rango(min_val_x,max_val_x)
    num_points_x = calcular_puntos(range_x,res_x)
    gen_size_x = tamanio_gen(num_points_x)

    range_y = obtener_rango(min_val_y,max_val_y)
    num_points_y = calcular_puntos(range_y,res_y)
    gen_size_y = tamanio_gen(num_points_y)

    my_poblacion = generate_population(gen_size_x,gen_size_y, min_val_x, max_val_x, min_val_y, max_val_y, [res_x, res_y], poblacion)

    population = my_poblacion[0]
    individuos = evaluate_population(my_poblacion)

    aptitudes = []
    for aptitud in individuos[2]:
        if aptitud > 0:
            aptitudes.append(aptitud)
    
    if len(aptitudes) >= 1:
        aptitud_maxima.append(max(aptitudes))
        aptitud_minima.append(min(aptitudes))
        aptitud_promedio.append(statistics.mean(aptitudes))
        get_best_individual(individuos,mejores_soluciones, maximo)

    parejas = create_parejas(population)
    for pareja in parejas:
        create_hijos(pareja,population, prob_mutate_individual, prob_mutate_gen)

    individuos = get_all_fenotipos(population, min_val_x, min_val_y, max_val_x, max_val_y, [res_x, res_y])
    individuos = evaluate_population(individuos)
    while 0 in individuos[2]:
        for i in range(len(individuos[2])):
            if individuos[2][i] == 0:
                individuos[0].pop(i)
                individuos[1].pop(i)
                individuos[2].pop(i)

    for i in range(generaciones):
        while len(individuos[0]) > poblacion:
            if maximo:
                cortar_minimos(individuos)
            else:
                cortar_maximos(individuos)
        individuos = get_all_fenotipos(individuos[0], min_val_x, min_val_y, max_val_x, max_val_y, [res_x, res_y])
        individuos = evaluate_population(individuos)
        while 0 in individuos[2]:
            for i in range(len(individuos[2])):
                if individuos[2][i] == 0:
                    individuos[0].pop(i)
                    individuos[1].pop(i)
                    individuos[2].pop(i)
        if len(individuos[2]) >= 1:
            aptitud_maxima.append(max(individuos[2]))
            aptitud_minima.append(min(individuos[2]))
            aptitud_promedio.append(statistics.mean(individuos[2]))
            get_best_individual(individuos,mejores_soluciones, maximo)
            
        parejas = create_parejas(individuos[0])
        for couple in parejas:
            create_hijos(couple,individuos[0], prob_mutate_individual, prob_mutate_gen)
    
    if len(mejores_soluciones[0]) > 0:
        if maximo:
            index = mejores_soluciones[2].index(max(mejores_soluciones[2]))
            complemento = 'El punto máximo es: '
        else:
            index = mejores_soluciones[2].index(min(mejores_soluciones[2]))
            complemento = 'El punto mínimo es: '

        mejor_solucion = (mejores_soluciones[0][index],mejores_soluciones[1][index],mejores_soluciones[2][index])
        txt_resultado['text'] = f'{complemento}{mejor_solucion[1]}\nSu valor es: {mejor_solucion[2]}'
        
        mejores_x = []
        mejores_y = []

        for ejes in mejores_soluciones[1]:
            mejores_x.append(ejes[0])
            mejores_y.append(ejes[1])
        
        fig = plt.figure(figsize=(10,5))
        fig.tight_layout()
        plt.style.use('_mpl-gallery')
        x = []

        for i in range(len(aptitud_maxima)):
            x.append(i)

        ax = plt.subplot(1,2,1)
        ax.plot(x,aptitud_maxima, label='Caso Máximo')
        ax.plot(x,aptitud_promedio, label='Caso Promedio')
        ax.plot(x,aptitud_minima, label='Caso Mínimo')
        ax.legend(loc='best')

        if maximo:
            ax.set_title('Buscando máximo')
        else:
            ax.set_title('Buscando mínimo')
        
        ax_2 = plt.subplot(1,2,2)
        ax_2.scatter(mejores_x,mejores_y)
        ax_2.set_xlabel("X")
        ax_2.set_ylabel("Y")
        ax_2.set_title("Mejores individuos")
        
        plt.show()
    else:
        txt_resultado['text'] = 'La función no está definida en los intervalos definidos'

def buscar_maximo():
    algoritmo_genetico(True)

def buscar_minimo():
    algoritmo_genetico(False)

if __name__ == '__main__':
    root = Tk()
    root.geometry('735x375')
    root.title('[193269/193291] IA.C1.A1 Algoritmo genético de 2 variables')
    root.configure(bg='#2A0C4E')
    fuente = font.Font(size=13, font='Helvetica 10 bold')
    background = '#2A0C4E'

    label_min_x = Label(root,text='Valor mínimo de X', width=17, height=1, font=fuente, background=background, fg='white')
    label_min_x.place(x=5,y=10)
    text_entry_test_1 = StringVar()
    text_entry_test_1.set('1')
    
    text_entry_test_3 = StringVar()
    text_entry_test_3.set('1')
    
    text_entry_test_2 = StringVar()
    text_entry_test_2.set('3')

    text_entry_test_4 = StringVar()
    text_entry_test_4.set('3')
    field_min_x = Entry(root, width=18, font= fuente, textvariable=text_entry_test_1)
    field_min_x.place(x=10,y=40)

    label_max_x = Label(root,text='Valor máximo de X', width=17, height=1, font= fuente, background=background, fg='white')
    label_max_x.place(x=192.5,y=10)

    field_max_x = Entry(root, width=18, font= fuente, textvariable=text_entry_test_2)
    field_max_x.place(x=200,y=40)

    label_min_y = Label(root,text='Valor mínimo de Y', width=17, height=1, font= fuente, background=background, fg='white')
    label_min_y.place(x=382.5,y=10)
    field_min_y = Entry(root, width=18, font= fuente, textvariable=text_entry_test_3)
    field_min_y.place(x=390,y=40)

    label_max_y = Label(root,text='Valor máximo de Y', width=17, height=1, font= fuente, background=background, fg='white')
    label_max_y.place(x=575,y=10)
    field_max_y = Entry(root, width=18, font= fuente, textvariable=text_entry_test_4)
    field_max_y.place(x=580,y=40)

    test_resolucion_1 = StringVar()
    test_resolucion_1.set('0.001')
    test_resolucion_2 = StringVar()
    test_resolucion_2.set('0.0015')

    label_res_x = Label(root,text='Resolución de X', width=17, height=1, font= fuente, background=background, fg='white')
    label_res_x.place(x=5,y=100)
    field_res_x = Entry(root, width=18, font= fuente, textvariable=test_resolucion_1)
    field_res_x.place(x=10,y=130)
    
    label_res_y = Label(root,text='Resolución de Y', width=17, height=1, font= fuente, background=background, fg='white')
    label_res_y.place(x=195,y=100)
    field_res_y = Entry(root, width=18, font= fuente, textvariable=test_resolucion_2)
    field_res_y.place(x=200,y=130)

    test_num_gen = StringVar()
    test_num_gen.set('100')
    label_generaciones = Label(root,text='Número de Generaciones', width=21, height=1, font= fuente, background=background, fg='white')
    label_generaciones.place(x=370,y=100)

    field_generaciones = Entry(root, width=18, font= fuente, textvariable=test_num_gen)
    field_generaciones.place(x=390,y=130)

    test_num_poblacion = StringVar()
    test_num_poblacion.set('100')
    label_poblacion = Label(root,text='Tamaño de la población', width=20, height=1, font= fuente, background=background, fg='white')
    label_poblacion.place(x=560,y=100)

    field_poblacion = Entry(root, width=18, font= fuente, textvariable=test_num_poblacion)
    field_poblacion.place(x=580,y=130)

    test_prob_i = StringVar()
    test_prob_i.set('0.13')
    label_mutar_i = Label(root,text='Probabilidad de mutación de individuo', width=30, height=1, font= fuente, background=background, fg='white')
    label_mutar_i.place(x=95.5,y=190)
    field_mutar_i = Entry(root, width=18, font= fuente, textvariable=test_prob_i)
    field_mutar_i.place(x=145,y=220)
    
    test_prob_g = StringVar()
    test_prob_g.set('0.1')
    label_mutar_g = Label(root,text='Probabilidad de mutación de gen', width=30, height=1, font= fuente, background=background, fg='white')
    label_mutar_g.place(x=390,y=190)
    field_mutar_g = Entry(root, width=18, font= fuente, textvariable=test_prob_g)
    field_mutar_g.place(x=450,y=220)

    btn_maximo = Button(root, text='Buscar máximo', font=fuente, width=17, command= buscar_maximo)
    btn_maximo.place(x=100, y=320)
    
    btn_minimo = Button(root, text='Buscar mínimo', font=fuente, width=17, command= buscar_minimo)
    btn_minimo.place(x=450, y=320)

    txt_resultado = Label(root,text='', width=50,height=2, font= fuente, background=background, fg='white')
    txt_resultado.place(x=150,y=265)

    root.mainloop()