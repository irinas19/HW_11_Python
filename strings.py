# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)

# Добавьте к задачам 1 и 2 строки документации для классов.
import time


class Strings(str):

    def __new__(cls, value: str, name: str):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.created_at = time.time()
        return instance

    def __str__(self):
        return self + " " + f'{self.name} {self.created_at}'


if __name__ == '__main__':
    mystr = Strings('САМА строка', 'доп. параметр')
    print(mystr)
