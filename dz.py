# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях. Напишите к ним
# классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода. Например
# нельзя создавать прямоугольник со сторонами
# отрицательной длины.

# Семинар 3 Задача 6
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного 
# слова был один пробел между ним и номером строки.

class NotTextExc(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = 'NotTextException was raised. That is all.'
    def __str__(self):
        print('calling str')
        return self.message

message = input("\n6. Введите желаемый текст через пробел (текст не может содержать ничего кроме букв!)\n: ")
co = 1
for line in message.split():
    spy = sum(1 for ch in line if not ch.isalpha())
    print(co, ". ", line)
    if spy != 0:
        raise NotTextExc('Посторонние символы при вводе текста!')
    co += 1

# Семинар 10 Задача 2
# Создайте класс прямоугольник. Класс должен принимать длину и ширину при создании
# экземпляра. У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.

class SubZero(Exception):
    def __init__(self, *args):
        if args:
            match len(args):
                case 1:
                    self.message = args[0]
                case 2:
                    self.message = f'{args[0]}, {args[1]}'
        else:
            self.message = 'SubZeroException was raised. That is all.'
    def __str__(self):
        print('calling int')
        return self.message



class Rectan:
    "Класс обработки двух переменных и вычисления площади и периметра четырёхсторонней фигуры"
    def __new__(cls, lng, wdt, figur = ''):
        "Получение переменных от пользователя, создание новой фигуры"
        worker = super().__new__(cls)
        worker.lng = int(lng)
        worker.wdt = int(wdt)
        if lng == wdt:
            worker.figur = figur + 'Квадрат'
        else:
            worker.figur = figur + 'Прямоугольник'
        return worker
    def area(worker):
        "Вычисление площади фигуры"
        area = worker.lng * worker.wdt
        return area
    def perimet(worker):
        "Вычисление периметра фигуры"
        perimet = 2 * (worker.lng + worker.wdt)
        return perimet
    def __str__(self):
        "Вывод результата"
        return f'Площадь = {self.area()}\nПериметр = {self.perimet()}'

paramets = input("\n5. Введите желаемую длину и ширину прямоугольника через пробел (значения должны быть больше 0)\n: ")
paramets = paramets.split()
spy = sum(1 for dig in paramets if int(dig) < 0)
if spy != 0:
    raise SubZero()
ex = Rectan(paramets[0], paramets[-1])
print(f'\nПример 1 (длина: {ex.lng}, ширина: {ex.wdt}, {ex.figur}):\n{ex}')