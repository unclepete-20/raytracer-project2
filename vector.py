class V3(object):

  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
    self.values = (x, y, z)

  
  def __add__(self, other):
    return V3((self.x + other.x), (self.y + other.y), (self.z + other.z))

  
  def __sub__(self, other):
    return V3((self.x - other.x), (self.y - other.y), (self.z - other.z))

  
  def __mul__(self, other):

    
    if ((type(other) == int) or (type(other) == float)):
      return V3((other * self.x), (other * self.y), (other * self.z))

    
    return V3(
      ((self.y * other.z) - (self.z * other.y)),
      ((self.z * other.x) - (self.x * other.z)),
      ((self.x * other.y) - (self.y * other.x)),
    )

  
  def __matmul__(self, other):
    return ((self.x * other.x) + (self.y * other.y) + (self.z * other.z))

  
  def length(self):
    return (((self.x ** 2) + (self.y ** 2) + (self.z ** 2)) ** 0.5)

  
  def norm(self):
    return ((self * (1 / self.length())) if (self.length() != 0) else V3(1, 1, 1))

  
  def __repr__(self):
    return f"<{self.x}, {self.y}, {self.z}>"
