# generadores de reportes
from os import system
from tarea1.trabajo03.util.dataframe import unir_data, summary
import csv


# reporte curso
def report_curso(alumnos, notas):
    data = unir_data(alumnos, notas)
    mean_curso = list()
    for i in notas:
        mean_alumno = i.mean()
        if type(mean_alumno) == type(1.1):
            mean_curso.append(mean_alumno)
        else:
            pass
        pass
    if mean_curso:
        mean_curso = float("{0:.1f}".format(sum(mean_curso) / len(notas)))
    else:
        mean_curso = "no existe"
    system("cls")
    print("REPORTE DE CURSO".center(100, "="))
    print(data)
    print("Promedio de curso:{0}".format(str(mean_curso)))
    opcion = input("\n"
                       "[1] Salir\n"
                       "[2] Exportar a CSV\n"
                       "opcion: ")
    if opcion == "2":
        myFile = open("report/reporte_curso.csv", 'w')
        myFile.close()
        data.to_csv("report/reporte_curso.csv", index=False)
        adjunto = [[" ", " ", " ", " ", " ", " ", " ", "Promedio de curso:", str(mean_curso)]]
        myFile = open("report/reporte_curso.csv", 'a')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(adjunto)
        myFile.close()
        input("Reporte exportado correctamente")
    else:
        pass


# reporte por alumno
def report_alumno(alumnos, notas):
    # busqueda promedio curso
    mean_curso = list()
    for i in notas:
        mean_alumno = i.mean()
        if type(mean_alumno) == type(1.1):
            mean_curso.append(mean_alumno)
        else:
            pass
        pass
    if mean_curso:
        mean_curso = float("{0:.1f}".format(sum(mean_curso) / len(notas)))
    else:
        mean_curso = "no existe"
    # busqueda alumno y sus notas
    print("Reporte por alumno".center(100, "="))
    rut = input("ingrese el rut del alumno: ")
    alumno = 0
    nota = 0  # no supe instanciar objetos
    encontrado = bool
    for a in alumnos:
        if a.get_rut() == rut:
            alumno = a
            encontrado = True
            break
        else:
            encontrado = False
    if encontrado == True:
        for n in notas:
            if n.get_rut() == rut:
                nota = n
                break
            else:
                pass
            pass
        # mostrar report y opcion de exportar
        data = summary(alumno, nota)
        print(data)
        print("Promedio de curso:{0}    Estado del alumno:{1}".format(str(mean_curso), nota.estado()))
        opcion = input("\n"
                           "[1] Salir\n"
                           "[2] Exportar a CSV\n"
                           "opcion: ")
        if opcion == "2":
            myFile = open("report/reporte_alumno_{0}.csv".format(alumno.get_rut()), 'w')
            myFile.close()
            data.to_csv("report/reporte_alumno_{0}.csv".format(alumno.get_rut()), index=False)
            adjunto = [
                [" ", " ", " ", " ", " ", "Promedio de curso:", str(mean_curso), "Estado del alumno:", nota.estado()]]
            myFile = open("report/reporte_alumno_{0}.csv".format(alumno.get_rut()), 'a')
            with myFile:
                writer = csv.writer(myFile)
                writer.writerows(adjunto)
            myFile.close()
            input("Reporte exportado correctamente")

    else:
        ultima = input("alumno no encontrado\n"
                       "***enter para intentar denuevo\n"
                       "***ingrese un numero para salir de modificacion")
        if ultima == "":
            report_alumno(alumnos, notas)
