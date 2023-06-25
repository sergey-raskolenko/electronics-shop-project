from src.item import Item

class KeyboardLanguages:
    """
    Миксик-класс для смены раскладки клавиатуры
    """
    def __init__(self, name: str, price: float, quantity: int):
        self.__language = "EN"
        super().__init__(name, price, quantity)

    @property
    def language(self):
        """Геттер для расклдаки клавиатуры"""
        return self.__language

    def change_lang(self):
        """
        Изменяет раскладку клавиатуры
        """
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self

class KeyBoard(KeyboardLanguages, Item):
    """
    Класс для создания экземпляра 'Клавиатура'
    """
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
