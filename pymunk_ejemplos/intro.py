import pymunk
import pymunk.pygame_util
import pygame
from recursos import colores
pygame.init()
space = pymunk.Space()
space.gravity = 0, -900

class circulo:
    def __init__(self, masa, momentum, posicion, elasticidad,radio):
        self.masa=masa
        self.momentum=momentum
        self.elasticidad=elasticidad
        self.body = pymunk.Body()
        self.radio = radio
        self. posicion= posicion
        self.body = pymunk.Body(mass=self.masa, moment=self.momentum)
        self.body.position = self.posicion

        circle = pymunk.Circle(self.body, radius=self.radio)
        circle.elasticity = self.elasticidad
        space.add(self.body,circle)




class App:
    size = 800, 540
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
        self.running = True

    def run(self):
        
        img=pygame.image.load("img/assets/Tiles/grass.png")
        img=pygame.transform.smoothscale(img, (40,40))
        reloj=pygame.time.Clock()
        while self.running:
            tecla = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.image.save(self.screen, 'intro.png')

            self.screen.fill(colores.Lime)
            space.debug_draw(self.draw_options)
            j=0
            for l in range(100):
                self.screen.blit(img,(0+j,500))
                j=j+30
            pygame.display.update()
            print(space.body)
            space.step(0.01)
            reloj.tick(60)
        pygame.quit()

