# funcion para pasar lista de objetos con respectivos atributos a data frame formato pd

import pandas as pd


def frame_alumnos(lista):  # creacion de dataframe
    df = pd.DataFrame([t.frame() for t in lista])
    return df


def frame_notas(notas):  # creacion de data frame
    df = pd.DataFrame([t.frame() for t in notas])
    return df


def frame_promedios(notas):  # creacion de data frame
    df = pd.DataFrame([t.frame_mean() for t in notas])
    return df


def unir_data(alumnos, notas):  # union de datas mediante rut de personas
    alu = frame_alumnos(alumnos)
    nota = frame_notas(notas)
    promedio = frame_promedios(notas)
    juntos = pd.merge(alu, nota, on='Rut')
    juntos = pd.merge(juntos, promedio, on='Rut')
    return juntos


def summary(alumno, nota): #cracion de dataframe de un solo alumno index=[0]
    df1 = pd.DataFrame(alumno.frame(),index=[0])
    df2 = pd.DataFrame(nota.frame(),index=[0])
    df3 = pd.DataFrame(nota.frame_mean(),index=[0])
    juntos = pd.merge(df1, df2, on='Rut')
    juntos = pd.merge(juntos, df3, on='Rut')
    return juntos
