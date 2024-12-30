class Personaje:
    def __init__(self, nombre, poder, velocidad):
        self.nombre = nombre
        self.poder = poder
        self.velocidad = velocidad
    
    def mostrar_datos(self):
        return f'Nombre: {self.nombre}, Poder: {self.poder}, Velocidad: {self.velocidad}'
    
    def __add__(self, otro):
        nuevo_nombre = f"{self.nombre}-{otro.nombre}"
        nuevo_poder = self.poder + otro.poder
        nueva_velocidad = self.velocidad + otro.velocidad
        return Personaje(nuevo_nombre, nuevo_poder, nueva_velocidad)


def crear_personaje(personajes):
    nombre = input("Ingrese el nombre del personaje: ")
    while any(p.nombre == nombre for p in personajes):
        nombre = input("Este nombre ya está en uso, ingrese otro: ")
    poder = int(input("Ingrese la cantidad de poder: "))
    velocidad = int(input("Ingrese la velocidad de movimiento: "))
    print("Creando personaje...")
    nuevo_personaje = Personaje(nombre, poder, velocidad)
    print("Personaje creado con éxito")
    return nuevo_personaje


def fusionar(personajes):
    if len(personajes) < 2:
        print("No hay suficientes personajes para fusionar.")
        return None
    print("Seleccione los personajes a fusionar:")
    for i, personaje in enumerate(personajes, start=1):
        print(f'{i}. {personaje.mostrar_datos()}')
    char1 = int(input('Elija el número del primer personaje que desea fusionar: ')) - 1
    char2 = int(input('Elija el número del segundo personaje que desea fusionar: ')) - 1
    if char1 < 0 or char2 < 0 or char1 >= len(personajes) or char2 >= len(personajes) or char1 == char2:
        print("Selección inválida.")
        return None
    nuevo_nombre = input("Ingrese el nombre del nuevo personaje: ")
    while any(p.nombre == nuevo_nombre for p in personajes):
        nuevo_nombre = input("Ingrese otro nombre para el nuevo personaje, ya que este ya existe: ")
    nuevo_personaje = personajes[char1] + personajes[char2]
    nuevo_personaje.nombre = nuevo_nombre
    return nuevo_personaje

def opciones():
    salir = False
    personajes = []
    while not salir:
            opcion = int(input("Seleccione la opción que desee:\n 1. Crear nuevo personaje\n 2. Listar personajes\n 3. Fusionar personajes\n 4. Salir\n"))
            if opcion == 1:
                nuevo_personaje = crear_personaje(personajes)
                personajes.append(nuevo_personaje)
            elif opcion == 2:
                if not personajes:
                    print("No hay personajes creados.")
                else:
                    for i, personaje in enumerate(personajes, start=1):
                        print(f'{i}. {personaje.mostrar_datos()}')
            elif opcion == 3:
                fusionado = fusionar(personajes)
                if fusionado:
                    personajes.append(fusionado)
            elif opcion == 4:
                print("Saliendo...")
                salir = True
            else:
                print("Opción inválida.")


def main():
    opciones()

main()


