from turtle import Turtle

class Shapes:
<<<<<<< HEAD
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
=======
    def __init__(self, x=0, y=0):
        self.turtle = Turtle(x,y)
        pass
    def path(self):
        return self.turtle.path

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
        self.turtle.go(height).turn(90).go(width).turn(90).go(height).turn(90).go(width)

class Polygon(Shapes):
    def __init__(self,num,size,x=0, y=0):
        angle = (1 - 2 / num) * 180
        self.angle = angle
        self.size = size
        Shapes.__init__(self,x,y)
        for _ in range(num):
             self.turtle.go(size).turn(angle)





>>>>>>> 9a9879a972f9216427cb015535301ddc690c305b

