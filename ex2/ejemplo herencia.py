
class auto:

    def __init__(self,rueda,puerta,techo):
        self.rueda = rueda
        self.puerta = puerta
        self.techo = techo

        """
        set
        get
        ...
        ...
        ...
        """

class camioneta(auto):

    def __init__(self, rueda, puerta, techo, ventana):
        super().__init__(rueda,puerta,techo)
        self.ventana = ventana
