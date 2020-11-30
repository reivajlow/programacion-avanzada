# funciones lectoras de data

import pandas as pd
import csv
from tarea1.trabajo03.model.Notas import *
from tarea1.trabajo03.model.Alumnos import *


def leer_alumnos():  # lectura de csv retorna lista de objetos
    data = []
    list_A = []
    with open('C:/Users/javoe/PycharmProjects/ayudaprograavanzada/tarea1/trabajo03/data/alumnos.csv', newline='') as f:
        reader = csv.reader(f)
        for linea in reader:
            data.append(linea)
    for a in data:
        list_A.append(Alumnos(str(a[0]), str(a[1]), str(a[2])))
    try:
        del list_A[0]
    except:
        pass
    return list_A


def leer_notas():  # lectura de csv retorna lista de objetos
    data = []
    list_N = []
    with open('C:/Users/javoe/PycharmProjects/ayudaprograavanzada/tarea1/trabajo03/data/notas.csv', newline='') as f:
        reader = csv.reader(f)
        for linea in reader:
            data.append(linea)
    try:
        del data[0]
    except:
        pass
    for i in data:
        x = Notas(str(i[0]), float(i[1]), float(i[2]), float(i[3]), float(i[4]), float(i[5]))
        list_N.append(x)
    return list_N
