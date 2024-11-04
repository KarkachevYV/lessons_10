class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        """Добавляет товар в ассортимент."""
        self.items[item_name] = price

    def remove_item(self, item_name):
        """Удаляет товар из ассортимента."""
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        """Получает цену товара по его названию. Если товар отсутствует, возвращает None."""
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """Обновляет цену товара."""
        if item_name in self.items:
            self.items[item_name] = new_price


# Создаем несколько объектов класса Store
store1 = Store("Магазин 1", "Улица 1, дом 1")
store2 = Store("Магазин 2", "Улица 2, дом 2")
store3 = Store("Магазин 3", "Улица 3, дом 3")

# Добавляем товары в магазины
store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)

store2.add_item("апельсины", 1.0)
store2.add_item("груши", 0.85)

store3.add_item("киви", 1.2)
store3.add_item("вишня", 2.0)

# Тестируем методы на примере store1
print(f"{store1.name} имеет следующий ассортимент товаров: {store1.items}")

# Добавим новый товар
store1.add_item("персики", 1.5)
print(f"Товары после добавления персиков: {store1.items}")

# Обновим цену на бананы
store1.update_price("бананы", 0.8)
print(f"Товары после обновления цены на бананы: {store1.items}")

# Удалим товар
store1.remove_item("яблоки")
print(f"Ассотримент товаров после удаления яблок: {store1.items}")

# Запросим цену на товар
price_of_bananas = store1.get_price("бананы")
print(f"Цена бананов: {price_of_bananas}")

# Запросим цену на отсутствующий товар
price_of_apples = store1.get_price("яблоки")
print(f"Цена яблок: {price_of_apples}")