from estado_ventanilla import EstadoVentanilla

class Cerrada(EstadoVentanilla):

    def atiende(self,persona):
        print("Ventanilla Cerrada!")