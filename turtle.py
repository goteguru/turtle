from math import sin,cos,pi

class Turtle:
    def __init__(self,x=0,y=0):
        self.origin=x,y
        self.path=[self.origin]
        self.angle=0
        self.place=self.origin
    
    def turn(self, angle):
        self.angle+=angle
        return self
    
    def go(self, dist):
        x,y=self.place
        x+=dist*sin(self.angle/180*pi)
        y+=dist*cos(self.angle/180*pi)
        self.place=x,y
        self.path.append((round(x),round(y)))
        return self
    
    def close(self):
        self.path.append(self.origin)
        return self
    
if __name__=="__main__":
    t=Turtle()
    t.turn(90).go(30).turn(90).go(30).close()
    print (t.path)
    
    