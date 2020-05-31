
import pygame
import sys

#Init
pygame.init()
hintergrund=pygame.image.load("Grafiken/hintergrund.png")
screen=pygame.display.set_mode([1200,595])
clock=pygame.time.Clock()
pygame.display.set_caption("Jumpy by Gerd Harlander")

stehen=pygame.image.load("Grafiken/stand.png")
sprung=pygame.image.load("Grafiken/sprung.png")

rechtsGehen = [pygame.image.load("Grafiken/rechts1.png"),pygame.image.load("Grafiken/rechts2.png"),pygame.image.load("Grafiken/rechts3.png"),pygame.image.load("Grafiken/rechts4.png"),pygame.image.load("Grafiken/rechts5.png"),pygame.image.load("Grafiken/rechts6.png"),pygame.image.load("Grafiken/rechts7.png"),pygame.image.load("Grafiken/rechts8.png")]
linksGehen = [pygame.image.load("Grafiken/links1.png"),pygame.image.load("Grafiken/links2.png"),pygame.image.load("Grafiken/links3.png"),pygame.image.load("Grafiken/links4.png"),pygame.image.load("Grafiken/links5.png"),pygame.image.load("Grafiken/links6.png"),pygame.image.load("Grafiken/links7.png"),pygame.image.load("Grafiken/links8.png")]

def zeichnen(liste):
    global schritteRechts
    global schritteLinks

    screen.blit(hintergrund,(0,0))

    if schritteRechts==63:
        schritteRechts=0
    if schritteLinks==63:
        schritteLinks=0

    if liste[0]:
        screen.blit(linksGehen[schritteLinks//8],(x,y))

    if liste[1]:
        screen.blit(rechtsGehen[schritteRechts//8],(x,y))
    if liste[2]:
        screen.blit(stehen,(x,y))
    if liste[3]:
        screen.blit(sprung,(x,y))
    pygame.display.update()

#Variables
x=300
y=390
gesch=5
breite=40
hoehe=80
sprungvar=-16

linkeWand=pygame.draw.rect(screen,(0,0,0),(-2,0,2,600),0)
rechteWand=pygame.draw.rect(screen,(0,0,0),(1201,0,2,600),0)

#[links,rechts,stand,sprung]
richtg=[0,0,0,0]
schritteRechts=0
schritteLinks=0

#Main Game Loop
go=True
while go:
    #Event Sink
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit
    spielerRechteck=pygame.Rect(x,y,40,80)
    gedrueckt=pygame.key.get_pressed()
    richtg=[0,0,1,0]
    if gedrueckt[pygame.K_UP] and sprungvar==-16:
        sprungvar=15
    if gedrueckt[pygame.K_RIGHT] and not spielerRechteck.colliderect(rechteWand):
        x+=gesch
        richtg=[0,1,0,0]
        schritteRechts+=1
    if gedrueckt[pygame.K_LEFT] and not spielerRechteck.colliderect(linkeWand):
        x-=gesch
        richtg=[1,0,0,0]
        schritteLinks+=1
    if sprungvar>=-15:
        richtg=[0,0,0,1]
        n=1
        if sprungvar<0:
            n=-1
        y-=(sprungvar**2)*0.17*n
        sprungvar-=1
    if richtg[2] or richtg[3]:
        schritteRechts=0
        schritteLinks=0
        
    zeichnen(richtg)
    clock.tick(60)