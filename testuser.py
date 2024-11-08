class User:
    def __init__(self, user_id: int, name: str):
        self.__user_id = user_id  # Защищенный атрибут
        self.__name = name  # Защищенный атрибут
        self.__access_level = 'user'  # Уровень доступа для обычных пользователей

    def get_user_id(self) -> int:
        return self.__user_id

    def get_name(self) -> str:
        return self.__name

    def get_access_level(self) -> str:
        return self.__access_level

    def set_name(self, name: str):
        self.__name = name


class Admin(User):
    def __init__(self, user_id: int, name: str):
        super().__init__(user_id, name)
        self.__access_level = 'admin'  # Уровень доступа для администраторов
        self.__users = []  # Список пользователей

    def add_user(self, user: User):
        if isinstance(user, User):
            self.__users.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Невозможно добавить пользователя. Объект не является экземпляром User.")

    def remove_user(self, user_id: int):
        user_to_remove = next((user for user in self.__users if user.get_user_id() == user_id), None)
        if user_to_remove:
            self.__users.remove(user_to_remove)
            print(f"Пользователь {user_to_remove.get_name()} удален.")
        else:
            print("Пользователь не найден.")

    def list_users(self):
        if not self.__users:
            print("Нет пользователей в системе.")
        else:
            print("Список пользователей:")
            for user in self.__users:
                print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")

# Пример использования
if __name__ == "__main__":
    admin = Admin(1, "Администратор")
    
    user1 = User(2, "Сотрудник 1")
    user2 = User(3, "Сотрудник 2")
    
    admin.add_user(user1)
    admin.add_user(user2)
    
    admin.list_users()
    
    admin.remove_user(2)
    
    admin.list_users()