from src.item import Item
class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """
        Создание экземпляра класса Phone

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество сим-карт.
        """
        super().__init__(name, price, quantity)
        if isinstance(number_of_sim, int) and number_of_sim > 0:
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __repr__(self):
        """
        Возвращает строку с инфорацией об экземпляре для разработчика
        """
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"


    def __str__(self):
        """
        Возвращает строку с информацией об экземпляре для пользователя
        """
        return f"{self.name}"

    @property
    def number_of_sim(self):
        """
        Возвращает значение атрибута number_of_sim
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        """
        Устанавливает значение атрибута number_of_sim
        """
        if isinstance(value, int) and value > 0:
            self.__number_of_sim = value
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
