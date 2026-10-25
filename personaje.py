from abc import ABC, abstractmethod
class Personaje(ABC):
    
    def __init__(self, nombre, vida, ataque, defensa):
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        if not 0 <= vida <= 100:
            raise ValueError("La vida debe estar entre 0 y 100.")
        if ataque <= 0:
            raise ValueError("El ataque debe ser positivo.")
        if defensa < 0:
            raise ValueError("La defensa no puede ser negativa.")
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    
    
    def calcular_danio(self):
        return self.ataque
    
    def recibir_danio(self, cantidad):
        
        if cantidad < 0:
            return
        
        self.vida -= cantidad
        
        if self.vida < 0:
            self.vida = 0
        return self.vida
    @abstractmethod   
    ### estoy trabaando con este  
    def atacar(self, enemigo):
        pass
        
    def mostrar_estado(self):
        print(f"Personaje: {self.nombre} | Vida: {self.vida} HP | Ataque: {self.ataque} | Defensa: {self.defensa}")

    def esta_vivo(self):
        return self.vida > 0
    

class Guerrero(Personaje):
    def __init__ (self, nombre, vida, ataque, defensa):
        super().__init__(nombre, vida, ataque, defensa)
    def atacar(self, enemigo):
        daño = max(0, self.calcular_danio() * 1.20 - enemigo.defensa)
        enemigo.recibir_danio(daño)

class Arquero(Personaje):
    def __init__ (self, nombre, vida, ataque, defensa):
            super().__init__(nombre, vida, ataque, defensa)
    def atacar(self, enemigo):
        daño_base = max(0, self.calcular_danio() - enemigo.defensa)
        if daño_base > 0:
            daño_final = daño_base * 2
        else:
            daño_final = 0
        enemigo.recibir_danio(daño_final)

class Mago(Personaje):
    def __init__ (self, nombre, vida, ataque, defensa):
            super().__init__(nombre, vida, ataque, defensa)
    def atacar(self, enemigo):
        daño = self.calcular_danio()
        enemigo.recibir_danio(daño)
class Combate:
    def __init__ (self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.rondas = 0
    def mostrar_estado(self):
        self.p1.mostrar_estado()
        self.p2.mostrar_estado()

    def iniciar(self):
        while self.p1.esta_vivo() and self.p2.esta_vivo():
            self.p1.atacar(self.p2)
            self.rondas += 1
            print(f"Ronda #{self.rondas}")
            self.mostrar_estado()

            if not self.p2.esta_vivo():
                print(f"{self.p1.nombre} ganó en {self.rondas} rondas")
                return
            self.p2.atacar(self.p1)
            self.rondas += 1
            print(f"Ronda {self.rondas}:")
            self.mostrar_estado()
            if not self.p1.esta_vivo():
                print(f"{self.p2.nombre} ganó en {self.rondas} rondas")
                return
        
    def cambiar_turno(self, turno_actual):
        if turno_actual == self.p1:
            turno_actual = self.p2
        else:
            turno_actual = self.p1
        print(f"Turno de: {turno_actual.nombre}")
    def verificar_ganador(self):
        if self.p1.esta_vivo() and not self.p2.esta_vivo():
            return self.p1.nombre
        elif self.p2.esta_vivo() and not self.p1.esta_vivo():
            return self.p2.nombre
        else:
            return "Empate"
    def mostrar_resultado(self):
        ganador = self.verificar_ganador()
        if ganador == self.p1.nombre:
            print(f"El ganador de la partida es {self.p1.nombre}")
        elif ganador == self.p2.nombre:
            print(f"El ganador de la partida es {self.p2.nombre}")
        else:
            print(f"Hubo empate")

guerrero1 = Guerrero("Ruki", 100, 40, 30)
mago1 = Mago("Magis", 100, 20, 20)
guerrero1.atacar(mago1)
mago1.mostrar_estado()
mago1.atacar(guerrero1)
guerrero1.mostrar_estado()
pelea = Combate(guerrero1, mago1)
pelea.iniciar()
