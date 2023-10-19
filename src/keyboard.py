from src.item import Item


class KeyboardMixin:
    ''' миксин для раскладки '''
    layout = {'RU': 'EN', 'EN': 'RU'}

    def __init__(self, name: str, price: float, quantity: int):
        ''' миксин вызывает базовый класс '''
        super().__init__(name, price, quantity)
        self.__lang = 'EN'

    def change_lang(self):
        ''' сменить раскладку '''
        self.__lang = KeyboardMixin.layout.get(self.__lang, self.__lang)

    @property
    def layout_lang(self):
        ''' язык раскладки '''
        return self.__lang


class Keyboard(KeyboardMixin, Item):
    ''' клавиатура '''

    def __init__(self, name: str, price: float, quantity: int):
        ''' конструктор с миксином '''
        super().__init__(name, price, quantity)

    @property
    def language(self):
        ''' язык раскладки из миксина '''
        return self.layout_lang
