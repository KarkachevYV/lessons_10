import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        # Генерируем случайное число от 1 до 5
        if random.randint(1, 5) == 1:  # Промах с вероятностью 5%
            print(f"{self.name} промахивается!")
            return  # Если промах, выходим из метода
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} уменьшая здоровье на {self.attack_power}!")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack(self.computer)
            print(f"{self.computer.name} здоровье: {self.computer.health}")
            if not self.computer.is_alive():
                print(f"{self.player.name} победил!")
                break
            
            self.computer.attack(self.player)
            print(f"{self.player.name} здоровье: {self.player.health}")
            if not self.player.is_alive():
                print(f"{self.computer.name} победил!")
                break


if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()