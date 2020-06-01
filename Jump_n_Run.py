
import pygame
import sys

#Init
pygame.init()
hintergrund=pygame.image.load("Grafiken/hintergrund.png")
screen=pygame.display.set_mode([1200,595])
clock=pygame.time.Clock()
pygame.display.set_caption("Jumpy by Gerd Harlander")
sprungSound=pygame.mixer.Sound("Sounds/sprung.wav")

#Load png´s for the 4 different states
stehen=pygame.image.load("Grafiken/stand.png")
sprung=pygame.image.load("Grafiken/sprung.png")

#List with 8 pictures for Animation
rechtsGehen = [pygame.image.load("Grafiken/rechts1.png"),pygame.image.load("Grafiken/rechts2.png"),pygame.image.load("Grafiken/rechts3.png"),pygame.image.load("Grafiken/rechts4.png"),pygame.image.load("Grafiken/rechts5.png"),pygame.image.load("Grafiken/rechts6.png"),pygame.image.load("Grafiken/rechts7.png"),pygame.image.load("Grafiken/rechts8.png")]
linksGehen = [pygame.image.load("Grafiken/links1.png"),pygame.image.load("Grafiken/links2.png"),pygame.image.load("Grafiken/links3.png"),pygame.image.load("Grafiken/links4.png"),pygame.image.load("Grafiken/links5.png"),pygame.image.load("Grafiken/links6.png"),pygame.image.load("Grafiken/links7.png"),pygame.image.load("Grafiken/links8.png")]

class spieler:
    def __init__(self,x,y,gesch,breite,hoehe,sprungvar,richtg,schritteRechts,schritteLinks):
        self.x=x
        self.y=y
        self.gesch=gesch
        self.breite=breite
        self.hoehe=hoehe
        self.sprungvar=sprungvar
        self.richtg=richtg
        self.schritteRechts=schritteRechts
        self.schritteLinks=schritteLinks
        self.sprung=False
    def laufen(self,liste):
        if liste[0]:
            self.x-=self.gesch
            self.richtg=[1,0,0,0]
            self.schritteLinks+=1
        if liste[1]:
            self.x+=self.gesch
            self.richtg=[0,1,0,0]
            self.schritteRechts+=1

    def resetSchritte(self):
        self.schritteLinks=0
        self.schritteRechts=0

    def stehen(self):
        self.richtg=[0,0,1,0]
        self.resetSchritte()
    def sprungSetzen(self):
        if self.sprungvar==-16:
            self.sprung=True
            self.sprungvar=15
            pygame.mixer.Sound.play(sprungSound)
    def springen(self):
        if self.sprung:
            self.richtg=[0,0,0,1]
            if self.sprungvar>=-15:
                n=1
                if self.sprungvar<0:
                    n=-1
                self.y-=(self.sprungvar**2)*0.17*n
                self.sprungvar-=1
            else:
                self.sprung=False
    def spZeichnen(self):
        if self.schritteRechts==63:
            self.schritteRechts=0
        if self.schritteLinks==63:
            self.schritteLinks=0

        #Schritte Links animation
        if self.richtg[0]:
            screen.blit(linksGehen[self.schritteLinks//8],(self.x,self.y))
        #Schritte Rechts animation
        if self.richtg[1]:
            screen.blit(rechtsGehen[self.schritteRechts//8],(self.x,self.y))
        #Stehen animation
        if self.richtg[2]:
            screen.blit(stehen,(self.x,self.y))
        #Springen animation
        if self.richtg[3]:
            screen.blit(sprung,(self.x,self.y))

def zeichnen():
    screen.blit(hintergrund,(0,0))
    spieler1.spZeichnen()
    pygame.display.update()

#Field Boarders
linkeWand=pygame.draw.rect(screen,(0,0,0),(-2,0,2,600),0)
rechteWand=pygame.draw.rect(screen,(0,0,0),(1201,0,2,600),0)

#Generate Spieler
spieler1=spieler(300,393,5,96,128,-16,[0,0,1,0],0,0)

#States for player [links,rechts,stand,sprung]
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
    spielerRechteck=pygame.Rect(spieler1.x,spieler1.y,40,80)
    gedrueckt=pygame.key.get_pressed()
    
    
    if gedrueckt[pygame.K_RIGHT] and not spielerRechteck.colliderect(rechteWand):
        spieler1.laufen([0,1])
    elif gedrueckt[pygame.K_LEFT] and not spielerRechteck.colliderect(linkeWand):
       spieler1.laufen([1,0])
    else:
        spieler1.stehen()

    if gedrueckt[pygame.K_UP]:
        spieler1.sprungSetzen()
    spieler1.springen()
     
    zeichnen()

    clock.tick(60)