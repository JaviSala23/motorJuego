from pymunk_ejemplos.intro import *
from recursos import colores


b0 = space.static_body
segment = pymunk.Segment( b0,(2, 19), (800, 19), 4)
segment.elasticity = 0.99


body = pymunk.Body(mass=100, moment=100)
body.position = 100, 500

circle = pymunk.Circle(body,radius=30)
circle.elasticty = 0.99
space.add(body, circle, segment)

App().run()