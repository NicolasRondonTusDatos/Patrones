import time
class Creature:
    def __init__(self, name, health, hunger, happiness):
        self.name = name
        self.health = health
        self.hunger = hunger
        self.happiness = happiness

    def feed(self):
        self.hunger -= 10
        self.happiness += 5

    def play(self):
        self.happiness += 10

    def check_status(self):
        print(f"{self.name}: Salud: {self.health}, Hambre: {self.hunger}, Felicidad: {self.happiness}")

start_time = time.time()

for i in range(100000):
    Creature("Criatura Prototipo", 100, 50, 50)

end_time = time.time()
total_time = end_time - start_time
print(f"Tiempo total de ejecución: {total_time} segundos")