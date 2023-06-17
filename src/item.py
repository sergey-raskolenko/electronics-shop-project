import os
import csv
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    filename_csv = os.path.join(os.path.dirname(__file__),"items.csv")
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
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

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
        with open(Item.filename_csv, newline='') as filecsv:
            reader = csv.DictReader(filecsv)
            for row in reader:
                Item(name=row['name'], price=row['price'], quantity=row['quantity'])

    @staticmethod
    def string_to_number(value: str):
        """
        Cтатический метод, возвращающий число из числа-строки
        """
        return int(float(value))
