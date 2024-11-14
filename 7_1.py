# Создание класса Product с атрибутами (название, вес, категория)
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    # Формирование строки информации о продукте
    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

# Создание класса Shop с атрибутом .txt
class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    # Чтение файла .txt с возвращением содержимого в виде строки
    def get_products(self):
        # Обработка исключений
        try:
            with open(self.__file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return ""  # Если файл не найден, возвращаем пустую строку

    # Добавление новых продуктов в файл без дублирования
    def add(self, *products):
        existing_products = self.get_products().strip().split('\n')
        existing_products_set = {p.split(', ')[0] for p in existing_products if p}  # Множество названий
                                                                                    # существующих продуктов

        # Цикл проверки на наличие аналога в списке с выводом сообщения об этом
        for product in products:
            if product.name in existing_products_set:
                print(f"Продукт: {product} - уже есть в магазине")
            else:
                with open(self.__file_name, 'a') as file:
                    file.write(str(product) + '\n')


# Пример работы программы
s1 = Shop()
p1 = Product('Картофель', 150, 'Овощи')
p2 = Product('Кефир', 1.5, 'Молокопродукты')
p3 = Product('Пепси-кола', 1.5, 'Газированный шампунь')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())