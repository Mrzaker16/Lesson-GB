class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return f'Запуск отрисовки {self.title}'

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)


    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки в режиме ручки'

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)


    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки в режиме карандаша'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки в режиме макера'


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())