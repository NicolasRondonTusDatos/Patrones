from abc import ABC, abstractmethod
import random


class Creature(ABC):

    def __init__(self):
        self.health = 20

    @abstractmethod
    def describe(self):
        pass

    @abstractmethod
    def special_ability(self):
        pass

    @abstractmethod
    def encounter_challenge(self, choice):
        pass

    @abstractmethod
    def list_abilities(self):
        pass


class CreatureCreator(ABC):
    @abstractmethod
    def create_creature(self):
        pass


class Dragon(Creature):
    def __init__(self):
        super().__init__()

    def describe(self):
        return "Un poderoso dragón con alas majestuosas."

    def special_ability(self):
        return "Sopla fuego."

    def list_abilities(self):
        return ["volar", "fuego", "sabiduria"]

    def encounter_challenge(self, choice):
        if choice in self.list_abilities():
            return random.randint(0, 9)  # Daño aleatorio entre 1 y 7
        else:
            return 0  # Sin daño si la elección no es válida


class Unicorn(Creature):
    def __init__(self):
        super().__init__()

    def describe(self):
        return "Un unicornio mágico con un cuerno brillante."

    def special_ability(self):
        return "Puede curar con su cuerno."

    def list_abilities(self):
        return ["brillar", "correr", "viento"]

    def encounter_challenge(self, choice):
        if choice in self.list_abilities():
            return random.randint(0, 13)  # Daño aleatorio entre 1 y 7
        else:
            return 0  # Sin daño si la elección no es válida


class DragonCreator(CreatureCreator):
    def create_creature(self):
        return Dragon()


class UnicornCreator(CreatureCreator):
    def create_creature(self):
        return Unicorn()


def game():
    creatures = []

    for i in range(2):
        while True:
            choice = input(f"Jugador {i + 1}, elige tu criatura (Dragón o Unicornio): ").lower()
            if choice == "dragon":
                creature = DragonCreator().create_creature()
                break
            elif choice == "unicornio":
                creature = UnicornCreator().create_creature()
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
            # El otro jugador recibe el daño
            other_player = 1 - i
            creatures[other_player].health -= damage
            print(
                f"Jugador {i + 1} ataca con {player_choice}, causando {damage} de daño. Salud del oponente ahora es {creatures[other_player].health}\n")
            if creatures[other_player].health <= 0:
                print(f"¡Jugador {i + 1} gana el juego!")
                return

        round += 1
    print("El juego ha terminado.")


if __name__ == "__main__":
    game()
