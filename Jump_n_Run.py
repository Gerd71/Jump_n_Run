
import pygame
import sys

#Init
pygame.init()
hintergrund=pygame.image.load("Grafiken/hintergrund.png")
screen=pygame.display.set_mode([1200,595])
clock=pygame.time.Clock()
pygame.display.set_caption("Jumpy by Gerd Harlander")

def zeichnen():
    screen.blit(hintergrund,(0,0))
    pygame.draw.rect(screen,(0,0,255),(x,y,breite,hoehe))
    pygame.display.update()

#Variables
x=300
y=440
gesch=5
breite=40
hoehe=80
sprungvar=-16

linkeWand=pygame.draw.rect(screen,(0,0,0),(-2,0,2,600),0)
rechteWand=pygame.draw.rect(screen,(0,0,0),(1201,0,2,600),0)

#Main Game Loop
go=True
while go:
    #Event Sink
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit
    spielerRechteck=pygame.Rect(x,y,40,80)
    gedrueckt=pygame.key.get_pressed()
    if gedrueckt[pygame.K_UP] and sprungvar==-16:
        sprungvar=15
    if gedrueckt[pygame.K_RIGHT] and not spielerRechteck.colliderect(rechteWand):
        x+=gesch
    if gedrueckt[pygame.K_LEFT] and not spielerRechteck.colliderect(linkeWand):
        x-=gesch
    if sprungvar>=-15:
        n=1
        if sprungvar<0:
            n=-1
        y-=(sprungvar**2)*0.17*n
        sprungvar-=1

    zeichnen()
    clock.tick(60)