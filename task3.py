# 3. Применить написанный логгер к приложению из любого предыдущего д/з.

import os
from task1 import logger

# Задание:
# Доработать класс FlatIterator в коде ниже.
# Должен получиться итератор, который принимает список списков и возвращает их плоское представление,
# т. е. последовательность, состоящую из вложенных элементов.
# Функция test в коде ниже также должна отработать без ошибок.

class FlatIterator:


    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.list_iter = iter(self.list_of_list)  # определяем итератор для списка
        self.inside_list = []  # определяем вложенный внутренний список для добавления элементов
        self.cursor = -1  # смещаем курсор за границу списка
        return self

    path = 'logs/main.log'
    if os.path.exists(path):
        with open('logs/main.log', 'a') as file:
            data = "\n New logs in task №3: \n"
            file.write(data)
    @logger
    def __next__(self):
        self.cursor += 1
        if len(self.inside_list) == self.cursor:  # сравниваем внутренний список и перебор курсором по списку
            self.inside_list = None
            self.cursor = 0
            while not self.inside_list:  # если списки закончились, то stop iteration
                self.inside_list = next(self.list_iter)  # если пустой, то берем следующий внутренний список
        return self.inside_list[self.cursor]

def test_3():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

if __name__ == '__main__':
        test_3()