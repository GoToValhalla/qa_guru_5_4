import random
import math

def test_greeting():
    """
    Напишите программу, которая выводит на экран приветствие.
    """
    name = "Анна"
    age = 25
    # TODO Сформируйте нужную строку
    output = f"Привет, {name}! Тебе {age} лет."
    print(output)
    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."

def test_rectangle():
        """
        Напишите программу, которая берет длину и ширину прямоугольника
        и считает его периметр и площадь.
        """
        a = 10
        b = 20
        # TODO сосчитайте периметр
        perimeter = 2 * (a + b)
        print(perimeter)
        assert perimeter == 60

        # TODO сосчитайте площадь
        area = a * b
        print(area)
        assert area ==  200

def test_circle():
        """
        Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
        Используйте константу PI
        """
        r = 23
        # TODO сосчитайте площадь
        area = math.pi * r ** 2
        print(area)
        assert area == 1661.9025137490005
        # TODO сосчитайте длину окружности
        length = 2 * math.pi * r
        print(length)
        assert length == 144.51326206513048

def test_random_list():
        """
        Создайте список из 10 случайных чисел от 1 до 100 и отсортируйте его по возрастанию.
        """
        # TODO создайте список
        l = [random.randint(1, 100) for _ in range(10)]
        l.sort()
        print(l)
        assert len(l) == 10
        assert l[0] < l[-1]

def test_unique_elements():
        """
        Удалите из списка все повторяющиеся элементы
        """
        l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
        l = list(set(l))
        l.sort()
        print(l)
        # TODO удалите повторяющиеся элементы
        assert isinstance(l, list)
        assert len(l) == 10
        assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_dicts():
        """
        Создайте словарь из двух списков.
        Используйте первый список как ключи, а второй - как значения.
        Выведите на экран все значения словаря.
        Подсказка: используй встроенную функцию zip.
        """
        first = ["a", "b", "c", "d", "e"]
        second = [1, 2, 3, 4, 5]
        # TODO создайте словарь
        d = dict(zip(first, second))
        print(f'\nЗначение словаря: {d.values()}')
        assert isinstance(d, dict)
        assert len(d) == 5