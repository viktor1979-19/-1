first = 'Мама мыла раму'
second = 'Рамена мало было'

function = map(lambda x, y: x == y, first, second)

print(list(function))

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open('example.txt', 'a', encoding='UTF-8') as file:
            for data in data_set:
                file.write(str(data) + '\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())