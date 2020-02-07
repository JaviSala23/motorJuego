from pymunk_ejemplos.intro import *
from recursos import colores


b0 = space.static_body
segment = pymunk.Segment(b0, (0, 35), (800, 35), 4)
segment.elasticity = 1


space.add(segment)

App().run()