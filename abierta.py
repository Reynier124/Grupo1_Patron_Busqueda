from estado_ventanilla import EstadoVentanilla

class Abierta(EstadoVentanilla):

    def atiende(self, persona):
        print(f"Estoy atentiendo a: {persona.nombre}")