class Point:
    """ This is a class Point with
        attributes:
          x, y - coordinates of a point
        class method: 
          print_xy - function that prints x and y
    """
    # constructor of the class
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # print the coordinates
    def print_xy(self):
        print("x = ", self.x)
        print("y = ", self.y)
        return "("+str(self.x)+", "+ str(self.y)+")"

    # overload equal operator
    def __eq__( self, rhsPoint ):
        return self.x == rhsPoint.x and \
               self.y == rhsPoint.y

    def __str__(self):
       return self.print_xy() 
 
if __name__ == "__main__":
   # create the first object
   p = Point()
   p.print_xy() 

   # create the second object
   q = Point(1,1)
   q.print_xy() 

   if p == q:
      print("equal")
   else:
      print("not equal")

   print(p)
   print(q)
