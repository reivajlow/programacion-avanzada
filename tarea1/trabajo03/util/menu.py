'''
menu principal
'''
from os import system

import keyboard #libreria que permite generar eventos a partir de teclas
"""requiere instalacion mediante pip"""

selected = 1 #variable para funciones de menu

def show_menu():
    global selected
    system("cls")
    print("\n" * 30)
    print("MENU PRINCIPAL")
    opciones = ["agregar alumnos", "mostrar alumnos y notas", "modificar alumnos", "modificar notas", "reporte de curso", "reporte de alumno","salir"]
    print("use las flechas para seleccionar una opcion:")
    for i in range(1,len(opciones)+1):
        print("{1} {0}. {3} {2}".format(i, ">" if selected == i else " ", "<" if selected == i else " ",opciones[i-1]))

def up():
    global selected
    if selected == 1:
        return
    selected -= 1
    show_menu()

def down():
    global selected
    if selected == 7:
        return
    selected += 1
    show_menu()

def menu():
    global selected
    show_menu()
    keyboard.add_hotkey('up', up) #evento flecha up
    keyboard.add_hotkey('down', down) #evento flecha down
    keyboard.wait("enter") #evento enter finalizar funcion
    return selected

def menu2(): #menu clasico
    while True:
        system("cls")

        print("MENU PRINCIPAL".center(100,"="))
        opciones = ["agregar alumnos",
                    "mostrar alumnos y notas",
                    "modificar alumnos",
                    "modificar notas",
                    "reporte de curso",
                    "reporte de alumno",
                    "salir"]
        for i in range(1,len(opciones)+1):
            print(" {0}. {1} ".format(i, opciones[i-1]))
        opcion = int(input("ingrese una opcion: "))
        if 1 <= opcion <= 7:
            return opcion
        else:
            input("ingrese una opcion valida")

def descripcion() -> object: #inicio de programa
    system("cls")
    input("Bienvenido a programa de mantencion de alumnos\n"
          "tener en consideracion:\n"
          "                      -Notas con punto como separador decimal\n"
          "                       ejemplo: 4.5\n"
          "                      -Al ingresar una nota fuera de rango sera considerada como 0.0\n"
          "                       y esta no influira en el calculo de promedio\n"
          "\n"
          "Gracias por usar nuestro programa ;)\n"
          "***ENTER PARA CONTINUAR")