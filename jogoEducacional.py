import pygame
import random
import string
import time
from funcoes import Logs

nome = str(input('Digite o seu nome: ')).upper().strip()
email = str(input('Digite seu e-mail: ')).upper().strip()
Logs(nome, email)

pygame.init()

# Estabelece o tamanho da tela
displayWidth = 800
displayHeight = 800
display = pygame.display.set_mode((displayWidth, displayHeight))
fps = pygame.time.Clock()
pygame.display.set_caption('Jogo Educacional')


# cores
black = (0, 0, 0)
white = (255, 255, 255)

# sons e imagens
somIntro = pygame.mixer.Sound('assets/intro.wav')
fundo = pygame.image.load('assets/schoolBackIntro.jpg')
leao = pygame.image.load('assets/leao.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                nome = nome[:-1]
            else:
                nome += event.unicode

    pygame.mixer.Sound.play(somIntro)
    display.fill(white)
    display.blit(fundo, (0,0))
    display.blit(leao, (320, 15))
    pygame.display.update()
    fps.tick(60)