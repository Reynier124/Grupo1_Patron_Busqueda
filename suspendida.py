from estado_ventanilla import EstadoVentanilla

class Suspendida(EstadoVentanilla):

    def atiende(self, persona):
        if persona.edad > 65:
            print(f"Atentiendo a: {persona.nombre}")
        else:
            print("Espere 5 minutos por fa...")