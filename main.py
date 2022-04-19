import pygame

# Inicializa o pygame
pygame.init()

# Cria a tela do jogo
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

# Retangulo de Colisão do Jogador

def playerrectf(x, y):
    playerrect = pygame.Rect(playerX, playerY, 50, 100)
    pygame.draw.rect(screen, (0, 0, 0), playerrect)

# Retangulo de Colisão do Npc

def npcrectf(x, y):
    npcrect = pygame.Rect(npcX+20, npcY, 50, 100)
    pygame.draw.rect(screen, (0, 0, 0), npcrect)

# Retangulo do Tiro do Player

def tiroprectf(x, y):
    tiroprect = pygame.Rect(tiroX+30, tiroY+45, 40, 10)
    pygame.draw.rect(screen, (0, 0, 0), tiroprect)

# Retangulo do Tiro do NPC

def tironrectf(x, y):
    tironrect = pygame.Rect(tironpcX-33, tironpcY+45, 40, 10)
    pygame.draw.rect(screen, (0, 0, 0), tironrect)

def player(x, y, mov):
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


# ARRUMAR SPRITE DE MOVIMENTAÇÃO NPC <<<<<<<<
def npc(x, y, movn):
    if movn == 1:
        screen.blit(npci, (x, y))
    elif movn == 3:
        screen.blit(npciright, (x, y))
    elif movn == 2:
        screen.blit(npcileft, (x, y))


# Tiros

tiroi = pygame.image.load('laserRed.png')
tiroX = 25
tiroY = 0
tiroX_change = 1
tiroV = 1

tironpci = pygame.image.load('laserGreen.png')
tironpcX = 900
tironpcY = 0
tironpcX_change = 1
tironpcV = 1


def tiro(x, y):
    screen.blit(tiroi, (x + 30, y + 45))
    global tiroV
    tiroV = 0


def tironpc(x, y):
    screen.blit(tironpci, (x - 30, y + 45))
    global tironpcV
    tironpcV = 0


# Loop do Jogo
rodando = True
while rodando:

    #Tela branca pra ver o retangulo
    screen.fill((255,255,255))

    # Desenhando os retangulos de colisão
    playerrectf(playerX, playerY)

    npcrectf(npcX, npcY)

    tiroprectf(tiroX, tiroY)

    tironrectf(tironpcX, tironpcY)

    # Desenha o background
    #bg()

    # Verifica se a variavel de verificação do tiro do npc é 1 para atirar novamente
    if tironpcV == 1:
        tironpcY = npcY
        tironpc(tironpcX, tironpcY)



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
            # Atirar
            if event.key == pygame.K_SPACE:
                if tiroV == 1:
                    tiroY = playerY
                    tiro(tiroX, tiroY)
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

    # Movimentação do tiro do player
    if tiroX >= 1000:
        tiroX = 25
        tiroV = 1
    if tiroV == 0:
        tiro(tiroX, tiroY)
        tiroX += tiroX_change

    # Movimentação do tiro do npc
    if tironpcX <= 0:
        tironpcX = 900
        tironpcV = 1
    if tironpcV == 0:
        tironpc(tironpcX, tironpcY)
        tironpcX -= tironpcX_change

    # Delimitando o limite da tela
    if playerY <= 0:
        playerY = 0
    elif playerY >= 710:
        playerY = 710

    # Mudando Y do Player e NPC e Renderizando
    npcY += npcY_change
    playerY += playerY_change
    player(playerX, playerY, mov)
    npc(npcX, npcY, movn)

    #Da update no display da tela todo lopp
    pygame.display.update()

