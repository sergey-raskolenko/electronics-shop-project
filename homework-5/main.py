from src.keyboard import KeyBoard

if __name__ == '__main__':
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"

    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"

    # Сделали RU -> EN -> RU
    # Разделил применение на две строки, т.к. метод второй метод не применяется к NoneType объекту
    kb.change_lang()
    kb.change_lang()
    assert str(kb.language) == "RU"

    kb.language = 'CH'
    # AttributeError: property 'language' of 'KeyBoard' object has no setter
