import pymunk
import pymunk.pygame_util
import pygame

GRAY = (220, 220, 220)

pygame.init()
size = 640, 240
screen = pygame.display.set_mode(size)
draw_options = pymunk.pygame_util.DrawOptions(screen)

space = pymunk.Space()
space.gravity = 0, -900

b0 = space.static_body
segment = pymunk.Segment(b0, (2, 19), (800, 19), 4)
segment.elasticity = 1

body = pymunk.Body(mass=1, moment=10)
body.position = 100, 200

circle = pymunk.Circle(body, radius=30)
circle.elasticity = 0.95
space.add(body, circle, segment)

running = True
reloj=pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.image.save(screen, 'intro1.png')

    screen.fill(GRAY)
    space.debug_draw(draw_options)
    pygame.display.update()
    space.step(0.01)
    reloj.tick(60)
pygame.quit()