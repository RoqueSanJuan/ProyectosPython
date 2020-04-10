from random import randint

from Persona import Persona


class Mundo:

    def __init__(self):
        self.diasTranscurridos = 0
        self.poblacion = 100000
        self.contagiados = 0
        self.curados = 0
        self.ContporPer = 3
        self.arPer = []
        self.muertos = 0
        for f in range(self.poblacion):
                p = Persona()
                self.arPer.append(p)

    def insertarContagiado(self):
        p = Persona()
        p.contagiado()
        self.arPer.append(p)
        print("Se ingresa a una persona contagiada: " + str(p.Id))
        self.poblacion += 1
        self.contagiados += 1

    def NuevoContagio(self):
        # La probabilidad de contagio la calculo haciendo el valor de contagio de virus que es 3 por persona
        # dividido en los 14 dias que asumo que es el tiempo que contagia una persona me da 0.2
        # Si 3 es el 100% 0.2 me da 7 ---> Asumo que ese es el valor de prob de contagio diario
        probContDia = randint(1,100)
        if probContDia <= 10:
            perRand = randint(0 , self.poblacion-1)                #Busco una persona random
            if not self.arPer[perRand].Inf:
                if not self.arPer[perRand].Curado:
                    self.arPer[perRand].contagiado()
                    self.contagiados += 1
                    #print("Se contagio al individuo : " + str( self.arPer[perRand].Id))

    def nuevoDia(self):
        self.diasTranscurridos += 1
        for persona in self.arPer:
            if persona.Inf:
                self.NuevoContagio()
                persona.DiasInf += 1
                self.proMuerte(persona)
                if persona.DiasInf > 14:
                    persona.curado()
                    self.curados += 1
                    self.contagiados -= 1

    def mostrarDatos(self):
        datos = str("Poblacion: " + str(self.poblacion) + " Dia: " + str(self.diasTranscurridos)+ " Contagiados: " + str(self.contagiados) + " Muertos: " + str(self.muertos) + " Curados: " + str(self.curados))
        print(datos)

    def mostrarPersonas(self):
        for personas in range(len(self.arPer)):
            print(self.arPer[personas])

    def proMuerte(self, persona):
            if persona.Inf:
                probmuerte = randint(0, 10000)
                if persona.Edad > 60:
                    if probmuerte <= 3:
                        persona.muere()
                        self.arPer.remove(persona)
                        self.poblacion -= 1
                        self.muertos += 1
                        self.contagiados -= 1
                if persona.Edad < 60:
                    if probmuerte <= 1:
                        persona.muere()
                        self.arPer.remove(persona)
                        self.poblacion -= 1
                        self.muertos += 1
                        self.contagiados -= 1