from point import Point

class ColorPoint(Point):
   def __init__(self, x=0, y=0, color="black"):
      super().__init__(x,y)
      self.color = color

   # print the coordinates
   def print_xy(self):
      print("color: " + self.color)
      return "This is a " + self.color + " point located at " + \
            super().print_xy()

   def dist(self, rhsPoint):
      dx = self.x - rhsPoint.x
      dy = self.y - rhsPoint.y
      return math.sqrt( dx ** 2 + dy ** 2 )

class ShapePoint(Point):
   def __init__(self, x=0, y=0, shape="circle"):
      super().__init__(x,y)
      self.shape = shape

   # print the coordinates
   def print_xy(self):
      print("shape: " + self.shape)
      return "This is a " + self.shape + " point located at " + \
            super().print_xy()

   def dist(self, rhsPoint):
      a = self.x ** 2
      b = rhsPoint.x ** 2
      dy = rhsPoint.y - self.y
      c = 2 * self.x * rhsPoint.x * dy 
      return math.sqrt( a + b - c) 

if __name__ == "__main__":
  pc = ColorPoint(0, 0)
  print(pc.print_xy())
  ps = ShapePoint(1,1)
  print(ps)
