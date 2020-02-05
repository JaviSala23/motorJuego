from pymunk_ejemplos.intro import *
from recursos import colores


segment = pymunk.Segment(b0, (2, 140), (800, 140), 22)
segment.elasticity = 0.5
segment.friction = 0.5

body = pymunk.Body(mass=1, moment=10)
body.position = (100, 200)

circle = pymunk.Circle(body, radius=20)
circle.elasticty = 0.5
circle.friction = 0.5
space.add(body, circle, segment)

App().run()