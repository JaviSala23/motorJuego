from pymunk_ejemplos.intro import *
from recursos import colores


b0 = space.static_body
segment = pymunk.Segment(b0, (0, 35), (800, 35), 4)
segment.elasticity = 1

circulo(1, 10, (50,200), 0.95,30)
space.add(segment)

App().run()