from ex.model.Cliente import *


class Banco:

    def __init__(self):
        self.cliente1 = Cliente("leonel")
        self.cliente2 = Cliente("thomas")

    def operacion(self):
        self.cliente1.depositar(500)
        self.cliente2.giro(100)

    def total(self):
        total = self.cliente2.get_monto() + self.cliente1.get_monto()
        print("El total de dinero en el banco es: ", total)
