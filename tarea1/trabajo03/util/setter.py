"""modificacion de objetos"""

from os import system
from tarea1.trabajo03.model.Alumnos import *


def setter_alumno(lista_a, lista_n): # modificar o eliminar alumno
    indice = int()
    system("cls")
    print("Modificacion de Alumno".center(100, "-"))
    rutcambio = input("ingrese el rut del estudiante a modificar: ")
    for i in range(len(lista_a)):
        encontrado = False
        if rutcambio == lista_a[i].get_rut():
            encontrado = True
            indice = i
            break
        else:
            pass
    if encontrado:
        while True:
            print("Ingrese accion a realizar "
                  "\n[0]modificar "
                  "\n[1]eliminar")
            opcion = input("opcion: ")
            if opcion == "0":
                system("cls")
                print("Para modificar al alumno ingrese el nombre y apellido de el mismo")
                nombre = input("ingrese el nombre: ")
                apellido = input("ingrese el apellido: ")
                lista_a[indice].set_nombre(nombre)
                lista_a[indice].set_apellido(apellido)
                input("alumno modificado correctamente")
                break
            elif opcion == "1":
                system("cls")
                print("Esta seguro de eliminar al alumno {0}".format(lista_a[indice].get_nombre()))
                pas = input("[0] Si\n"
                                "[1] No\n"
                                ": ")
                if pas == "0":
                    for x in range(len(lista_n)):
                        if rutcambio == lista_n[x].get_rut():
                            del lista_n[x]
                            break
                        else:
                            pass
                    del lista_a[indice]
                    input("alumno eliminado junto a todas sus notas")
                    break
                else:
                    pass
            else:
                print("ingrese una opcion valida")
    else:
        ultima = input("alumno no encontrado\n"
                       "***enter para intentar denuevo\n"
                       "***ingrese un numero para salir de modificacion")
        if ultima == "":
            setter_alumno(lista_a, lista_n)
        else:
            pass


def setter_notas(lista_n): # modificar notas
    system("cls")
    print("modificacion de notas".center(100, "-"))
    rutcambio = input("ingrese el rut del estudiante: ")
    for i in range(len(lista_n)):
        encontrado = False
        if rutcambio == lista_n[i].get_rut():
            encontrado = True
            indice = i
            break
        else:
            pass
    if encontrado == True:
        while True:
            nota = input("\n\n"
                             "ingrese el numero de la nota que desea modificar\n"
                             "**recuerde que cada alumno tiene 5 notas enumeradas de 1 a 5\n"
                             ": ")
            if nota == "1":
                system("cls")
                print("modificar nota 1".center(100, "="))
                print("la nota 1 del alumno rut:{0} es un {1}".format(lista_n[indice].get_rut(),
                                                                      lista_n[indice].get_nota1()))
                change = float(input("ingrese la nota nueva: "))
                if 1 <= change <= 7:
                    pass
                else:
                    change = 0.0
                lista_n[indice].set_nota1(change)
                input("nota modificada correctamente")
                break
            elif nota == "2":
                system("cls")
                print("modificar nota 2".center(100, "="))
                print("la nota 2 del alumno rut:{0} es un {1}".format(lista_n[indice].get_rut(),
                                                                      lista_n[indice].get_nota2()))
                change = float(input("ingrese la nota nueva: "))
                if 1 <= change <= 7:
                    pass
                else:
                    change = 0.0
                lista_n[indice].set_nota2(change)
                input("nota modificada correctamente")
                break
            elif nota == "3":
                system("cls")
                print("modificar nota 3".center(100, "="))
                print("la nota 3 del alumno rut:{0} es un {1}".format(lista_n[indice].get_rut(),
                                                                      lista_n[indice].get_nota3()))
                change = float(input("ingrese la nota nueva: "))
                if 1 <= change <= 7:
                    pass
                else:
                    change = 0.0
                lista_n[indice].set_nota3(change)
                input("nota modificada correctamente")
                break
            elif nota == "4":
                system("cls")
                print("modificar nota 4".center(100, "="))
                print("la nota 4 del alumno rut:{0} es un {1}".format(lista_n[indice].get_rut(),
                                                                      lista_n[indice].get_nota4()))
                change = float(input("ingrese la nota nueva: "))
                if 1 <= change <= 7:
                    pass
                else:
                    change = 0.0
                lista_n[indice].set_nota4(change)
                input("nota modificada correctamente")
                break
            elif nota == "5":
                system("cls")
                print("modificar nota 5".center(100, "="))
                print("la nota 5 del alumno rut:{0} es un {1}".format(lista_n[indice].get_rut(),
                                                                      lista_n[indice].get_nota5()))
                change = float(input("ingrese la nota nueva: "))
                if 1 <= change <= 7:
                    pass
                else:
                    change = 0.0
                lista_n[indice].set_nota5(change)
                input("nota modificada correctamente")
                break
            else:
                input("ingrese nota valida")

        pass
    else:
        ultima = input("alumno no encontrado\n"
                       "***enter para intentar denuevo\n"
                       "***ingrese un numero para salir de modificacion")
        if ultima == "":
            setter_notas(lista_n)
        else:
            pass


