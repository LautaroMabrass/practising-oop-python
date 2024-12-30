from abc import ABC, abstractmethod

class personajes(ABC):
    # Clase padre
    @abstractmethod
    def __init__(self, nombre, poder, habilidad):
        self._nombre = nombre 
        self.poder = poder
        self.habilidad = habilidad
    
    @abstractmethod
    def atacar(self):
        pass

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, new_name):
        self._nombre = new_name 
    
    def __add__(self, otro):
        nuevo_poder = (self.poder + otro.poder) ** 2
        if isinstance(self, magos) and isinstance(otro, magos):
            return magos("Elija nombre de fusion", nuevo_poder, f"{self.habilidad} + {otro.habilidad}")
        else:
            return brujo("Elija nombre de fusion", nuevo_poder, "Bolas de fuego")

class magos(personajes):
    # Posible personaje 1
    def __init__(self, nombre, poder, habilidad):
        super().__init__(nombre, poder, habilidad)
    
    def atacar(self):
        print(f'{self.habilidad}')

class arquero(personajes):
    # Posible personaje 2
    def __init__(self, nombre, poder, habilidad):
        super().__init__(nombre, poder, habilidad)
    
    def atacar(self):
        print(f'{self.habilidad}')

class brujo(personajes):
    # Fusión de arquero y mago
    def __init__(self, nombre, poder, habilidad):
        super().__init__(nombre, poder, habilidad)
    
    def atacar(self):
        print(f'{self.habilidad}')

# Instancias y pruebas
sonia = magos("Sonia", 500, "Bola de agua")
enrik = arquero("Enrik", 250, "Flecha de agua")
jinn = magos("Jinn", 150, "Bola de agua")

# Fusión de mago + arquero = brujo
witcher = sonia + enrik
print(witcher.nombre)  # Nombre original
witcher.atacar()
print(witcher.poder)

# Cambio de nombre
witcher.nombre = "Witcher"
print(witcher.nombre)  # Nuevo nombre

print('-' * 20)

# Fusión de mago + mago = mago
fizz = sonia + jinn
print(fizz.nombre)  # Nombre original
fizz.atacar()
print(fizz.poder)

# Cambio de nombre
fizz.nombre = "Fizz"
print(fizz.nombre)  # Nuevo nombre
