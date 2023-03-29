import pygame
from pygame.draw import *
pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))
screen.fill((255, 255, 255))
pygame.draw.circle(screen, (0, 0, 0), (300, 300), 102)
pygame.draw.circle(screen, (255, 255, 0), (300, 300), 100)
pygame.draw.circle(screen, (0, 0, 0), (260, 270), 25)
pygame.draw.circle(screen, (0, 0, 0), (340, 270), 20)
pygame.draw.circle(screen, (255, 0, 0), (340, 270), 18)
pygame.draw.circle(screen, (255, 0, 0), (260, 270), 23)
pygame.draw.circle(screen, (0, 0, 0), (260, 270), 10)
pygame.draw.circle(screen, (0, 0, 0), (340, 270), 10)
pygame.draw.polygon(screen, (0, 0, 0), [[260,350], [260, 360], [340, 360], [340, 350]])
pygame.draw.polygon(screen, (0, 0, 0), [[200, 180], [295, 265], [290, 270], [205, 185]])
pygame.draw.polygon(screen, (0, 0, 0), [[400, 180], [295, 265], [300, 270], [395, 185]])
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

