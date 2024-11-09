from abc import ABC, abstractmethod

# Шаг 1: Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self, monster):
        pass
    
    @abstractmethod
    def name(self):
        pass

# Шаг 2: Конкретные типы оружия
class Sword(Weapon):
    def attack(self, monster):
        monster.health = 0  # Уничтожаем монстра
        return f" и наносит удар мечом !"

    def name(self):
        return "меч"

class Bow(Weapon):
    def attack(self, monster):
        monster.health -= 10  # Наносим урон монстру
        return f" и стреляя из лука лишь ранит Монстра! У него осталось {monster.health} здоровья."

    def name(self):
        return "лук"

# Шаг 3: Класс Fighter
class Fighter:
    def __init__(self, name, weapon: Weapon): 
        self.name = name
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self, monster):
        return self.weapon.attack(monster)

# Класс Monster
class Monster:
    def __init__(self, name, health): 
        self.name = name
        self.health = health

    def is_defeated(self):
        return self.health <= 0

# Шаг 4: Реализация боя
def battle(fighter: Fighter, monster: Monster):
    print(f"{fighter.name} выбирает {fighter.weapon.name()}.")
    attack_message = fighter.attack(monster)
    print(attack_message)
    if monster.is_defeated():
        print(f"Монстр {monster.name} побежден!")
        
    else:
        print(f"Монстр {monster.name} все еще в бою!")

# Пример использования
if __name__ == "__main__":
    # Создаем монстра с 20 единицами здоровья
    monster = Monster("Гоблин", 20)
    
    # Создаем бойца с луком
    fighter = Fighter("Артур", Bow())

    # Бой с луком
    battle(fighter, monster)

    # Изменим оружие на меч
    fighter.change_weapon(Sword())

    # Новый бой с мечом
    battle(fighter, monster)