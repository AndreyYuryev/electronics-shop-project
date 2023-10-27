from src.item import Item, InstantiateCSVError

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv('itm.csv')
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv('src/item.csv')
    # InstantiateCSVError: Файл item.csv поврежден
