from abc import ABC, abstractmethod
class Personaje(ABC):
    
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    
    
    def calcular_danio(self):
        return self.ataque
    
    def recibir_danio(self, cantidad):

      ###  daño final = max(0, self.ataque - defensa enemiga)
      #es posible qe tenga q duplicar este metodo en las otras clases de personake y asi poder colocar ataque de ese personae menos la defensa del enemigo.
        if cantidad < 0:
            return self.ataque
        
        self.vida -= cantidad
        
        if self.vida < 0:
            self.vida = 0
        return self.vida
    @abstractmethod    
    def atacar(self, enemigo):
        
        danio = self.calcular_danio()
        
        enemigo.recibir_danio(danio)
        
    def mostrar_estado(self):
        print(f"{self.nombre}: {self.vida} HP")

    def esta_vivo(self):
        return self.__vida > 0

guerrero = Personaje("Arthas", 100, 20, 30)
orco = Personaje("Grom", 80, 15, 30)

guerrero.atacar(orco)

orco.mostrar_estado()

orco.vida = -50000

orco.mostrar_estado()

orco.ataque = -300

orco.vida = "estoy muertito"

print(orco.vida)

#############################

guerrero = Personaje("Ruki", 100, 20, 30)
mago = Personaje("Magis", 100, 40, 20)
guerrero.atacar(mago)
mago.mostrar_estado()
mago.atacar(guerrero)
guerrero.mostrar_estado()

######################### Errores ###################################

#[Running] python -u "c:\Users\jireh\OneDrive\proyectos programación\Guardians of the Ancient Kingdom\pruebas.py"
#<bound method Personaje.mostrar_estado of <__main__.Personaje object at 0x0000028983F786E0>>

#Traceback (most recent call last):
 # File "c:\Users\jireh\OneDrive\proyectos programaci�n\Guardians of the Ancient Kingdom\pruebas.py", line 38, in <module>
   # personaje2 = Personaje("juancho", 100, 20, 40)
#TypeError: Can't instantiate abstract class Personaje without an implementation for abstract method 'atacar'

#Traceback (most recent call last):
  #File "c:\Users\jireh\OneDrive\proyectos programaci�n\Guardians of the Ancient Kingdom\pruebas.py", line 38, in <module>
   # guerrero = Personaje("Arthas", 100, 20)
#TypeError: Can't instantiate abstract class Personaje without an implementation for abstract method 'atacar'

#Traceback (most recent call last):
  #File "c:\Users\jireh\OneDrive\proyectos programaci�n\Guardians of the Ancient Kingdom\proyecto.py", line 102, in <module>
    #guerrero = Personaje("Ruki", 100, 20, 30)
#TypeError: Can't instantiate abstract class Personaje without an implementation for abstract method 'atacar'

#[Running] python -u "c:\Users\jireh\OneDrive\proyectos programación\Guardians of the Ancient Kingdom\proyecto.py"
#Magis: 100 HP
#Traceback (most recent call last):
 # File "c:\Users\jireh\OneDrive\proyectos programaci�n\Guardians of the Ancient Kingdom\proyecto.py", line 103, in <module>
  #  mago1.atacar(guerrero1)
  #  ~~~~~~~~~~~~^^^^^^^^^^^
  #File "c:\Users\jireh\OneDrive\proyectos programaci�n\Guardians of the Ancient Kingdom\proyecto.py", line 57, in atacar
   # da�o_base = max(0, self.calcular_danio - enemigo.defensa)
            #           ~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~
#TypeError: unsupported operand type(s) for -: 'method' and 'int'

#Traceback (most recent call last):
 # File "c:\Users\jireh\OneDrive\proyectos programaci�n\Guardians of the Ancient Kingdom\proyecto.py", line 102, in <module>
    #guerrero1.atacar(mago1)
#    ~~~~~~~~~~~~~~~~^^^^^^^
 # File "c:\Users\jireh\OneDrive\proyectos programaci�n\Guardians of the Ancient Kingdom\proyecto.py", line 45, in atacar
  #  enemigo.recibir_danio(da�o)
   # ~~~~~~~~~~~~~~~~~~~~~^^^^^^
  #File "c:\Users\jireh\OneDrive\proyectos programaci�n\Guardians of the Ancient Kingdom\proyecto.py", line 20, in recibir_danio
   # self.__vida -= cantidad
    #^^^^^^^^^^^
#AttributeError: 'Mago' object has no attribute '_Personaje__vida'

##empezó a funcionar porfin
#Magis: 96.0 HP
#Ruki: 60 HP

#[Running] python -u "c:\Users\jireh\OneDrive\proyectos programación\Guardians of the Ancient Kingdom\proyecto.py"
#Personaje: Magis | Vida: 96.0 HP | Ataque: 40 | Defensa: 20
#Personaje: Ruki | Vida: 60 HP | Ataque: 20 | Defensa: 30

#Traceback (most recent call last):
  #File "c:\Users\jireh\OneDrive\proyectos programaci�n\Guardians of the Ancient Kingdom\proyecto.py", line 106, in <module>
  #  guerrero1.iniciar()
 #   ^^^^^^^^^^^^^^^^^
#AttributeError: 'Guerrero' object has no attribute 'iniciar'

#TypeError: Combate.__init__() missing 2 required positional arguments: 'turno_actual' and 'rondas'

#TypeError: Combate.iniciar() missing 1 required positional argument: 'rondas'

#AttributeError: 'Combate' object has no attribute 'mostrar_estado'. Did you mean: 'mostrar_resultado'?

#TypeError: Combate.cambiar_turno() missing 1 required positional argument: 'turno_actual'


#Traceback (most recent call last):
  #File "c:\Users\jireh\OneDrive\proyectos programaci�n\Guardians of the Ancient Kingdom\proyecto.py", line 116, in <module>
    #pelea.iniciar()
    #~~~~~~~~~~~~~^^
  #File "c:\Users\jireh\OneDrive\proyectos programaci�n\Guardians of the Ancient Kingdom\proyecto.py", line 74, in iniciar
    #self.mostrar_estado()
    #^^^^^^^^^^^^^^^^^^^
#AttributeError: 'Combate' object has no attribute 'mostrar_estado'. Did you mean: 'mostrar_resultado'?

###[Done] exited with code=0 in 0.309 seconds