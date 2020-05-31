
import pygame
import sys

pygame.init()
screen=pygame.display.set_mode([600,600])

x=300
y=300

gesch=3
breite=30
hoehe=40

go=True

while go:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit

        gedruckt=pygame.key.get_pressed()
        if gedruckt[pygame.K_UP]:
            y-=gesch
        if gedruckt[pygame.K_DOWN]:
            y+=gesch
        if gedruckt[pygame.K_RIGHT]:
            x+=gesch
        if gedruckt[pygame.K_LEFT]:
            x-=gesch