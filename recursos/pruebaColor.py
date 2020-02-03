#!/usr/bin/python
# -*- coding: utf-8-*-

import pygame
import colores

pygame.init()
   

dimensiones = [1020,630]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Recurso de Colores")

 
hecho = False
fuente = pygame.font.Font(None, 25)
 

negro = fuente.render("Black", True, colores.White)
rojo = fuente.render("Red", True, colores.White)
lima = fuente.render("Lime", True, colores.Black)
azul = fuente.render("Blue", True, colores.White)
amarillo= fuente.render("Yellow", True, colores.Black)
cyan= fuente.render("Cyan", True, colores.Black)
magenta=fuente.render("Magenta", True, colores.White)
plata=fuente.render("Silver", True, colores.Black)
gris=fuente.render("Gray", True, colores.White)
marron=fuente.render("Maroon", True, colores.White)
olive=fuente.render("Olive", True, colores.White)
verde=fuente.render("Green", True, colores.Black)
purpura=fuente.render("Purple", True, colores.White)
teal=fuente.render("Teal", True, colores.White)
navy=fuente.render("Navy", True, colores.White)


 
reloj = pygame.time.Clock()
i=0

while not hecho:
    if i==14:
        i=0
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
     
    pantalla.fill(colores.White)
    pygame.draw.rect(pantalla, colores.Black, [10, 20, 200, 200])
    pantalla.blit(negro, [15, 25])
    pygame.draw.rect(pantalla, colores.Red, [210, 20, 200, 200])
    pantalla.blit(rojo, [215, 25])
    pygame.draw.rect(pantalla, colores.Lime, [410, 20, 200, 200])
    pantalla.blit(lima, [415, 25])
    pygame.draw.rect(pantalla, colores.Blue, [610, 20, 200, 200])
    pantalla.blit(azul, [615, 25])
    pygame.draw.rect(pantalla, colores.Yellow, [810, 20, 200, 200])
    pantalla.blit(amarillo, [815, 25])
    pygame.draw.rect(pantalla, colores.Cyan, [10, 220, 200, 200])
    pantalla.blit(cyan, [10, 225])
    pygame.draw.rect(pantalla, colores.Magenta, [210, 220, 200, 200])
    pantalla.blit(magenta, [215, 225])
    pygame.draw.rect(pantalla, colores.Silver, [410, 220, 200, 200])
    pantalla.blit(plata, [415, 225])
    pygame.draw.rect(pantalla, colores.Gray, [410, 220, 200, 200])
    pantalla.blit(gris, [415, 225])
    pygame.draw.rect(pantalla, colores.Maroon, [610, 220, 200, 200])
    pantalla.blit(marron, [615, 225])
    pygame.draw.rect(pantalla, colores.Olive, [810, 220, 200, 200])
    pantalla.blit(olive, [815, 225])
    pygame.draw.rect(pantalla, colores.Green, [10, 420, 200, 200])
    pantalla.blit(verde, [15, 425])
    pygame.draw.rect(pantalla, colores.Purple, [10, 420, 200, 200])
    pantalla.blit(purpura, [15, 425])
    pygame.draw.rect(pantalla, colores.Teal, [210, 420, 200, 200])
    pantalla.blit(teal, [215, 425])
    pygame.draw.rect(pantalla, colores.Navy, [410, 420, 200, 200])
    pantalla.blit(teal, [415, 425])
 
    pygame.display.flip()
 

    reloj.tick(5)
    
    i=i+1

pygame.quit()