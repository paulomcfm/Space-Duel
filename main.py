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
mov = 1


def player(x,y, mov):
    if mov == 1:
        screen.blit(playeri, (x, y))
    elif mov == 2:
        screen.blit(playeriright, (x, y))
    elif mov == 3:
        screen.blit(playerileft, (x, y))


# NPC
npci = pygame.image.load('player2.png')
npciright = pygame.image.load('player2Right.png')
npcileft = pygame.image.load('player2Left.png')
npcX = 900
npcY = 350
npcY_change = 0
movn = 1

def npc(x,y, movn):
    if movn == 1:
        screen.blit(npci, (x, y))
    elif movn == 3:
        screen.blit(npciright, (x, y))
    elif movn == 2:
        screen.blit(npcileft, (x, y))


# Loop do Jogo

rodando = True
while rodando:

    bg()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        # Movimentação do Player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                playerY_change = 6
                mov = 2
            if event.key == pygame.K_UP:
                playerY_change = -5
                mov = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or pygame.K_DOWN:
                playerY_change = 0
                mov = 1

    # Movimentação do NPC
    if npcY < playerY and npcY != playerY:
        npcY_change = 3
        movn = 2
    elif npcY > playerY and npcY != playerY:
        npcY_change = -3
        movn = 3
    elif npcY == playerY:
        npcY_change = 0
        movn = 1

    # Mudando Y do Player e NPC e Renderizando
    npcY += npcY_change
    playerY += playerY_change
    player(playerX, playerY, mov)
    npc(npcX, npcY, movn)

    pygame.display.update()