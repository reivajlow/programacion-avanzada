class Cliente:
    nombre = str()
    monto = int()

    def __init__(self, nombre):
        self.nombre = nombre
        self.monto = 0

    def depositar(self, monto):
        self.monto += monto  # self.monto = self.monto + monto


    def giro(self,monto):
        if monto < self.monto:
            self.monto -= monto


    def get_monto(self):
        return self.monto

