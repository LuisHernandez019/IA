import elitism
import queens
import random
import array
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from deap import base
from deap import creator
from deap import tools
from tkinter import Button, StringVar, Tk, Label, Entry, font

def main():
    NUM_OF_QUEENS = int(field_reinas.get())
    POPULATION_SIZE = int(field_poblacion.get())
    MAX_GENERATIONS = int(field_generaciones.get())
    P_MUTATION = float(field_mutar_g.get())
    HALL_OF_FAME_SIZE = 30
    P_CROSSOVER = float(field_cruza_g.get())
    RANDOM_SEED = 42

    random.seed(RANDOM_SEED)

    nQueens = queens.NQueensProblem(NUM_OF_QUEENS)
    toolbox = base.Toolbox()

    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", array.array, typecode='i', fitness=creator.FitnessMin)
    toolbox.register("randomOrder", random.sample, range(len(nQueens)), len(nQueens))
    toolbox.register("individualCreator", tools.initIterate, creator.Individual, toolbox.randomOrder)
    toolbox.register("populationCreator", tools.initRepeat, list, toolbox.individualCreator)

    def getViolationsCount(individual):
        return nQueens.getViolationsCount(individual),

    toolbox.register("evaluate", getViolationsCount)
    toolbox.register("select", tools.selTournament, tournsize=2)
    toolbox.register("mate", tools.cxUniformPartialyMatched, indpb=2.0/len(nQueens))
    toolbox.register("mutate", tools.mutShuffleIndexes, indpb=1.0/len(nQueens))

    population = toolbox.populationCreator(n=POPULATION_SIZE)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("min", np.min)
    stats.register("avg", np.mean)

    hof = tools.HallOfFame(HALL_OF_FAME_SIZE)
    population, logbook = elitism.eaSimpleWithElitism(population, toolbox, cxpb=P_CROSSOVER, mutpb=P_MUTATION, ngen=MAX_GENERATIONS, stats=stats, halloffame=hof, verbose=True)
    minFitnessValues, meanFitnessValues = logbook.select("min", "avg")

    plt.figure(1)
    sns.set_style("whitegrid")
    plt.plot(minFitnessValues, color='red')
    plt.plot(meanFitnessValues, color='green')
    plt.xlabel('Generación')
    plt.ylabel('Fitness Mínimo / Promedio')
    plt.title('Fitness mínimo y promedio alrededor de las generaciones.')
    sns.set_style("whitegrid", {'axes.grid' : False})
    nQueens.plotBoard(hof.items[0])
    plt.show()

if __name__ == "__main__":
    root = Tk()
    root.geometry('620x320')
    root.title('[193269/193291] Problema de las N reinas')
    root.configure(bg='#2A0C4E')
    
    fuente = font.Font(size=13, font='Helvetica 10 bold')
    background = '#2A0C4E'

    test_num_gen = StringVar()
    test_num_gen.set('16')
    label_generaciones = Label(root,text='Número de reinas', width=21, height=1, font=fuente, background=background, fg='white')
    label_generaciones.place(x=40,y=50)
    field_reinas = Entry(root, width=18, font=fuente, textvariable=test_num_gen)
    field_reinas.place(x=60,y=80)
    
    test_num_gen = StringVar()
    test_num_gen.set('100')
    label_generaciones = Label(root,text='Número de generaciones', width=21, height=1, font= fuente, background=background, fg='white')
    label_generaciones.place(x=230,y=50)
    field_generaciones = Entry(root, width=18, font=fuente, textvariable=test_num_gen)
    field_generaciones.place(x=250,y=80)

    test_num_poblacion = StringVar()
    test_num_poblacion.set('300')
    label_poblacion = Label(root,text='Tamaño de la población', width=20, height=1, font= fuente, background=background, fg='white')
    label_poblacion.place(x=40,y=130)
    field_poblacion = Entry(root, width=18, font=fuente, textvariable=test_num_poblacion)
    field_poblacion.place(x=60,y=160)

    test_prob_g = StringVar()
    test_prob_g.set('0.1')
    label_mutar_g = Label(root,text='Probabilidad de mutación', width=30, height=1, font= fuente, background=background, fg='white')
    label_mutar_g.place(x=195,y=130)
    field_mutar_g = Entry(root, width=18, font= fuente, textvariable=test_prob_g)
    field_mutar_g.place(x=250,y=160)

    test_prob_c = StringVar()
    test_prob_c.set('0.9')
    label_cruza_g = Label(root,text='Probabilidad de cruza', width=30, height=1, font= fuente, background=background, fg='white')
    label_cruza_g.place(x=375,y=130)
    field_cruza_g = Entry(root, width=18, font= fuente, textvariable=test_prob_c)
    field_cruza_g.place(x=430,y=160)

    btn_solucion = Button(root, text='Obtener solución', font=fuente, width=17, command=main)
    btn_solucion.place(x=145, y=225)

    root.mainloop()