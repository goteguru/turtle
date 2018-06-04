from turtle import Turtle

class Shapes:
    def __init__(self, x=0, y=0):
        self.turtle = Turtle(x,y)
        pass


class Arrow(Shapes):
    def __init__(self, direction, size,x=0, y=0):
        self.direction = direction
        self.size = size
        Shapes.__init__(self,x,y)

class Rectangle(Shapes):
    def __init__(self,height, width,x=0, y=0):
        self.height = height
        self.width = width
        Shapes.__init__(self,x,y)
        self.path = self.turtle.go(height).turn(90).go(width).turn(90).go(height).turn(90).go(width).path

class Polygon(Shapes):
    def __init__(self,angle,size,x=0, y=0):
        self.angle = angle
        self.size = size
        n = 360 / angle
        Shapes.__init__(self,x,y)
        self.path = n*(self.turtle.go(size).turn(angle)).path


