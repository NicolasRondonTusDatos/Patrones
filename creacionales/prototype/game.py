import copy

# Clase prototipo para las criaturas
class CreaturePrototype:
    def clone(self):
        return copy.deepcopy(self)

# Clase concreta para las criaturas
class Creature(CreaturePrototype):
    def __init__(self, name, health, hunger, happiness, special_ability=None):
        self.name = name
        self.health = health
        self.hunger = hunger
        self.happiness = happiness
        self.level = 1
        self.experience = 0
        self.special_ability = special_ability

    def feed(self):
        self.hunger -= 10
        self.happiness += 5
        self.experience += 2  # Gana experiencia al alimentarse
        print(f"Has alimentado a {self.name}.")
        self.check_status()  # Mostrar el estado después de alimentar
        self.level_up()

    def play(self):
        self.happiness += 10
        self.experience += 5  # Gana más experiencia al jugar
        print(f"Has jugado con {self.name}.")
        self.check_status()  # Mostrar el estado después de jugar
        self.level_up()


    def level_up(self):
        if self.experience >= 100:  # Umbral de experiencia para subir de nivel
            self.level += 1
            self.experience = 0
            # Mejora las habilidades o desbloquea nuevas aquí
            self.health += 10
            self.happiness += 5
            print(f"{self.name} ha subido al nivel {self.level}!")

    def check_status(self):
        print(f"{self.name}: Salud: {self.health}, Hambre: {self.hunger}, Felicidad: {self.happiness}, Nivel: {self.level}, Experiencia: {self.experience}")


# Función principal del juego
def main():
    print("¡Bienvenido al juego de simulación de vida de criaturas!")

    creatures = []
    num_creatures = int(input("¿Cuántas criaturas deseas crear?: "))

    # Crear un prototipo de criatura
    creature_prototype = Creature("Criatura Prototipo", 100, 50, 50)


    for i in range(num_creatures):
        creature_name = input(f"Ingresa el nombre de la criatura {i + 1}: ")
        health = int(input("Ingresa la salud inicial: "))
        hunger = int(input("Ingresa el nivel de hambre inicial: "))
        happiness = int(input("Ingresa el nivel de felicidad inicial: "))
        special_ability = input("Elige una habilidad especial (opcional): ")

        new_creature = creature_prototype.clone()
        new_creature.name = creature_name
        new_creature.health = health
        new_creature.hunger = hunger
        new_creature.happiness = happiness
        new_creature.special_ability = special_ability
        creatures.append(new_creature)

    while True:
        print("\n¿Qué acción deseas realizar?")
        print("1. Alimentar")
        print("2. Jugar")
        print("3. Ver estado de una criatura")
        print("4. Ver estado de todas las criaturas")
        print("5. Salir")

        choice = input("Selecciona una opción (1/2/3/4/5): ")

        if choice == "1":
            for i, creature in enumerate(creatures):
                print(f"{i + 1}. {creature.name}")
            index = int(input("Selecciona una criatura para alimentar: ")) - 1
            if 0 <= index < len(creatures):
                creatures[index].feed()
                print(f"Has alimentado a {creatures[index].name}.")
            else:
                print("Índice no válido.")
        elif choice == "2":
            for i, creature in enumerate(creatures):
                print(f"{i + 1}. {creature.name}")
            index = int(input("Selecciona una criatura para jugar: ")) - 1
            if 0 <= index < len(creatures):
                creatures[index].play()
                print(f"Has jugado con {creatures[index].name}.")
            else:
                print("Índice no válido.")
        elif choice == "3":
            for i, creature in enumerate(creatures):
                print(f"{i + 1}. {creature.name}")
            index = int(input("Selecciona una criatura para ver su estado: ")) - 1
            if 0 <= index < len(creatures):
                creatures[index].check_status()
            else:
                print("Índice no válido.")
        elif choice == "4":
            for i, creature in enumerate(creatures):
                print(f"Criatura {i + 1}:")
                creatures[i].check_status()
        elif choice == "5":
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")


if __name__ == "__main__":
    main()
