import pygame
import random
import time
from funcoes import Logs

# Recebe o nome e e-mail do jogador e salva no log
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

def vogal():
    vogais = ['A', 'E', 'I', 'O', 'U']
    vogaisAleatoria = vogais[random.randint(0,4)]
    return vogaisAleatoria

def consoante():
    consoantes = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z']
    consoanteAleatoria = consoantes[random.randint(0, 18)]
    return consoanteAleatoria

def jogo():
    pygame.mixer.music.load('assets/intro.mp3')
    pygame.mixer.music.play(-1)
    posicaoLeaoX = largura * 0.45
    posicaoLeaoY = altura * 0.8
    movimentoX = 0
    movimentoY = 0
    vogalPosicaoX = largura * 0.45
    vogalPosicaoY = -30
    consoantePosicaoX = 700
    consoantePosicaoY = altura * 0.45
    velocidade = 5
    letraLargura = 75
    letraAltura = 75
    vogal()
    font = pygame.font.SysFont(None, 54)
    vogais = font.render(vogal(), True, black)
    consoantes = font.render(consoante(), True, black)

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

        # Pega posição do Leão e impede que cruze as bordas
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
        display.blit(vogais, ((vogalPosicaoX, vogalPosicaoY)))
        display.blit(consoantes, ((consoantePosicaoX, consoantePosicaoY)))
        vogalPosicaoY = vogalPosicaoY + velocidade
        consoantePosicaoX = consoantePosicaoX - velocidade

        if vogalPosicaoY > altura:
            vogal()
            vogais = font.render(vogal(), True, black)
            vogalPosicaoY = -30
            vogalPosicaoX = random.randrange(0, largura-50)

        if consoantePosicaoX < 0:
            consoante()
            consoantes = font.render(consoante(), True, black)
            consoantePosicaoX = 800
            consoantePosicaoY = random.randrange(0, altura-50)

        pygame.display.update()
        fps.tick(60)

jogo()
