"""
Programa de administracion de estudiantes y notas
desarrollado por javier saavedra
ultima modificacion 2020/06/26
python 3.8.3
codificacion utf-8
"""

# importacion
from typing import List
import os
import sys
from tarea1.trabajo03.util.add import add_alumno
from tarea1.trabajo03.util.read import leer_notas, leer_alumnos
from tarea1.trabajo03.util.write import write_alumnos, write_notas
from tarea1.trabajo03.util.dataframe import frame_alumnos, frame_notas, unir_data
from tarea1.trabajo03.util.menu import menu, menu2, descripcion
from tarea1.trabajo03.util.setter import setter_alumno, setter_notas
from tarea1.trabajo03.util.reports import report_curso, report_alumno
from tarea1.trabajo03.model.Notas import *
from tarea1.trabajo03.model.Alumnos import *


#lectura de data base
alumnos = list()
notas = list()
alumnos: List[Alumnos] = leer_alumnos()
notas: List[Notas] = leer_notas()

#confirmacion base de datos
if not alumnos and not notas:
    input("debe agregar un alumno para iniciar\n"
          "Enter para ingresar alumno")
    os.system("cls")
    add_alumno(alumnos, notas)
    write_alumnos(frame_alumnos(alumnos))
    write_notas(frame_notas(notas))
elif alumnos and notas:
    pass
else:
    input("problemas con las bases de datos")
    sys.exit()

descripcion()

while True:
    os.system("cls")

    try:
        opcion = menu2()
    except:
        opcion=0
        input("ingrese un valor numerico")
    if opcion == 1: # agregar alumnos
        os.system("cls")
        add_alumno(alumnos,notas)
        write_alumnos(frame_alumnos(alumnos))
        write_notas(frame_notas(notas))
        pass
    elif opcion == 2: #mostrar alumnos y notas
        os.system("cls")
        mostrar = unir_data(alumnos,notas)
        print("alumnos y notas".center(100,"="))
        print(mostrar)
        input("\n\n\n ENTER PARA SALIR")
        pass
    elif opcion == 3: #modificar alumnos
        os.system("cls")
        setter_alumno(alumnos,notas)
        write_alumnos(frame_alumnos(alumnos))
        write_notas(frame_notas(notas))
        pass
    elif opcion == 4: # modificar notas
        os.system("cls")
        setter_notas(notas)
        write_notas(frame_notas(notas))
        pass
    elif opcion == 5:#reporte curso
        os.system("cls")
        report_curso(alumnos,notas)
        pass
    elif opcion == 6:#reporte alumno
        os.system("cls")
        report_alumno(alumnos,notas)
        pass
    elif opcion == 7:#salir
        os.system("cls")
        break
    else:
        pass





