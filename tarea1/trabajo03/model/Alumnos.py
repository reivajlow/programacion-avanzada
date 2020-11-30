# Clase alumnos

class Alumnos:
    __rut = str()
    nombre = str()
    apellido = str()

    def __init__(self, rut, nombre, apellido):
        self.__rut = rut
        self.nombre = nombre
        self.apellido = apellido
        pass
# estructura de datos
    def frame(self):
        return {
            'Rut': self.__rut,
            'Nombre': self.nombre,
            'Apellido': self.apellido}
# get datos
    def get_rut(self):
        return self.__rut
    def get_nombre(self):
        return self.nombre
    def get_apellido(self):
        return self.apellido

    #setear datos
    def set_nombre(self,nombre):
        self.nombre = nombre
    def set_apellido(self,apellido):
        self.apellido = apellido
