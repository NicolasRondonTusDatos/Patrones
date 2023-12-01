import random

class ScoreboardSingleton:
    _instance = None
    _best_score = float('inf')  # Inicializado como infinito para asegurarse de que cualquier puntaje sea mejor

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ScoreboardSingleton, cls).__new__(cls)
        return cls._instance

    @property
    def best_score(self):
        return self._best_score

    def update_best_score(self, score):
        if score < self._best_score:
            self._best_score = score

class NumberGuessingGame:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

    def play(self):
        print("Bienvenido al Juego de Adivinanza de Números!")
        print("Intenta adivinar el número secreto entre 1 y 100.")

        while True:
            try:
                guess = int(input("Ingresa tu adivinanza: "))
                self.attempts += 1

                if guess < self.secret_number:
                    print("Demasiado bajo. Intenta de nuevo.")
                elif guess > self.secret_number:
                    print("Demasiado alto. Intenta de nuevo.")
                else:
                    print(f"Felicitaciones, adivinaste el número secreto {self.secret_number} en {self.attempts} intentos!")
                    scoreboard = ScoreboardSingleton()
                    scoreboard.update_best_score(self.attempts)
                    print(f"Mejor puntaje: {scoreboard.best_score}")
                    break

            except ValueError:
                print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    while True:
        game = NumberGuessingGame()
        game.play()
        play_again = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if play_again != "s":
            break
