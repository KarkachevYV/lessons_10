import json

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Подклассы должны реализовывать этот метод")

    def eat(self):
        return f"{self.name} ест."


class Bird(Animal):
    def make_sound(self):
        return "Щебечет!"


class Mammal(Animal):
    def make_sound(self):
        return "Ревёт!"


class Reptile(Animal):
    def make_sound(self):
        return "Шипит!"


def animal_sound(animals):
    for animal in animals:
        print(f"{animal.name}  стильно: {animal.make_sound()}")


class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.serialize(), file)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.deserialize(data)

    def serialize(self):
        return {
            'animals': [{'name': animal.name, 'age': animal.age, 'type': type(animal).__name__} for animal in self.animals],
            'employees': [employee.serialize() for employee in self.employees]
        }

    def deserialize(self, data):
        self.animals = []
        for animal_data in data['animals']:
            if animal_data['type'] == 'Bird':
                animal = Bird(animal_data['name'], animal_data['age'])
            elif animal_data['type'] == 'Mammal':
                animal = Mammal(animal_data['name'], animal_data['age'])
            elif animal_data['type'] == 'Reptile':
                animal = Reptile(animal_data['name'], animal_data['age'])
            self.animals.append(animal)

        self.employees = [ZooKeeper.deserialize(emp) if emp['type'] == 'ZooKeeper' else Veterinarian.deserialize(emp) for emp in data['employees']]


class Employee:
    def __init__(self, name):
        self.name = name

    def serialize(self):
        raise NotImplementedError("Подклассы должны реализовывать этот метод")


class ZooKeeper(Employee):
    def feed_animal(self, animal):
        return f"{self.name} кормит {animal.name}."

    def serialize(self):
        return {'name': self.name, 'type': 'ZooKeeper'}

    @classmethod
    def deserialize(cls, data):
        return cls(data['name'])


class Veterinarian(Employee):
    def heal_animal(self, animal):
        return f"{self.name} лечит {animal.name}."

    def serialize(self):
        return {'name': self.name, 'type': 'Veterinarian'}

    @classmethod
    def deserialize(cls, data):
        return cls(data['name'])


# Пример использования
if __name__ == "__main__":
    zoo = Zoo()

    # Добавим животных
    zoo.add_animal(Bird("Parrot", 2))
    zoo.add_animal(Mammal("Lion", 5))
    zoo.add_animal(Reptile("Snake", 3))

    # Добавим сотрудников
    zookeeper = ZooKeeper("John")
    veterinarian = Veterinarian("Sara")
    zoo.add_employee(zookeeper)
    zoo.add_employee(veterinarian)


    # Пример полиморфизма
    animal_sound(zoo.animals)

    # Выводим действия сотрудников
    print(zookeeper.feed_animal(zoo.animals[0]))  # Кормим попугая
    print(veterinarian.heal_animal(zoo.animals[1]))  # Лечим льва

    # Сохраним состояние зоопарка
    zoo.save_to_file('info_zoo.txt')
   
    # Создадим новый зоопарк и загрузим из файла
    print("Выводим информацию из файла")
    new_zoo = Zoo()
    new_zoo.load_from_file('info_zoo.txt')
    animal_sound(new_zoo.animals)
    print(veterinarian.heal_animal(zoo.animals[2]))  # Лечим змею
    print(zoo.animals[2].eat())
