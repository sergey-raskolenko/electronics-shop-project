import os
import csv

class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        if args:
            self.message = args[0]
        else:
            self.message = "InstantiateCSVError: Файл поврежден"

        def __str__(self):
            return f"{self.message}"


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    filename = "items.csv"
    filename_path_csv = os.path.join(os.path.dirname(__file__), filename)
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        """
        Возвращает строку с инфорацией об экземпляре для разработчика
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Возвращает строку с информацией об экземпляре для пользователя
        """
        return f'{self.name}'

    def __add__(self, other) -> int:
        """
        Возвращает сложенное количество двух объектов, если они принадлежат классу Item или дочернему классу
        :param other:
        :return quantity:
        """
        if isinstance(other, Item):
            quantity = self.quantity + other.quantity
            return quantity
        else:
            raise ValueError("Правый операнд должен быть объектом класса Item или дочерних ему классов")

    @property
    def name(self):
        """
        Возвращает значение атрибута name
        """
        return self.__name

    @name.setter
    def name(self, value):
        """
        Устанавливает значение атрибута name
        """
        if isinstance(value, str) and 0<len(value)<10:
            self.__name = value
        else:
            raise Exception("Длина наименования товара превышает 10 символов.")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price*self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price*Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """
        Класс-метод, инициализирующий экземпляры класса `Item` данными из файла .csv
        """
        try:
            with open(cls.filename_path_csv, newline='') as filecsv:
                reader = csv.DictReader(filecsv)
                for row in reader:
                    if list(row.keys()) != ['name', 'price', 'quantity']:
                        raise InstantiateCSVError(f"InstantiateCSVError: Файл {cls.filename} поврежден")
                    elif not row.get('name') or not row.get('price') or not row.get('quantity'):
                        raise InstantiateCSVError(f"InstantiateCSVError: Файл {cls.filename} поврежден")
                    elif row['name'] == '' or row['price'] == '' or row['quantity'] == '':
                        raise InstantiateCSVError(f"InstantiateCSVError: Файл {cls.filename} поврежден")
                    else:
                        cls(name=row['name'], price=row['price'], quantity=row['quantity'])
        except FileNotFoundError:
            print(FileNotFoundError(f"FileNotFoundError: Отсутствует файл {cls.filename}"))
        except InstantiateCSVError as error:
            print(error)

    @staticmethod
    def string_to_number(value: str):
        """
        Cтатический метод, возвращающий число из числа-строки
        """
        return int(float(value))
