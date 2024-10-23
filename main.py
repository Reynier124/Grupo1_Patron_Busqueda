from persona import Persona
from banco import Banco

p1 = Persona("Francisco","Pasquier",21)
p2 = Persona("Pilar","Grosso",71)
p3 = Persona("Leonel","Funes",60)
p4 = Persona("Cristian","Guzman",21)

banco = Banco("Santander", "Juan Domingo Peron 571")
banco.atende(p1)

banco.suspende_ventanilla()

banco.atende(p2)
banco.atende(p3)

banco.cerra_ventanilla()
banco.atende(p4)