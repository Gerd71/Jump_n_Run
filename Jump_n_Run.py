
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
angriffLinks=sprung=pygame.image.load("Grafiken/angriffLinks.png")
angriffRechts=sprung=pygame.image.load("Grafiken/angriffRechts.png")
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
        self.last=[1,0]
        self.ok=True
    def laufen(self,liste):
        if liste[0]:
            self.x-=self.gesch
            #States for player [links,rechts,stand,sprung]
            self.richtg=[1,0,0,0]
            self.schritteLinks+=1
        if liste[1]:
            self.x+=self.gesch
            #States for player [links,rechts,stand,sprung]
            self.richtg=[0,1,0,0]
            self.schritteRechts+=1

    def resetSchritte(self):
        self.schritteLinks=0
        self.schritteRechts=0

    def stehen(self):
        #States for player [links,rechts,stand,sprung]
        self.richtg=[0,0,1,0]
        self.resetSchritte()
    def sprungSetzen(self):
        if self.sprungvar==-16:
            self.sprung=True
            self.sprungvar=15
            pygame.mixer.Sound.play(sprungSound)
    def springen(self):
        if self.sprung:
            #States for player [links,rechts,stand,sprung]
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
            self.last=[1,0]
        #Schritte Rechts animation
        if self.richtg[1]:
            screen.blit(rechtsGehen[self.schritteRechts//8],(self.x,self.y))
            self.last=[0,1]
        #Stehen animation
        if self.richtg[2]:
            if self.last[0]:
                screen.blit(angriffLinks,(self.x,self.y))
            else:
                screen.blit(angriffRechts,(self.x,self.y))
        #Springen animation
        if self.richtg[3]:
            screen.blit(sprung,(self.x,self.y))

class kugel:
    def __init__(self,spx,spy,richtung,radius,farbe,gesch):
        self.x=spx
        self.y=spy
        if richtung[0]:
            self.x+=5
            self.gesch=-1*gesch
        elif richtung[1]:
            self.x+=92
            self.gesch=gesch
        self.y+=84
        self.radius=radius
        self.farbe=farbe
    def bewegen(self):
        self.x+=self.gesch
    def zeichnen(self):
        pygame.draw.circle(screen,self.farbe,(self.x,self.y),self.radius,0)

class zombie():
    def __init__(self,x,y,gesch,breite,hoehe,richtg,xMin,xMax):
        self.x=x
        self.y=y
        self.gesch=gesch
        self.breite=breite
        self.hoehe=hoehe
        self.richtg=richtg
        self.schritteRechts=0
        self.schritteLinks=0
        self.xMin=xMin
        self.xMax=xMax
        self.leben=6
        self.linksListe = [pygame.image.load("Grafiken/l1.png"),pygame.image.load("Grafiken/l2.png"),pygame.image.load("Grafiken/l3.png"),pygame.image.load("Grafiken/l4.png"),pygame.image.load("Grafiken/l5.png"),pygame.image.load("Grafiken/l6.png"),pygame.image.load("Grafiken/l7.png"),pygame.image.load("Grafiken/l8.png")]
        self.rechtsListe = [pygame.image.load("Grafiken/r1.png"),pygame.image.load("Grafiken/r2.png"),pygame.image.load("Grafiken/r3.png"),pygame.image.load("Grafiken/r4.png"),pygame.image.load("Grafiken/r5.png"),pygame.image.load("Grafiken/r6.png"),pygame.image.load("Grafiken/r7.png"),pygame.image.load("Grafiken/r8.png")]
        self.ganz = pygame.image.load("Grafiken/voll.png")
        self.halb = pygame.image.load("Grafiken/halb.png")
        self.leer = pygame.image.load("Grafiken/leer.png")

    def herzen(self):
        if self.leben>=2:
            screen.blit(self.ganz,(507,15))
        if self.leben>=4:
            screen.blit(self.ganz,(569,15))
        if self.leben==6:
            screen.blit(self.ganz,(631,15))
        if self.leben==1:
            screen.blit(self.halb,(507,15))
        elif self.leben==3:
            screen.blit(self.halb,(569,15))
        elif self.leben==5:
            screen.blit(self.halb,(631,15))
        if self.leben<=0:
            screen.blit(self.leer,(507,15))
        if self.leben<=2:
            screen.blit(self.leer,(569,15))
        if self.leben<=4:
            screen.blit(self.leer,(631,15))

    def zZeichnen(self):
        if self.schritteRechts==63:
            self.schritteRechts=0   
        if self.schritteLinks==63:
            self.schritteLinks=0

        if self.richtg[0]:
            screen.blit(self.linksListe[self.schritteLinks//8],(self.x,self.y))
        if self.richtg[1]:
            screen.blit(self.rechtsListe[self.schritteRechts//8],(self.x,self.y))

    def laufen(self):
        self.x+=self.gesch
        if self.gesch>0:
            self.richtg=[0,1]
            self.schritteRechts+=1
        if self.gesch<0:
            self.richtg=[1,0]
            self.schritteLinks+=1

    def hinher(self):
        if self.x>self.xMax:
            self.gesch*=-1
        elif self.x<self.xMin:
            self.gesch*=-1
        self.laufen()

def zeichnen():
    screen.blit(hintergrund,(0,0))
    for k in kugeln:
        k.zeichnen()
    spieler1.spZeichnen()
    zombie1.zZeichnen()
    zombie1.herzen()
  
    pygame.display.update()

def kugel_handler():
    global kugeln
    for k in kugeln:
       if k.x>=0 and k.x<=1200:
           k.bewegen()
       else:
           kugeln.remove(k)

def kollision():
    global kugeln
    zombieRechteck=pygame.Rect(zombie1.x+18,zombie1.y+24,zombie1.breite-36,zombie1.hoehe-24)
    
    for k in kugeln:
        kugelRechteck=pygame.Rect(k.x-k.radius,k.y-k.radius,k.radius*2,k.radius*2)
        if zombieRechteck.colliderect(kugelRechteck):
            kugeln.remove(k)
            zombie1.leben-=1


#Field Boarders
linkeWand=pygame.draw.rect(screen,(0,0,0),(-2,0,2,600),0)
rechteWand=pygame.draw.rect(screen,(0,0,0),(1201,0,2,600),0)

#Generate Spieler und Zombie
spieler1=spieler(300,393,5,96,128,-16,[0,0,1,0],0,0)
zombie1=zombie(600,393,4,96,128,[0,0],40,1000)

#Das Array fuer die Kugeln
kugeln=[]

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

    if gedrueckt[pygame.K_SPACE]:
        if len(kugeln)<=4 and spieler1.ok:
            kugeln.append(kugel(round(spieler1.x),round(spieler1.y),spieler1.last,8,(0,0,0),7))

        spieler1.ok=False
    if not gedrueckt[pygame.K_SPACE]:
        spieler1.ok=True

   
    kugel_handler()
    zombie1.hinher()
    kollision()
    zeichnen()

    clock.tick(60)