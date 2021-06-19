import pygame
import random
import string
import time


pygame.init()

# Estabelece o tamanho da tela
displayWidth = 800
displayHeight = 600
display = pygame.display.set_mode((displayWidth, displayHeight))
fps = pygame.time.Clock()
pygame.display.set_caption('Jogo Educacional')

# cores
black = (0, 0, 0)
white = (255, 255, 255)

# sons e imagens
somIntro = pygame.mixer.Sound('assets/intro.wav')
meninaIntro = pygame.image.load('assets/meninaIntro.png')
meninoIntro = pygame.image.load('assets/meninoIntro.jpg')
fundo = pygame.image.load('assets/schoolBackIntro.jpg')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.mixer.Sound.play(somIntro)
    display.fill(white)
    display.blit(fundo, (0,0))
    pygame.display.update()
    fps.tick(60)