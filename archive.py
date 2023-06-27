# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра

# Добавьте к задачам 1 и 2 строки документации для классов.

# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.


class Archive:
    numbers = []
    values = []

    def __new__(cls, number: int, value: str):
        instance = super().__new__(cls)
        cls.numbers.append(number)
        cls.values.append(value)
        return instance

    def __init__(self, number: int, value: str):
        self.number = number
        self.value = value

    def __repr__(self):

        return f'Archive({self.number}, "{self.value}")'

    def __str__(self):
        return f'Номер: {self.number}, Значение: "{self.value}"'


if __name__ == '__main__':
    a_1 = Archive(1, "Один")
    a_2 = Archive(2, "Два")
    print(f'{a_1.numbers} {a_1.values}')
    print(f'{a_2.numbers} {a_2.values}')
    a_3 = Archive(3, "Три")
    print(f'{a_3.numbers} {a_3.values}')
    help(a_1)
    print(a_1.__repr__())
    print(f'{a_1 = }')
    print(a_1)