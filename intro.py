"""sacado de https://pymunk-tutorial.readthedocs.io/en/latest/intro/intro.html#a-bouncing-ball"""


from recursos import colores
import pymunk
import pymunk.pygame_util
import pygame

space = pymunk.Space()
space.gravity = 0, -900
b0 = space.static_body


class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((700, 240))
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
        self.running = True

    def run(self):
        reloj = pygame.time.Clock()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.image.save(self.screen, 'intro.png')

            self.screen.fill(colores.Navy)
            space.debug_draw(self.draw_options)
            pygame.display.update()
            space.step(0.01)
            reloj.tick(60)


if __name__ == '__main__':
    p0, p1 = (0, 0), (700, 0)
    segment = pymunk.Segment(b0, p0, p1, 4)
    segment.elasticity = 1

    body = pymunk.Body(mass=1, moment=10)
    body.position = (100, 200)

    circle = pymunk.Circle(body, radius=30)
    circle.elasticity = 0.95
    space.add(body, circle, segment)

    App().run()