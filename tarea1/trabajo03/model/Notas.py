# clase de notas
class Notas:
    __rut = str()
    nota1 = float()
    nota2 = float()
    nota3 = float()
    nota4 = float()
    nota5 = float()

    def __init__(self, rut, nota1, nota2, nota3, nota4, nota5):
        self.__rut = rut
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        self.nota5 = nota5

    def get_rut(self):
        return self.__rut

    def get_nota1(self):
        return self.nota1

    def get_nota2(self):
        return self.nota2

    def get_nota3(self):
        return self.nota3

    def get_nota4(self):
        return self.nota4

    def get_nota5(self):
        return self.nota5

    # crear dataframe

    def frame(self):
        return {
            'Rut': self.__rut,
            'Nota 1': self.nota1,
            'Nota 2': self.nota2,
            'Nota 3': self.nota3,
            'Nota 4': self.nota4,
            'Nota 5': self.nota5,
        }

    def frame_mean(self): #data frame rut y promedio
        cantidad = int()
        suma = [float(self.nota1), float(self.nota2), float(self.nota3), float(self.nota4), float(self.nota5)]
        for i in suma:
            if 1 <= i <= 7:
                cantidad += 1
            else:
                del i
        if cantidad != 0:
            promedio = float("{0:.1f}".format(sum(suma) / cantidad))
        else:
            promedio = "no tiene"
            pass
        return {
            'Rut': self.__rut,
            "Promedio": promedio,
        }


    # setear datos
    def set_nota1(self, nota):
        self.nota1 = nota

    def set_nota2(self, nota):
        self.nota2 = nota

    def set_nota3(self, nota):
        self.nota3 = nota

    def set_nota4(self, nota):
        self.nota4 = nota

    def set_nota5(self, nota):
        self.nota5 = nota

    # promedio
    def mean(self):
        cantidad = int()
        suma = [float(self.nota1), float(self.nota2), float(self.nota3), float(self.nota4), float(self.nota5)]
        for i in suma:
            if 1 <= i <= 7:
                cantidad += 1
            else:
                del i
        if cantidad != 0:
            promedio = float("{0:.1f}".format(sum(suma) / cantidad))
        else:
            promedio = "no tiene"
        return promedio

    def estado(self): #estado del alumno segun promedio
        cantidad = int()
        suma = [float(self.nota1), float(self.nota2), float(self.nota3), float(self.nota4), float(self.nota5)]
        for i in suma:
            if 1 <= i <= 7:
                cantidad += 1
            else:
                del i
        if cantidad != 0:
            promedio = float("{0:.1f}".format(sum(suma) / cantidad))
        else:
            promedio = "no tiene"

        if 1 <= promedio < 4:
            estado = "REPROBADO"
        elif 4<= promedio <=7:
            estado = "APROBADO"
        else:
            estado = "sin notas"
        return estado

