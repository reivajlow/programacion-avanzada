# funciones para ingresar nuevos objetos (alumnos / notas)
from os import system
from tarea1.trabajo03.model.Alumnos import *
from tarea1.trabajo03.model.Notas import *


def add_alumno(lista_a, lista_n):
    while True:
        system("cls")
        print("ingreso de alumno".center(100, "="))
        print(" *** para finalizar presione enter sin ingresar texto")
        rut = input("ingrese rut: ")
        nombre = input("ingrese nombre: ")
        apellido = input("ingrese apellido: ")
        if rut == "" or nombre == "" or apellido == "":
            break
        else:
            lista_a.append(Alumnos(rut, nombre, apellido))
            add_notas(lista_n, rut)
    system("cls")
    return


def add_notas(lista, rut):
    system("cls")
    print("ingreso de notas".center(100, "="))
    try:
        nota1 = float(input("ingrese nota1: "))
        if 1 <= nota1 <= 7:
            pass
        else:
            nota1 = 0.0
        nota2 = float(input("ingrese nota2: "))
        if 1 <= nota2 <= 7:
            pass
        else:
            nota2 = 0.0
        nota3 = float(input("ingrese nota3: "))
        if 1 <= nota3 <= 7:
            pass
        else:
            nota3 = 0.0
        nota4 = float(input("ingrese nota4: "))
        if 1 <= nota4 <= 7:
            pass
        else:
            nota4 = 0.0
        nota5 = float(input("ingrese nota5: "))
        if 1 <= nota5 <= 7:
            pass
        else:
            nota5 = 0.0
        lista.append(Notas(rut, nota1, nota2, nota3, nota4, nota5))
        print("notas agregadas correctamente")
        system("cls")
    except:
        add_notas(lista, rut)
        input("ingrese valor numerico\n"
              "enter para volver a ingresar notas")
    return
