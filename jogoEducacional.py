import pygame
import random
import string
import time
from funcoes import Logs

'''nome = str(input('Digite o seu nome: ')).upper().strip()
email = str(input('Digite seu e-mail: ')).upper().strip()
Logs(nome, email)'''

pygame.init()

# Estabelece o tamanho da tela
largura = 800
altura = 600
display = pygame.display.set_mode((largura, altura))
fps = pygame.time.Clock()
pygame.display.set_caption('Jogo Educacional')

# cores
black = (0, 0, 0)
white = (255, 255, 255)

# sons e imagens
somIntro = pygame.mixer.Sound('assets/intro.mp3')
fundo = pygame.image.load('assets/floresta.jpg')
leao = pygame.image.load('assets/leao.png')
icone = pygame.image.load("assets/lionIcon.png")



def jogo():
    pygame.mixer.music.load('assets/intro.mp3')
    pygame.mixer.music.play(-1)
    posicaoLeaoX = largura * 0.45
    posicaoLeaoY = altura * 0.8
    movimentoX = 0
    movimentoY = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movimentoX = -10
                elif event.key == pygame.K_RIGHT:
                    movimentoX = 10
                elif event.key == pygame.K_UP:
                    movimentoY = -10
                elif event.key == pygame.K_DOWN:
                    movimentoY = 10
            if event.type == pygame.KEYUP:
                movimentoX = 0
                movimentoY = 0

        pygame.mixer.Sound.play(somIntro)
        display.fill(white)
        display.blit(fundo, (0,0))
        posicaoLeaoX = posicaoLeaoX + movimentoX
        if posicaoLeaoX < 0:
            posicaoLeaoX = 0
        elif posicaoLeaoX > 680:
            posicaoLeaoX = 680
        posicaoLeaoY = posicaoLeaoY + movimentoY
        if posicaoLeaoY < 0:
            posicaoLeaoY = 0
        elif posicaoLeaoY > 480:
            posicaoLeaoY = 480
        
        display.blit(leao, (posicaoLeaoX, posicaoLeaoY))

        #display.blit(textoTela, (50, 700))
        pygame.display.update()
        fps.tick(60)

jogo()
