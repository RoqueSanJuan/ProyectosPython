from random import randint


class Persona:
    Id = 0  # Variable de clase estatica , todas las instancias la comparten

    def __init__(self):
        Persona.Id += 1  # Sumo 1 a la variable de clase que es estatica
        self.Id = Persona.Id
        self.Vivo = True
        self.Inf = False
        self.Curado = False
        self.DiasInf = 0
        self.Edad = randint(0, 90)

    def __str__(self):  # para poder usar el print de un objeto
        cadena = str(self.Id) + " Edad: " + str(self.Edad) + " " + str(self.Vivo) + " " + str(self.DiasInf) + " " + str(
            self.Inf)
        return cadena

    def muere(self):
        self.Vivo = False
        self.Curado = False
        self.Inf = False
        self.DiasInf = 0

    def curado(self):
        self.Curado = True
        self.DiasInf = 0
        self.Inf = False

    def contagiado(self):
        self.Inf = True


"""m1 = Mundo()
m1.mostrarPersonas()
m1.insertarContagiado()
m1.insertarContagiado()
m1.insertarContagiado()
m1.insertarContagiado()
m1.mostrarDatos()
entrada = "1"
while(entrada != "0"):
    entrada = input()
    m1.nuevoDia()
    m1.mostrarDatos()
"""
#m1.mostrarPersonas()


