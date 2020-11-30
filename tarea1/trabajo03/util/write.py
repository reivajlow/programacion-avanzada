import csv
from os import system
import pandas as pd


# funciones escritoras de csv

def write_alumnos(dataframe):
    dataframe.to_csv("data/alumnos.csv", index=False)
    system("cls")
    pass


def write_notas(dataframe):
    dataframe.to_csv("data/notas.csv", index=False)
    system("cls")
    pass
