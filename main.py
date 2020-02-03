#!/usr/bin/python
# -*- coding: utf-8-*-

import pygame
from recursos import colores

pygame.init()
   
# Establecemos las dimensiones de la pantalla [largo,altura]
dimensiones = [700,500]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Mi Primer juego en Informatica")
color=[colores.Blue,colores.Green,colores.White,colores.Black,colores.Red,colores.Lime,
       colores.Yellow,colores.Cyan,colores.Magenta,colores.Silver,colores.Gray,colores.Maroon,
       colores.Olive,colores.Purple,colores.Teal,colores.Navy]
#El bucle se ejecuta hasta que el usuario hace click sobre el botón de cierre.
 
hecho = False
 
  
# Se usa para establecer cuan rápido se actualiza la pantalla
 
reloj = pygame.time.Clock()
i=0
# -------- Bucle principal del Programa -----------
while not hecho:
    if i==14:
        i=0
    
    # --- Bucle principal de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
     
    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ
  
    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ
     
    # Primero, limpia la pantalla con blanco. No vayas a poner otros comandos de dibujo encima 
    # de esto, de otra forma serán borrados por este comando:
    pantalla.fill(color[i])
     
    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()
 
    # --- Limitamos a 60 fotogramas por segundo (frames per second)
    reloj.tick(5)
    
    i=i+1
# Cerramos la ventana y salimos.
# Si te olvidas de esta última línea, el programa se 'colgará'
# al salir si lo hemos estado ejecutando desde el IDLE.
pygame.quit()