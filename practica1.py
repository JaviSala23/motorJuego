from pymunk_ejemplos.intro import *
from recursos import colores


b0 = space.static_body
segment = pymunk.Segment(b0, (0, 35), (800, 35), 4)
segment.elasticity = 1

body = pymunk.Body(mass=1, moment=10)
body.position = 100, 200

circle = pymunk.Circle(body, radius=30)
circle.elasticity = 0.95
space.add(body, circle, segment)

App().run()