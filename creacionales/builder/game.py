from abc import ABC, abstractmethod
import random


# Clase abstracta Creature
class Creature(ABC):
    def __init__(self, health, abilities, description):
        self.health = health
        self.abilities = abilities
        self.description = description

    def describe(self):
        return self.description

    def special_ability(self):
        pass

    def encounter_challenge(self, choice):
        if choice in self.abilities:
            return random.randint(1, 7)
        else:
            return 0

    def list_abilities(self):
        return self.abilities


# Interfaz del Builder
class CreatureBuilder(ABC):
    @abstractmethod
    def set_health(self, health):
        pass

    @abstractmethod
    def add_ability(self, ability):
        pass

    @abstractmethod
    def set_description(self, description):
        pass

    @abstractmethod
    def build(self):
        pass


# Builder concreto para Dragon
class DragonBuilder(CreatureBuilder):
    def __init__(self):
        self.health = 20
        self.abilities = []
        self.description = ""

    def set_health(self, health):
        self.health = health
        return self

    def add_ability(self, ability):
        self.abilities.append(ability)
        return self

    def set_description(self, description):
        self.description = description
        return self

    def build(self):
        return Dragon(self.health, self.abilities, self.description)


# Builder concreto para Unicornio
class UnicornBuilder(CreatureBuilder):
    def __init__(self):
        self.health = 20
        self.abilities = []
        self.description = ""

    def set_health(self, health):
        self.health = health
        return self

    def add_ability(self, ability):
        self.abilities.append(ability)
        return self

    def set_description(self, description):
        self.description = description
        return self

    def build(self):
        return Unicorn(self.health, self.abilities, self.description)


# Clase Dragon
class Dragon(Creature):
    def special_ability(self):
        return "Sopla fuego."


# Clase Unicornio
class Unicorn(Creature):
    def special_ability(self):
        return "Puede curar con su cuerno."


# Clase Director
class CreatureDirector:
    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder: CreatureBuilder):
        self._builder = builder

    def build_custom_dragon(self, health, abilities):
        self.builder.set_health(health)
        for ability in abilities:
            self.builder.add_ability(ability)
        self.builder.set_description("Un poderoso dragón con alas majestuosas.")

    def build_custom_unicorn(self, health, abilities):
        self.builder.set_health(health)
        for ability in abilities:
            self.builder.add_ability(ability)
        self.builder.set_description("Un unicornio mágico con un cuerno brillante.")




# Función principal del juego
def game():
    creature = None
    director = CreatureDirector()
    creatures = []

    for i in range(2):
        while True:
            choice = input(f"Jugador {i + 1}, elige tu criatura (Dragón o Unicornio): ").lower()
            try:
                health_input = int(input(f"Jugador {i + 1}, elige un número del 15 al 20: "))
                ability_input = input(f"Añade tu propio poder: ")
            except ValueError:
                print("Por favor, ingresa un número válido para la salud.")
                continue

            if choice == "dragon":
                builder = DragonBuilder()
                director.builder = builder
                director.build_custom_dragon(0, ["bola de fuego", "aliento negro", "arañazo"])  # Construye el dragón base
                builder.set_health(health_input).add_ability(ability_input)  # Personalización
                creature = builder.build()
                break
            elif choice == "unicornio":
                builder = UnicornBuilder()
                director.builder = builder
                director.build_custom_unicorn(0,["salto", "carrera", "magia"])  # Construye el unicornio base
                builder.set_health(health_input).add_ability(ability_input)  # Personalización
                creature = builder.build()
                break
            else:
                print("Elección no válida. Por favor, elige 'Dragón' o 'Unicornio'.")

        creatures.append(creature)
        print(creature.describe())
        print(f"Habilidad especial: {creature.special_ability()}")
        print(f"Habilidades disponibles: {', '.join(creature.list_abilities())}\n")

    # Ciclo del juego
    round = 1
    while all(c.health > 0 for c in creatures):
        print(f"Ronda {round}\n")
        for i, creature in enumerate(creatures):
            print(f"Turno del Jugador {i + 1} - Salud: {creature.health}")
            print(f"Habilidades disponibles: {', '.join(creature.list_abilities())}")
            player_choice = input("Elige tu ataque: ")
            damage = creature.encounter_challenge(player_choice)
            other_player = 1 - i
            creatures[other_player].health -= damage
            print(
                f"Jugador {i + 1} ataca con {player_choice}, causando {damage} de daño. Salud del oponente ahora es "
                f"{creatures[other_player].health}\n")
            if creatures[other_player].health <= 0:
                print(f"¡Jugador {i + 1} gana el juego!")
                return

        round += 1
    print("El juego ha terminado.")


if __name__ == "__main__":
    game()
