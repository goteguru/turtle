from turtle import Turtle

class Shapes:
    def __init__(self):
        pass


class Arrow(Shapes):
    def __init__(self, direction, size):
        self.direction = direction
        self.size = size
        Shapes.__init__(self)

class Rectangle(Shapes):
    def __init__(self,height, width):
        self.height = height
        self.width = width
        t = Turtle()
        self.path = t.go(height).turn(90).go(width).turn(90).go(height).turn(90).go(width).path
        Shapes.__init__(self)

class Polygon(Shapes):
    def __init__(self,angle,size):
        self.angle = angle
        self.size = size
        t = Turtle()
        n = 360 / angle
        self.path = n*(t.go(size).turn(angle)).path
        Shapes.__init__(self)

