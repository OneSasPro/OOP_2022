# Подключение библиотек
import pygame
from pygame.draw import *
from random import randint

pygame.init()

# Задаём цвета
RED = (204, 0, 0)
BLUE = (0, 0, 204)
YELLOW = (255, 255, 0)
GREEN = (0, 204, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
# Кортеж из цветов
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
# Предварительный выбор координат и радиуса 3ёх шариков
# Координаты x и y + радиус 1ого шарика
x1 = randint(100, 700)
y1 = randint(100, 500)
r1 = randint(30, 50)
# Координаты x и y + радиус 2ого шарика
x2 = randint(100, 700)
y2 = randint(100, 500)
r2 = randint(30, 50)
# Координаты x и y + радиус 3ого шарика
x3 = randint(100, 700)
y3 = randint(100, 500)
r3 = randint(30, 50)
# Предвариательный выбор цвета каждого из шариков
color_1 = COLORS[randint(0, 5)]
color_2 = COLORS[randint(0, 5)]
color_3 = COLORS[randint(0, 5)]

FPS = 40
# Размеры поля
size = width, height = 900, 600
screen = pygame.display.set_mode(size)

pygame.display.update()
clock = pygame.time.Clock()
# Параметр ускорения шариков, помогающий правильно отрисовывать физику отталкивания от стен
ACCELERATION = 0.01


# Функция определения координат курсора в игровом поле
def mouse_pos():
    global position, position_x, position_y
    position = pygame.mouse.get_pos()
    position_x = position[0]
    position_y = position[1]


# Определим каждый из шариков, как отдельный объект через класс
class Ball:
    # Определим параметры шарика
    def __init__(self, x, y, radius):
        self.radius = radius
        self.x = x
        self.y = y
        self.velocity_y = 10
        self.velocity_x = 10
        self.counter = 0

    # Нарисуем шарик в игровом поле
    def draw(self, color1):
        circle(screen, color1, (self.x, self.y), self.radius)

    # Шарик должен двигаться
    def move(self):
        # Физика движения шарика по игровому полю
        self.velocity_y += ACCELERATION
        self.velocity_x += ACCELERATION
        self.y += self.velocity_y
        self.x += self.velocity_x
        # Если шарик достигает краёв игрового поля, то он отталкивается от них на основе координат своего центра +
        # радиус
        if self.y + self.radius >= 600 or self.y - self.radius <= 0:
            self.velocity_y = -self.velocity_y
        if self.x + self.radius >= 900 or self.x - self.radius <= 0:
            self.velocity_x = -self.velocity_x

    # Функция определения попадания курсора мыши по шарику
    def click(self, counter):
        # Чем меньше шарик, тем больше очков даётся за попадание по нему
        # Решение основано на формуле круга x^2 + y^2 = r^2   =>   r = sqrt(x^2 + y^2)
        if self.radius >= 45 and (self.radius > ((position_x - self.x) ** 2 + (position_y - self.y) ** 2) ** 0.5):
            self.counter += 1
            print("Click!")
        elif 45 > self.radius >= 40 and (self.radius > ((position_x - self.x) ** 2 + (position_y - self.y) ** 2) ** 0.5):
            self.counter += 2
            print("Click!")
        elif 40 > self.radius >= 30 and (self.radius > ((position_x - self.x) ** 2 + (position_y - self.y) ** 2) ** 0.5):
            self.counter += 3
            print("Click!")
        else:
            print("You missed!")
        print("Your score is", self.counter)
        counter += self.counter
        return counter


# Головная функция, функция игры
def game():
    # Определяем 3 шарика со своими ранее заданными параметрами
    ball_one = Ball(x1, y1, r1)
    ball_two = Ball(x2, y2, r2)
    ball_three = Ball(x3, y3, r3)
    counter = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            # Когда кликаем мышкой, то:
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Берем позицию курсора
                mouse_pos()
                # Подставляем в каждую функцию шарика для опрделения позиции курсора в игровом поле относительно шариква
                # При попадании в шарик добавляем пользователю очки :)
                # При промахе оповещаем пользователе о его неудаче :(
                ball_one.click(counter)
                ball_two.click(counter)
                ball_three.click(counter)
                print("________________________________") # Разделение для удобства и красоты

        # Движение шариков
        ball_one.move()
        ball_two.move()
        ball_three.move()
        # Заполняем серым цветом игровое поле
        screen.fill((32, 32, 32))
        ball_one.draw(color_1)
        ball_two.draw(color_2)
        ball_three.draw(color_3)
        pygame.display.update()
        clock.tick(FPS)

game()
pygame.quit()
