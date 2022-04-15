import pygame

#Inicializa o pygame
pygame.init()

#Cria a tela do jogo
screen = pygame.display.set_mode((1000, 800))

# Icone, Titulo e Background
pygame.display.set_caption("Space Duel")
icone = pygame.image.load('logo.png')
pygame.display.set_icon(icone)
bgi = pygame.image.load("bg.png")


def bg():
    screen.blit(bgi, (0, 0))


# Jogador
playeri = pygame.image.load('player.png')
playeriright = pygame.image.load('playerRight.png')
playerileft = pygame.image.load('playerLeft.png')
playerX = 25
playerY = 350
playerY_change = 0


def player(x,y):
    screen.blit(playeri, (x, y))


# 2 Jogar
player2i = pygame.image.load('player2.png')
player2iright = pygame.image.load('player2Right.png')
player2ileft = pygame.image.load('player2Left.png')
player2X = 900
player2Y = 350
player2Y_change = 0

def player2(x,y):
    pressed = 1
    if pressed == 1:
        screen.blit(player2i, (x, y))
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
                screen.blit(player2ileft, (x, y))
                pressed = 0
        if event.key == pygame.K_UP:
                screen.blit(player2iright, (x, y))
                pressed = 0
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_DOWN or pygame.K_DOWN:
            pressed =1






# Loop do Jogo
rodando = True
while rodando:

    bg()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                playerY_change = 5
                player2Y_change = 3
            if event.key == pygame.K_UP:
                playerY_change = -5
                player2Y_change = -3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or pygame.K_DOWN:
                playerY_change = 0
                player2Y_change = 0

    player2Y += player2Y_change
    playerY += playerY_change
    player(playerX,playerY)
    player2(player2X, player2Y)

    pygame.display.update()