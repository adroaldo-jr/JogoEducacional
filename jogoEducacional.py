import pygame
import random
import time
from funcoes import Logs, Vogal, Consoante

# Recebe o nome e e-mail do jogador e salva no log
nome = str(input('Digite o seu nome: ')).upper().strip()
email = str(input('Digite seu e-mail: ')).upper().strip()
Logs(nome, email)

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
pygame.display.set_caption("Jogo Educacional - Coma apenas as vogais")
pygame.display.set_icon(icone)

def text_objects(texto, fonte):
    textSurface = fonte.render(texto, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    fonte = pygame.font.Font("freesansbold.ttf", 30)
    TextSurf, TextRect = text_objects(text, fonte)
    TextRect.center = ((largura/2), (altura/2))
    display.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(3)
    jogo()

def dead(vogais):
    message_display("Comeu consoante e engasgou. Comeu "+ str(vogais) +" vogais!")

def jogo():
    pygame.mixer.music.load('assets/intro.mp3')
    pygame.mixer.music.play(-1)
    posicaoLeaoX = largura * 0.45
    posicaoLeaoY = altura * 0.8
    leaoLargura = 120
    movimentoX = 0
    movimentoY = 0
    vogalPosicaoX = largura * 0.45
    vogalPosicaoY = -30
    consoantePosicaoX = largura * 0.60
    consoantePosicaoY = -30
    velocidade = 5
    letraLargura = 40
    letraAltura = 40

    # Renderiza a vogal e a consoante escolhidas
    font = pygame.font.SysFont(None, 54)
    vogais = font.render(Vogal(), True, black)
    consoantes = font.render(Consoante(), True, black)
    contador = 0

    while True:
        # Bloco de código para pegar comandos do usuário
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movimentoX = -10
                elif event.key == pygame.K_RIGHT:
                    movimentoX = 10
            if event.type == pygame.KEYUP:
                movimentoX = 0
        
        # Define a imagem de fundo do jogo
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
        
        # Bloco de código para mostrar o Leão e as consoantes e aumenta velocidade das letras
        display.blit(leao, (posicaoLeaoX, posicaoLeaoY))
        display.blit(vogais, ((vogalPosicaoX, vogalPosicaoY)))
        display.blit(consoantes, ((consoantePosicaoX, consoantePosicaoY)))
        vogalPosicaoY = vogalPosicaoY + velocidade
        consoantePosicaoY = consoantePosicaoY + velocidade

        # Verifica se a letra ultrapassou a tela e inicia ela novamente em outro local
        if vogalPosicaoY > altura:
            Vogal()
            vogais = font.render(Vogal(), True, black)
            vogalPosicaoY = -30
            vogalPosicaoX = random.randrange(0, largura-50)

        if consoantePosicaoY > altura:
            Consoante()
            consoantes = font.render(Consoante(), True, black)
            consoantePosicaoY = -30
            consoantePosicaoX = random.randrange(0, largura-50)
            velocidade += 0.5

        # Bloco de código que verifica se houve colisão entre o leão e as letras
        if posicaoLeaoY < vogalPosicaoY + letraAltura:
            if posicaoLeaoX < vogalPosicaoX and posicaoLeaoX + leaoLargura > vogalPosicaoX or vogalPosicaoX + letraLargura > posicaoLeaoX and vogalPosicaoX + letraLargura < posicaoLeaoX + leaoLargura:
                contador += 1
                Vogal()
                vogais = font.render(Vogal(), True, black)
                vogalPosicaoY = -30
                vogalPosicaoX = random.randrange(0, largura-50)

        if posicaoLeaoY < consoantePosicaoY + letraAltura:
            if posicaoLeaoX < consoantePosicaoX and posicaoLeaoX + leaoLargura > consoantePosicaoX or consoantePosicaoX + letraLargura > posicaoLeaoX and consoantePosicaoX + letraLargura < posicaoLeaoX + leaoLargura:
                dead(contador)

        pygame.display.update()
        fps.tick(60)

jogo()
