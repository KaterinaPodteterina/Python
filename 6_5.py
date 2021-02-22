class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f" Начало рисования\n  {self.title} \n {'*' * 30}")

class Pen(Stationary):
    def draw(self):
        print(f"\033[32m Начало рисования\n {self.title}\n {'*' * 30}")


class Pencil(Stationary):
    def draw(self):
        print(f"\033[33m Начало рисования\n {self.title}\n {'*' * 30}")


class Marker(Stationary):
    def draw(self):
        print(f"\033[31m Начало рисования\n {self.title}\n {'*' * 30}")

my_draw = Stationary ("Мой рисунок")
my_draw.draw()
my_draw_pen = Pen("Мой рисунок ручкой")
my_draw_pen.draw()
my_draw_pencil = Pencil("Мой рисунок карандаш")
my_draw_pencil.draw()
my_draw_marker = Marker("Мой рисунок маркер")
my_draw_marker.draw()