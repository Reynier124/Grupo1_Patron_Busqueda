from estado_ventanilla import EstadoVentanilla
from abierta import Abierta
from cerrada import Cerrada
from suspendida import Suspendida

class Ventanilla():
    def __init__(self):
        self.cajero = ""
        self.estado = Abierta()
    
    def suspendete(self):
        self.estado = Suspendida()
    
    def cerrate(self):
        self.estado = Cerrada()
    
    def abrite(self):
        self.estado = Abierta()
    
    def atende(self, persona):
        self.estado.atiende(persona)