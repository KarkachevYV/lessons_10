from datetime import datetime

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline  # Ожидается, что deadline будет в формате 'YYYY-MM-DD'
        self.completed = False  # Статус задачи по умолчанию - не выполнено

    def is_due(self):
        return datetime.strptime(self.deadline, '%Y-%m-%d') >= datetime.now()
    
    def mark_completed(self):
      self.completed = True

    def __str__(self):
      status = "Выполнено" if self.completed else "Не выполнено"
      return f"Задача: {self.description}, Срок: {self.deadline},  Статус: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)
    
    def mark_task_completed(self, index):
      if 0 <= index < len(self.tasks):
          self.tasks[index].mark_completed()
      else:
          print("Некорректный индекс задачи.")

    def get_current_tasks(self):
        return [task for task in self.tasks if task.is_due() and not task.completed]

    def show_current_tasks(self):
        current_tasks = self.get_current_tasks()
        if current_tasks:
            print("Не выполненные текущие задачи:")
            for task in current_tasks:
                print(task)
        else:
            print("Нет текущих задач.")

# Пример использования
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Купить молоко", "2024-11-03")
    manager.add_task("Сделать домашнее задание", "2024-11-11")
    manager.add_task("Отправить отчет", "2024-12-30")

    # Отметим вторую  задачу как выполненную
    manager.mark_task_completed(1)
    
    # Отметим как выполненную несуществующую задачу
    manager.mark_task_completed(3)

    # Показываем невыполненные текущие задачи
    manager.show_current_tasks()