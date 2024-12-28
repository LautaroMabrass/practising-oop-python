"""
Herencias - Ejercicio 2

Ejercicio de herencia y uso de super:

Crear un sistema para una escuela. En este sistema, vamos a tener dos clases principales: Persona y Estudiante. La clase Persona tendrá los atributos de nombre y edad y un método que imprima el nombre y la edad de la persona. La clase Estudiante heredará de la clase Persona y también tendrá un atributo adicional: grado y un método que imprima el grado del estudiante.
"""

class persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def datos(self):
        return f'Datos: nombre = {self.nombre}, edad = {self.edad}'

class estudiante(persona):
    def __init__(self,nombre,edad,grado):
        persona.__init__(self,nombre,edad)
        self.grado = grado
    
    def dato_estudiante(self):
        print(f'{super().datos()}, grado = {self.grado}')

lautaro = estudiante("lautaro",18,"sexto")
lautaro.dato_estudiante()