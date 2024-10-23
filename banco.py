from ventanilla import Ventanilla


class Banco():
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion= direccion
        self.ventanilla = Ventanilla()

    def atende(self,persona):
        print(f"{persona.nombre} ingresa a la fila")
        self.ventanilla.atende(persona)

    def suspende_ventanilla(self):
        self.ventanilla.suspendete()
    

    def cerra_ventanilla(self):
        self.ventanilla.cerrate()
    

    def abrite_ventanilla(self):
        self.ventanilla.abrite()
    