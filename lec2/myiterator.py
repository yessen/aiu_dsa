class MyIterator():
  """ MyIterator class shows how to implement 
      a basic iterator containing a list of numbers
      Attributes:
        L - list of numbers
        idx - pointer to the current position in the list
  """
  L = [1,2,3,4,5,6]
  idx = 0

  def __iter__(self):
    """ Returns itself """
    return self
 
  def __next__(self):
    """ Returns the next element in the list  """
    if self.idx < len(self.L):
      item = self.L[self.idx]
      self.idx += 1
      return item
    else:
      raise StopIteration

if __name__ == "__main__":
  # create an object of MyIterator class
  p = MyIterator()

  # traverse a list and print its content
  for item in p:
    print(item)
