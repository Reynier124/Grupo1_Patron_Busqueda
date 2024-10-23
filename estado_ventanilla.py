from abc import ABC, abstractmethod

class EstadoVentanilla(ABC):
    
    @abstractmethod
    def atiende(self, persona):
        pass
    